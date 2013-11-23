'''
@author: Abdelrahman Moez - aka Hydra
@script: os_detector.py
@description: This snippet detects the OS in three different ways.
@python version: 2.7
'''
# Way no.1:
import os
print os.name

# Way no.2
import platform
print platform.platform() # this one gives you much info

# Way no.3
import sys
print sys.platform
