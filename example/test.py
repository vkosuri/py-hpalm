
from src.hpalm import HPALM
domain='test'
project='test'
base_url = "http://10.11.200.1:8080"
username ="vkosuri"
password="pass@007"
hp=HPALM(base_url=base_url,username=username,password=password,domain=domain,project=project)
hp.login()
hp.logout()
