# show-joserfc-issue

```
pdm install
pdm run pytest
```

```
➜  show-joserfc-issue git:(main) pdm run pytest
======================================= test session starts =======================================
platform darwin -- Python 3.11.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/dino/work/show-joserfc-issue
configfile: pyproject.toml
collected 1 item

test_proof.py F                                                                             [100%]

============================================ FAILURES =============================================
___________________________________________ test_foobar ___________________________________________

    @mock_aws
    def test_foobar():
        c_idp = boto3.client("cognito-idp")
        username = "developer@example.com"
>       user_pool_id, pool_client_id = _setup_cognito(c_idp)

test_proof.py:9:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
test_proof.py:20: in _setup_cognito
    res = c_idp.create_user_pool(
.venv/lib/python3.11/site-packages/botocore/client.py:569: in _api_call
    return self._make_api_call(operation_name, kwargs)
.venv/lib/python3.11/site-packages/botocore/client.py:1005: in _make_api_call
    http, parsed_response = self._make_request(
.venv/lib/python3.11/site-packages/botocore/client.py:1029: in _make_request
    return self._endpoint.make_request(operation_model, request_dict)
.venv/lib/python3.11/site-packages/botocore/endpoint.py:119: in make_request
    return self._send_request(request_dict, operation_model)
.venv/lib/python3.11/site-packages/botocore/endpoint.py:200: in _send_request
    while self._needs_retry(
.venv/lib/python3.11/site-packages/botocore/endpoint.py:360: in _needs_retry
    responses = self._event_emitter.emit(
.venv/lib/python3.11/site-packages/botocore/hooks.py:412: in emit
    return self._emitter.emit(aliased_event_name, **kwargs)
.venv/lib/python3.11/site-packages/botocore/hooks.py:256: in emit
    return self._emit(event_name, kwargs)
.venv/lib/python3.11/site-packages/botocore/hooks.py:239: in _emit
    response = handler(**kwargs)
.venv/lib/python3.11/site-packages/botocore/retryhandler.py:207: in __call__
    if self._checker(**checker_kwargs):
.venv/lib/python3.11/site-packages/botocore/retryhandler.py:284: in __call__
    should_retry = self._should_retry(
.venv/lib/python3.11/site-packages/botocore/retryhandler.py:307: in _should_retry
    return self._checker(
.venv/lib/python3.11/site-packages/botocore/retryhandler.py:363: in __call__
    checker_response = checker(
.venv/lib/python3.11/site-packages/botocore/retryhandler.py:247: in __call__
    return self._check_caught_exception(
.venv/lib/python3.11/site-packages/botocore/retryhandler.py:416: in _check_caught_exception
    raise caught_exception
.venv/lib/python3.11/site-packages/botocore/endpoint.py:276: in _do_get_response
    responses = self._event_emitter.emit(event_name, request=request)
.venv/lib/python3.11/site-packages/botocore/hooks.py:412: in emit
    return self._emitter.emit(aliased_event_name, **kwargs)
.venv/lib/python3.11/site-packages/botocore/hooks.py:256: in emit
    return self._emit(event_name, kwargs)
.venv/lib/python3.11/site-packages/botocore/hooks.py:239: in _emit
    response = handler(**kwargs)
.venv/lib/python3.11/site-packages/moto/core/botocore_stubber.py:38: in __call__
    response = self.process_request(request)
.venv/lib/python3.11/site-packages/moto/core/botocore_stubber.py:68: in process_request
    backend_dict = backends.get_backend(service)  # type: ignore[call-overload]
.venv/lib/python3.11/site-packages/moto/backends.py:753: in get_backend
    return _import_backend(
.venv/lib/python3.11/site-packages/moto/backends.py:342: in _import_backend
    module = importlib.import_module("moto." + module_name)
../../.pyenv/versions/3.11.7/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1204: in _gcd_import
    ???
<frozen importlib._bootstrap>:1176: in _find_and_load
    ???
<frozen importlib._bootstrap>:1147: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:690: in _load_unlocked
    ???
<frozen importlib._bootstrap_external>:940: in exec_module
    ???
<frozen importlib._bootstrap>:241: in _call_with_frames_removed
    ???
.venv/lib/python3.11/site-packages/moto/cognitoidp/__init__.py:1: in <module>
    from .models import cognitoidp_backends  # noqa: F401
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    import datetime
    import enum
    import re
    import time
    import typing
    from collections import OrderedDict
    from typing import Any, Dict, List, Optional, Set, Tuple

>   from joserfc import jwk, jwt
E   ModuleNotFoundError: No module named 'joserfc'

.venv/lib/python3.11/site-packages/moto/cognitoidp/models.py:9: ModuleNotFoundError
===================================== short test summary info =====================================
FAILED test_proof.py::test_foobar - ModuleNotFoundError: No module named 'joserfc'
======================================== 1 failed in 0.32s ========================================
```
