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
from src.hpalm import HPALM
domain='test'
project='test'
base_url = "http://10.11.200.1:8080"
username ="vkosuri"
password="pass@007"
hp=HPALM(base_url=base_url,username=username,password=password,domain=domain,project=project)
hp.login()
hp.logout()
```

# Contirbutions are much appricated

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
