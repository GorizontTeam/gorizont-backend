import re

import six
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from accounts.models import User, Token
from config.local import EMAIL_HOST_USER, DOMAIN


def digits(string):
    val = "".join([s for s in string if s.isdigit()])
    if len(val) == 11 and val[0] == '8':
        val[0] = 7
    return val


def validate_user_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


def email_veryfication(user, info):
    current_site = get_current_site(info.context)
    mail_subject = 'Аккаунтыгызны активлаштырыгыз'
    message = render_to_string('base/email/email_template.html', {
        'user': user,
        'domain': DOMAIN,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # верно ли?
        'token': account_activation_token.make_token(user),
    })
    send_mail(mail_subject, message, EMAIL_HOST_USER, [user.email])


def activate_user_account(uidb64, token):
    errors = None
    ok = False
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        ok = True
        return ok, errors
    else:
        errors = ['Ссылка для активации недействительна!']
        return ok, errors


def send_password_reset_email(info, user):
    current_site = get_current_site(info.context)
    mail_subject = 'Серсүзне яңарту'
    message = render_to_string('base/email/change_password_email.html', {
        'user': user,
        'domain': DOMAIN,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    send_mail(mail_subject, message, EMAIL_HOST_USER, [user.email])


def change_password(uidb64, token, password, password_repeat):
    errors = None
    ok = False
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if password == password_repeat:
            user.set_password(password)
            user.save()
            ok = True
        else:
            ok = False
            errors = ['Пароли не совпадают']
        return ok, errors
    else:
        errors = ['Ссылка для активации недействительна!']
        return ok, errors


def get_object_or_none(model, **kwargs):
    try:
        a = model.objects.get(**kwargs)
        return a
    except:
        return None


def get_all_objects_with_limit(model, limit=None, offset=0, **kwargs):
    qs = model.objects.filter(**kwargs)
    if limit is not None:
        qs = qs[offset:offset + limit]
    return qs


def normalize_and_validate_phone(phone):
    phone = re.sub('[+()-]', '', str(phone)).replace(' ', '')
    if phone[0] == '8':
        phone_list = list(phone)
        phone_list[0] = '7'
        phone = "".join(phone_list)
    if len(phone) == 11:
        return int(phone), True
    return 0, False








