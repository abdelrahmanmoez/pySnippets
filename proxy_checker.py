'''
@author: Abdelrahman Moez - aka Hydra
@script: proxy_checker.py
@description: This snippet checks if given proxy ip:port is working or not
              
@python version: 2.7
'''

import urllib2
import re

# -----------------------------------------------------------------
def get_public_ip():
    address = "http://www.ipchicken.com"
    string = urllib2.urlopen(address).read()
    public_ip = re.search(r'\d+\.\d+\.\d+\.\d+', string).group()    
    return public_ip
# -----------------------------------------------------------------
def test_proxy(proxy_ip, proxy_port):
    proxy = urllib2.ProxyHandler({'http':proxy_ip+':'+proxy_port})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    install = urllib2.install_opener(opener)
    current_ip = get_public_ip()
    if real_ip == current_ip:
        return False
    else:
        return True
# -----------------------------------------------------------------
real_ip = get_public_ip()
# Change the next ip and port to what you need to test 
if test_proxy('211.142.236.137',8000) == True:
    print 'Proxy is working good'
else:
    print 'Proxy is not working'
