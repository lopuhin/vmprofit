import inspect
from functools import wraps
import platform
import tempfile
import time
import sys

import vmprof
from vmshare.service import Service


def upload(name, filename, host, auth):
    service = Service(host, auth)
    interpname = platform.python_implementation()
    service.post({Service.FILE_CPU_PROFILE: filename,
                  Service.FILE_JIT_PROFILE: filename + '.jit',
                  'argv': name,
                  'VM': interpname })


class profile(object):
    def __init__(self, web_url='http://vmprof.com', auth=None):
        self.web_url = web_url
        self.auth = auth
        self._prof_file = None
        self._t0 = None

    def _start_profiling(self):
        assert self._prof_file is None
        self._prof_file = tempfile.NamedTemporaryFile(delete=False)
        self._t0 = time.time()
        vmprof.enable(self._prof_file.fileno(), lines=True)

    def _stop_profiling(self, name, disabled=False):
        if not disabled:
            vmprof.disable()
        dt = time.time() - self._t0
        self._prof_file.close()
        sys.stderr.write(
            '{name} took {dt:.4f} s. Compiling and uploading to {web_url}\n'
            .format(name=name, dt=dt, web_url=self.web_url))
        upload(name=name, filename=self._prof_file.name,
               host=self.web_url, auth=self.auth)
        self._prof_file = None
        self._t0 = None

    def __call__(self, fn):
        @wraps(fn)
        def deco(*args, **kwargs):
            self._start_profiling()
            try:
                return fn(*args, **kwargs)
            finally:
                self.stop_profiling(fn.__name__)
        return deco

    def __enter__(self):
        self._start_profiling()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        vmprof.disable()
        line, name = inspect.stack()[1][2:4]
        name = 'with block in {} at line {}'.format(name, line)
        self._stop_profiling(name, disabled=True)
