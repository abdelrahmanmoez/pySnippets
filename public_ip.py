'''
@author: Abdelrahman Moez - aka Hydra
@script: public_ip.py
@description: This snippet is to get your public ip address.
@python version: 2.7
'''

# import needed modules
import re
import urllib2

def public_ip():
    # setting the website to use to get the public ip
    address = "http://www.ipchicken.com"
    # grabbing source code of the page
    src_code = urllib2.urlopen(address).read()
    # parsing public ip
    public_ip = re.search(r'\d+\.\d+\.\d+\.\d+', src_code).group()
    return public_ip

# layout public ip
print public_ip()
