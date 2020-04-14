import logging

import falcon
from werkzeug.serving import run_simple

import custom_logger
from custom_log_adapter import CustomAdapter
from middleware import RequestIDMiddleware
from say_something import SaySomething

app = falcon.API(middleware=RequestIDMiddleware())



class HelloViewAPI:
    """
         This is an endpoint for Hello View
    """
    # logger = logging.getLogger(__name__)
    # logging.basicConfig(level=logging.DEBUG)
    cl = custom_logger.CustomLogger()
    logger = cl.setup_custom_logger(__name__)
    adapter = CustomAdapter(logger, {})

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = "text/plain"
        resp.body = "Hello World!"


    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201
        resp.content_type = "text/plain"
        self.adapter.debug("Added debug for checking")
        ss = SaySomething()
        ss.kuch_bolo()

        resp.body = "Resource added successfully !"
    def on_put(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass


hobj = HelloViewAPI()

app.add_route('/hello', hobj)


if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app, use_reloader=True)
