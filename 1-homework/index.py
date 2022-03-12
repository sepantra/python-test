# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:27:08 2022

@author: Gv Shop
"""

Names=["Sayid","Moeen","Setareh"]
Roles=["Project Manager","Web Developer","Python Programmer"]

new={ "Hello "+Names[i]:"Role:" +Roles[i] for i in range(3)}
import pprint
pprint.pprint(new)
