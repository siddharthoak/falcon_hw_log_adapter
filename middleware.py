# middleware.py

from context import ctx

class RequestIDMiddleware:
    def process_request(self, req, resp):
        ctx.request_id = req.get_header("request_id")
        ctx.tenant_id = req.get_header("tenant_id")
