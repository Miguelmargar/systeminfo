'''
Created on 29 Jan 2019

@author: User
'''

from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system info",
      url="",
      author="Miguel Martinez",
      author_email="miguel.martinez@ucdconnect.ie",
      licence="GPL3",
      packages=["systeminfo"],
      entry_points={'console_scripts':['comp30830_systeminfo=systeminfo.main:main']}
      )