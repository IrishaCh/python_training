__author__ = 'Irina.Chegodaeva'
import datetime


class PostfixHelper:

    def __init__(self, app):
        self.app = app
        t = datetime.datetime.now()
        self.substring = "_" + t.strftime("%d%m%Y") + "_" + t.strftime("%H%M%S")
