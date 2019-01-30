
from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class MainHandler(BaseHandler):
    def get(self):
        # self.render("base.html")
        self.write("Hello, world")
