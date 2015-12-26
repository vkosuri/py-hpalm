# py - HPALM
Python HP ALM RESTful Client

Using the REST API, you can interact with the ALM Platform.


HTTP return codes are used:

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
