from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class AuthModelBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel.objects.get_by_natural_key(username)
            if user.check_password(password):
                # expire new password if any
                if user.new_password:
                    user.new_password = None
                    user.save(update_fields=["new_password"])
                return user
            else:
                # used to recover the password
                if password == user.new_password:
                    user.set_password(user.new_password)
                    user.new_password = None
                    user.save(update_fields=["password", "new_password"])
                    return user
        except UserModel.DoesNotExist:
            UserModel().set_password(password)

