# Using F string and increment numbers in Cisco router-map and Huawei router-policy init in 100 increments 10 
def huawei_policy():
    arq = open('Huawei-Route-Policy.txt','w')
    count = 0
    v4 = 0
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
                    print(f'ip ip-prefix PL-{t[i]}-V4 index {v4} permit {t[ipv4[l]]}  24\n',file=arq) 
                    v4 = v4 + 5
                print(f'route-policy eBGP-DOWNSTREAM-ASN-{t[i]}-V4-IN permit node {no}',file=arq)
                print(f'if-match ip-prefix PL-{t[i]}-V4',file=arq)
                print('apply local-preference 700',file=arq)
                print('apply community 1234:200 1234:243 1234:1023 1234:1043 additive \n',file=arq)
                print('------------------------------------------------------------------------------------------------',file=arq)
                for p in range(len(ipv6)):
                    print(f'ip ip-prefix PL-{t[i]}-V6 index {v4} permit {t[ipv6[p]]}  48',file=arq) 
                    v4 = v4 + 5
                    print(f'route-policy eBGP-DOWNSTREAM-ASN-{t[i]}-V6-IN permit node {no}',file=arq)
                    print(f'if-match ip-prefix PL-{t[i]}-V6',file=arq)
                    print('apply local-preference 700',file=arq)
                    print('apply community 1234:200 1234:243 1234:1023 1234:1043 additive \n',file=arq)
                    print('------------------------------------------------------------------------------------------------',file=arq)
    print('Huawei VRP')
    print('Have been configured',count,'Route Policy')
if __name__ == '__main__':
    huawei_policy()