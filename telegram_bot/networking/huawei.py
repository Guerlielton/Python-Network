# Using F string and increment numbers in Cisco router-map and Huawei router-policy init in 100 increments 10 
def huawei_policy():
    arq = open('Huawei-Route-Policy.txt','w')
    count = 0
    v4 = 0
    v6 = 0
    no = 100
    file = open('asn-list.txt', 'r')
    t = []
    for line in file.readlines():
        line = line.rstrip()
        t.append(line)
    for i in range(len(t)):
        if 'AS' in t[i]: 
             count = count + 1
             no = no + 10 
             v4 = v4 + 10
             v6 = v6 + 10
             k = 1
             ipv4 = []
             ipv6 = []
             while ('/' in t[i+k] ):
                 if ('::' in t[i+k]):
                     ipv6.append(i+k)
                 else:
                     ipv4.append(i+k)
                 k = k + 1
             for l in range(len(ipv4)): 
                 subnet = (t[ipv4[l]])[len(t[ipv4[l]])-2:]
                 if (subnet == '24'):
                     print(f'ip ip-prefix PL-{t[i]}-V4 index 10 permit {t[ipv4[l]].replace("/"," ")} \n',file=arq) #Remove "/" for huawei cli 
                 else:
                     print(f'ip ip-prefix PL-{t[i]}-V4 index 10 permit {t[ipv4[l]].replace("/"," ")} greater-equal {subnet} less-equal 24\n',file=arq) #Remove "/" for huawei cli 
                     
             print(f'route-policy eBGP-DOWNSTREAM-ASN-53019-AJU-IN permit node {no}',file=arq)
             print(f'if-match ip-prefix PL-{t[i]}-V4',file=arq)
             print('apply local-preference 700',file=arq)
             print('apply community 53087:200 53087:298 additive',file=arq)
             print('\n',file=arq)
             for p in range(len(ipv6)):
                 subnet = (t[ipv6[p]])[len(t[ipv6[p]])-2:]
                 if (subnet == '48'):
                     print(f'ip ipv6-prefix PL-{t[i]}-V6 index 10 permit {t[ipv6[p]].replace("/"," ")} \n',file=arq) #Remove "/" for huawei cli
                 else:
                     print(f'ip ipv6-prefix PL-{t[i]}-V6 index 10 permit {t[ipv6[p]].replace("/"," ")} greater-equal {subnet} less-equal 48\n',file=arq) #Remove "/" for huawei cli
                 print(f'route-policy eBGP-DOWNSTREAM-ASN-53019-AJU-V6-IN permit node {no}',file=arq)
                 print(f'if-match ipv6 address prefix-list PL-{t[i]}-V6',file=arq)
                 print('apply local-preference 700',file=arq)
                 print('apply community 53087:200 53087:298 additive \n',file=arq)
                 print('------------------------------------------------------------------------------------------------',file=arq)
    print('Huawei VRP')
    print('Have been configured',count,'Route Policy')
if __name__ == '__main__':
    huawei_policy()
