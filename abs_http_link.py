'''
@author: Abdelrahman Moez - aka Hydra
@script: abs_http.py
@description: This snippet returns the absolute http link of any given link.
              Return example: http://DOMAIN.COM
@python version: 2.7
'''

def abs_http(link):
    http_link = link
    if http_link.startswith("www."):
        http_link = http_link[4:]
        http_link = "".join(("http://",http_link))
    if http_link.startswith("http://www."):
        http_link = http_link[11:]
        http_link = "".join(("http://",http_link))
    if not http_link.startswith("http://"):
        http_link = "".join(("http://",http_link))
    return http_link

# Uncomment the next line to test this on Google!
#print abs_http('google.com')
