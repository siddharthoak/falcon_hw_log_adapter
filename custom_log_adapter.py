import logging
from context import ctx


class CustomAdapter(logging.LoggerAdapter):


    def debug(self, msg, *args, **kwargs):
        """
        Delegate a debug call to the underlying logger, after adding
        contextual information from this adapter instance.
        """
        msg, kwargs = self.process(msg, kwargs)
        self.logger.debug(msg, *args, **kwargs)

    def process(self, msg, kwargs):
        return '[RequestId: %s - TenantId: %s] %s' % (ctx.request_id, ctx.tenant_id, msg), kwargs
