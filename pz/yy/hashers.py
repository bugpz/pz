# from django.contrib.auth.hashers import BasePasswordHasher, MD5PasswordHasher
# from django.contrib.auth.hashers import mask_hash
# import hashlib
# from collections import OrderedDict
#
#
# class MyMD5PasswordHasher(MD5PasswordHasher):
#
#
#     def encode(self, password, salt):
#         assert password is not None
#         hash = hashlib.md5(password).hexdigest().upper()
#         return hash
#
#     def verify(self, password, encoded):
#         encoded_2 = self.encode(password, '')
#         return encoded.upper() == encoded_2.upper()
#
#     def safe_summary(self, encoded):
#         algorithm = "mymd5"
#         return OrderedDict([
#             (_('algorithm'), algorithm),
#             (_('salt'), ''),
#             (_('hash'), mask_hash(hash)),
#         ])