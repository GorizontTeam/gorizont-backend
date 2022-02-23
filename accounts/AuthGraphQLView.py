from accounts.models import Token
from django.utils.functional import SimpleLazyObject
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


def get_user_from_token(token):
    if token and token != "null":
        token = Token.objects.filter(id=token).select_related("user").first()
        return token.user
    return None


def get_token(r):
    token = r.META.get('HTTP_AUTHORIZATION')
    if token and token != "null":
        token = Token.objects.filter(id=token.split(" ")[1]).select_related("user").first()
        return token


def get_user(r):
    token = get_token(r)
    if token:
        return token.user
    return None


class AuthMixin:
    @method_decorator(csrf_exempt)
    def dispatch(self, r, *args, **kwargs):
        r.token = SimpleLazyObject(lambda: get_token(r))
        r.user = SimpleLazyObject(lambda: get_user(r))
        return super().dispatch(r, *args, **kwargs)


class AuthGraphQLView(AuthMixin, GraphQLView):
    def execute_graphql_request(self, *args, **kwargs):
        """Extract any exceptions and send them to Sentry"""
        import traceback

        result = super().execute_graphql_request(*args, **kwargs)

        if result and result.errors:
            for error in result.errors:
                try:
                    if hasattr(error, "original_error"):
                        raise error.original_error
                    else:
                        pass
                except Exception:
                    pass
        return result
