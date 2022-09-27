

from dao import db_ucheck, db_insert


def check_user(a1, a2):
    res = db_ucheck(a1, a2)
    return res

def add_user(*args):
    res = db_insert(*args)
    return res