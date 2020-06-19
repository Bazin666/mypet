import functools
from enum import Enum
from app.filter import validator,Rules
# class Validator(object):
#     def get_entry(self,entry):
#         return entry
#
#     def __init__(self):
#         self.error_method = default_error
#         self.get_entry = default_get_entry
#
#
#     def error(self, error_method):
#         self.error_method = error_method
#
#     def data_grid(self,func):
#         self.get_entry = func
#
#     def __call__(self, func):
#         items = self._args
#         for i in items:
#             entryName = i['args']['entry'] or ''
#             entry = self.get_entry(entryName)
#             args = i['args']['args'] or ''
#             ru = i['rule'] or (lambda *args,**kwargs: 'error')
#             wrapper = [entry]
#             if args:
#                 wrapper.append(*args)
#
#             if not ru(*wrapper):
#                 return self.error_method
#
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     def validator(self, *args, **kwargs):
#         self._args = args
#         self.kwargs = kwargs
#         items = self._args
#         for i in items:
#             entryName = i['args']['entry'] or ''
#             entry = self.get_entry(entryName)
#             args = i['args']['args'] or ''
#             ru = i['rule'] or (lambda *args,**kwargs: 'error')
#             wrapper = [entry]
#             if args:
#                 wrapper.append(*args)
#
#             if not ru(*wrapper):
#                 return self.error_method
#         def call(func):
#             @functools.wraps(func)
#             def wrapper(*args, **kwargs):
#                 return func(*args, **kwargs)
#
#             return wrapper





@validator(Rules.limit('name',2))
def t(name = 1):
    print(name)

t(name = 123123123)
