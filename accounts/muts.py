import graphene
from django.db.models import Q
from graphene import String, Boolean, Field, List

from accounts.dots import UserDot

from accounts.models import User, Token
from accounts.utils import (
    validate_user_email,
    email_veryfication,
    activate_user_account,
    send_password_reset_email,
    change_password,
    digits, normalize_and_validate_phone)


class Auth(graphene.Mutation):
    class Arguments:
        login = String(required=True)
        password = String(required=True)

    ok = Boolean()
    token = String()
    user = Field(UserDot)
    errors = List(String)

    @staticmethod
    def mutate(root, info, login, password):
        lg = login.lower()
        if "@" in lg:
            cond = Q(email=lg)
        else:
            cond = Q(username=lg)
        user = User.objects.filter(cond).first()
        if user is not None and user.check_password(password):
            token = Token.objects.create(user=user)
            return Auth(ok=True, token=token.id, user=user)
        return Auth(ok=False, errors=["Электрон адрес яки серсүз туры килми."])


class Reg(graphene.Mutation):
    class Arguments:
        email = String(required=True)
        password = String(required=True)
        password_repeat = String(required=True)

    ok = Boolean()
    token = String()
    user = Field(UserDot)
    errors = List(String)

    @staticmethod
    def mutate(self, info, email, password, password_repeat):
        if password == password_repeat:
            # verification_code = get_random_string(6, allowed_chars=string.digits)
            email = email.lower()

            if validate_user_email(email) == False:
                return Reg(ok=False, errors=[
                    "Электрон адресыгызны дөрес языгыз",
                ])

            if User.objects.filter(email=email).exists():
                return Reg(ok=False, errors=[
                    "Бу электрон адрес безнең системада регистрацияләнгән.",
                    "Шул email'ны кулланып, керегез. Әгәр серсүзегезне онытсагыз, серсүзне яңарту бүлегенә басыгыз."
                ])

            user = User(
                email=email,
                username=email,
                is_active=False,
            )

            user.set_password(password)
            user.save()
            email_veryfication(user, info)
            token = Token.objects.create(user=user)

            return Reg(ok=True, token=token.id, user=user)

        return Reg(ok=False, errors=["Серсүзләр туры килми."])


class UpdateUser(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        middle_name = graphene.String()
        bio = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        city_name = graphene.String()

    ok = Boolean()
    user = Field(UserDot)
    errors = List(String)

    @staticmethod
    def mutate(self, info, first_name=None, last_name=None, middle_name=None, email=None, phone=None, city_name=None):
        try:
            user = info.context.user

            if not user:
                return UpdateUser(ok=False, errors=["Кулланучы табылмады."])
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if middle_name:
                user.middle_name = middle_name
            if email:
                if validate_user_email(email) == False:
                    return Reg(ok=False, errors=[
                        "Электрон адресыгызны дөрес языгыз",
                    ])

                # if user.email == email:
                #     return Reg(ok=False, errors=[
                #         "Это ваш старый электронный адрес.",
                #     ])

                same_email_user = User.objects.filter(email=email).first()
                if same_email_user != user and User.objects.filter(email=email).exists():
                    return Reg(ok=False, errors=[
                        "Бу электрон адрес безнең системада регистрацияләнгән.",
                        "Шул email'ны кулланып, керегез. Әгәр серсүзегезне онытсагыз, серсүзне яңарту бүлегенә басыгыз."
                    ])

                user.email = email
            if phone:
                # phone, is_valid_phone = normalize_and_validate_phone(phone)
                # if is_valid_phone != True:
                #     return Reg(ok=False, errors=[
                #         "Телефон номерын дөрес итеп языгыз"
                #     ])
                user.phone_number = phone

            if city_name:
                user.city = city_name
            user.save()
            return UpdateUser(ok=True, user=user)
        except:
            return UpdateUser(ok=False, errors=["Пользователь не найден."])


class Logout(graphene.Mutation):
    class Arguments:
        pass

    ok = Boolean()

    @staticmethod
    def mutate(self, info):
        user = info.context.user
        if user:
            Token.objects.filter(user=user).first().delete()
            return Logout(ok=True)


class Activate(graphene.Mutation):
    class Arguments:
        uidb64 = graphene.String(required=True)
        token = graphene.String(required=True)

    ok = Boolean()
    errors = List(String)

    @staticmethod
    def mutate(self, info, uidb64, token):
        ok, errors = activate_user_account(uidb64, token)
        return Activate(ok=ok, errors=errors)


class StartPasswordReset(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    ok = Boolean()
    errors = List(String)

    @staticmethod
    def mutate(self, info, email):
        errors = None
        try:
            user = User.objects.get(email=email)
            send_password_reset_email(info, user)
            return StartPasswordReset(ok=True, errors=errors)
        except User.DoesNotExist:
            return StartPasswordReset(ok=False, errors=['Мондый email адрес белән кулланучы юк'])


class EndPasswordReset(graphene.Mutation):
    class Arguments:
        uidb64 = graphene.String(required=True)
        token = graphene.String(required=True)
        password = graphene.String(required=True)
        passwordRepeat = graphene.String(required=True)

    ok = Boolean()
    errors = List(String)

    @staticmethod
    def mutate(self, info, uidb64, token, password, passwordRepeat):
        ok, errors = change_password(uidb64, token, password, passwordRepeat)
        return EndPasswordReset(ok=ok, errors=errors)


class ChangePassword(graphene.Mutation):
    class Arguments:
        password = graphene.String(required=True)
        passwordRepeat = graphene.String(required=True)

    ok = Boolean()
    errors = List(String)

    @staticmethod
    def mutate(self, info, password, passwordRepeat):
        user = info.context.user
        if user:
            if password == passwordRepeat:
                user.set_password(password)
                user.save()
                return ChangePassword(ok=True, errors=None)
            else:
                return ChangePassword(ok=False, errors=['Серсүзләр туры килми'])
        return ChangePassword(ok=False, errors=['Кулланучы системага кермәгән'])







class Mutation(graphene.ObjectType):
    login = Auth.Field()
    reg = Reg.Field()
    update_user = UpdateUser.Field()
    logout = Logout.Field()
    activate = Activate.Field()
    start_password_reset = StartPasswordReset.Field()
    end_password_reset = EndPasswordReset.Field()
    change_password = ChangePassword.Field()
