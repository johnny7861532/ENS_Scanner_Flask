#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:37:20 2018

@author: johnnyhsieh
"""

from web3 import HTTPProvider, Web3
from ens import ENS
from ens.registrar import Status

provider = HTTPProvider('https://mainnet.infura.io')
web3 = Web3(provider)
web3.eth.blockNumber

ns = ENS(provider)

def Scanner(str):
    return ns.owner(str)

def check(str):
    
    if ns.registrar.status(str) == Status.Owned :
        return Scanner(str)
    elif ns.registrar.status(str) == Status.Revealing:
        return "Status.Revealing"
    elif ns.registrar.status(str) == Status.Auctioning:
        return "Status.Auctioning"  
    elif ns.registrar.status(str) == Status.Open:
        return "Status.Open"
    else:
        return "None"
        
    
check('johnnyhsiehh')
