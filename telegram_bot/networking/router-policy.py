from cisco_xr import route_xr
from cisco_xe import route_xe
from juniper import routepolicy
from huawei import huawei_policy
from vyos import vyos_policy

options = {
    1: routepolicy,
    2: route_xe,
    3: route_xr,
    4: huawei_policy,
    5: vyos_policy
}

while True:
    print()
    print('Choose the policy to be configured:')
    print()
    print('1 - Juniper')
    print('2 - Cisco-XE')
    print('3 - Cisco-XR')
    print('4 - Huawei')
    print('5 - VyOS')
    print('0 - Exit')
    print()
    
    try:
        opcao = int(input('Enter the option number: '))
        if opcao == 0:
            break
        elif opcao in options:
            selected_function = options[opcao]
            selected_function()
        else:
            print('Invalid option. Please choose a valid option.')
    except ValueError:
        print('Invalid input. Please enter a valid number.')

print('Exiting...')
