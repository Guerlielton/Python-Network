import os
import requests
import json
import time
from cisco_xr import route_xr
from cisco_xe import route_xe
from juniper import routepolicy
from huawei import huawei_policy
from vyos import vyos_policy


opcao = -1
while opcao != 0:
    print()
    print('Choose the policy to be configured: ')
    print()
    print('1 - Juniper')
    print('2 - Cisco-XE')
    print('3 - Cisco-XR')
    print('4 - Huawei')
    print('5 - VyOS')
    print('0 - Exit')
    print()
    opcao = int(input('Enter the option number: '))
    if (opcao == 1):
        routepolicy()
    elif (opcao == 2):
        route_xe()
    elif (opcao == 3):
        route_xr()
    elif (opcao == 4):
        huawei_policy()
    elif (opcao == 5):
        vyos_policy()

 #cisco #juniper #huawei #networking #python #automationanywhere #devnet
