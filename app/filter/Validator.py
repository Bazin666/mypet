import functools
from enum import Enum
from flask import request, jsonify
import re


def default_error(*args,**kwargs):
    return jsonify({'code': '123123', 'msg': '增加失败，请重新提交'})

def default_get_entry(entryName):
    return request.form.get(entryName)



def get_entry(entryName):
    return request.form.get(entryName,'')


def validator(*rules):
    def wrapper(func):
        @functools.wraps(func)
        def call(*args, **kwargs):
            items = rules
            for i in items:
                entryName = i['args']['entry'] or ''
                entry = get_entry(entryName)
                args = i['args']['args'] or ''
                ru = i['rule'] or (lambda *args,**kwargs: 'error')
                wrapper = [entry]
                if args:
                    wrapper.extend(args)
                if not ru(*wrapper):
                    return default_error()
            return func()
        return call
    return wrapper



def li(entry, length):
    return len(entry) < length


def notnull(entry):
    return entry != '' and entry != None


def range(entry, low, up):
    return low < len(entry) < up


def regex(entry, reg):
    return re.match(reg, entry)


class Rules(Enum):
    limit = lambda entryName, length: {'rule': li, 'args': {'entry': entryName, 'args': {length}}}
    range = lambda entryName, low, up: {'rule': range, 'args': {'entry': entryName, 'args': {low, up}}}
    notnull = lambda entryName: {'rule': notnull, 'args': {'entry': entryName, 'args': None}}
    regex = lambda entryName, reg: {'rule': regex, 'args': {'entry': entryName, 'args': {reg}}}
