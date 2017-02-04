py - hpalm
==========

Python HP ALM RESTful Client

Using the REST API, you can interact with the ALM Platform.

``` Bash
virtuenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

``` Python
from hpalm import HPALM
hp = HPALM(host='10.11.200.1', username='vkosuri', password='pass', domain='test', project='test')
hp.login()
```

HTTP return codes are used
--------------------------

|  Code | Cause                                               |
|-------|-----------------------------------------------------|
| 200   | successful operations                               |
| 201   | successful POST operations that create a new entity |
| 401   | unauthenticated request                             |
| 403   | unauthorized operations                             |
| 404   | resource not found                                  |
| 405   | method not supported by resource                    |
| 406   | unsupported ACCEPT type                             |
| 415   | unsupported request content type                    |
| 500   | Internal server error                               |
