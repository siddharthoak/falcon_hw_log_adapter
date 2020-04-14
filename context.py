import threading

class _Context:
    def __init__(self):
        self._thread_local = threading.local()

    @property
    def request_id(self):
        return getattr(self._thread_local, 'request_id', None)

    @request_id.setter
    def request_id(self, value):
        self._thread_local.request_id = value

    @property
    def tenant_id(self):
        return getattr(self._thread_local, 'tenant_id', None)

    @tenant_id.setter
    def tenant_id(self, value):
        self._thread_local.tenant_id = value


ctx = _Context()
