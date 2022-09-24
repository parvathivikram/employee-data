

from dao import db_ucheck


def check_user(a1, a2):
    res = db_ucheck(a1, a2)
    return res