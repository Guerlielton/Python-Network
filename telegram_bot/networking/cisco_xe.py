def route_xe():
    arq = open('Cisco-XE-Route-Map.txt','w')
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
                ipv6 = []
                ipv4 =[]
                count = count + 1
                no = no + 10
                k = 1
                while ('/' in t[i+k]):
                    if ('::' in t[i+k]):
                        ipv6.append(i+k)
                    else:
                        ipv4.append(i+k)
                    k = k + 1
                for l in range(len(ipv4)):
                    print(f'ip prefix-list PL-{t[i]}-V4 seq {v4} permit {t[ipv4[l]]} le 24 \n',file=arq) 
                    v4 = v4 + 5 
                print(f'route-map eBGP-DOWNSTREAM-ASN-{t[i]}-V4-IN permit {no}',file=arq)
                print(f'match ip address prefix-list PL-{t[i]}-V4',file=arq)
                print('set local-preference 700',file=arq)
                print('set community 1234:200 1234:243 1234:1023 1234:1043 additive \n',file=arq)
                for p in range(len(ipv6)):
                   print(f'ip prefix-list PL-{t[i]}-V6 seq {v4} permit {t[ipv6[p]]} le 48 \n',file=arq)
                   v4 = v4 + 5 
                print(f'route-map eBGP-DOWNSTREAM-ASN-{t[i]}-V6-IN permit {no}',file=arq)
                print(f'match ip address prefix-list PL-{t[i]}-V6',file=arq)
                print('set local-preference 700',file=arq)
                print('set community 1234:200 1234:243 1234:1023 1234:1043 additive \n',file=arq)
                print('------------------------------------------------------------------------------------------------',file=arq)
    print('Cisco IOS-XE')
    print('Have been configured',count,'Route Map')
if __name__ == "__main__":
    route_xe()
    