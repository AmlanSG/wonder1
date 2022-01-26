# -*- coding: utf-8 -*-
"""
Created on Sun Sep 09 01:57:22 2018

@author: ACER
"""

from Selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "http://www.google.com"
username = "admin"
password = "admin"

xpaths = { 'usernameTxtBox' : "//input[@name='username']",
           'passwordTxtBox' : "//input[@name='password']",
           'submitButton' :   "//input[@name='login']"
         }

mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.maximize_window()