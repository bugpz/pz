# import hashlib
# from yy import models
#
#
# class MyBackend(object):
#     def authenticate(self, username=None, password=None):
#         try:
#             user = models.M_User.objects.get(username=username)
#             print
#             user
#         except Exception:
#             print
#             'no user'
#             return None
#         if hashlib.md5(password).hexdigest().upper() == user.password:
#             return user
#         return None
#
#     def get_user(self, user_id):
#         try:
#             return models.M_User.objects.get(id=user_id)
#         except Exception:
#             return None