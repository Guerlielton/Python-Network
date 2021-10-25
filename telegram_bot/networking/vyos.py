# Using F string and increment numbers in Cisco router-map and Huawei router-policy init in 100 increments 10 
def vyos_policy():
    arq = open('VyOS-Policy.txt','w')
    count = 0
    file = open('asn-list.txt', 'r')
    t = []
    ru = 1
    for line in file.readlines():
        line = line.rstrip()
        t.append(line)
    for e in range(len(t)):
           if 'AS' in t[e]:   
                ipv6 = []
                ipv4 = []
                k = 1
                while ('/' in t[e+k] ):
                    if ('::' in t[e+k]):
                        ipv6.append(e+k)
                    else:
                        ipv4.append(e+k)
                    k = k + 1
                for l in range(len(ipv4)):
                    print(f'set policy prefix-list ALLOW-PREFIXES-AS-123 rule {ru} action permit',file=arq)
                    print(f'set policy prefix-list ALLOW-PREFIXES-AS-123 rule {ru} le 24',file=arq)
                    print(f'set policy prefix-list ALLOW-PREFIXES-AS-123 rule {ru} prefix {t[ipv4[l]]}\n',file=arq)
                    ru = ru + 1
    print(f'set policy route-map eBGP-DOWNSTREAM-AS-1234-SPO-IN rule 10 action permit',file=arq)
    print(f'set policy route-map eBGP-DOWNSTREAM-AS-1234-SPO-IN rule 10 match ip address prefix-list ALLOW-PREFIXES',file=arq)
    print(f'set policy route-map eBGP-DOWNSTREAM-AS-1234-SPO-IN rule 20 action deny',file=arq) 
                # for p in range(len(ipv6)):
                #     print(f'set policy prefix-list eBGP-DOWNSTREAM-ASN-1234-SPO-IN {t[i]}-V6 from route-filter {t[ipv6[p]]} upto /48',file=arq)
                # print(f'set policy prefix-list eBGP-DOWNSTREAM-ASN-1234-SPO-IN {t[i]}-V6 then local-preference 700',file=arq)
                # print(f'set policy prefix-list eBGP-DOWNSTREAM-ASN-1234-SPO-IN {t[i]}-V6 then community set COSTOMER-ISP',file=arq)
                # print(f'set policy prefix-list eBGP-DOWNSTREAM-ASN-1234-SPO-IN {t[i]}-V6 then community add EXPORT-ONLY-ISP2',file=arq)
                # print(f'set policy prefix-list eBGP-DOWNSTREAM-ASN-1234-SPO-IN {t[i]}-V6 then accept \n',file=arq)
                # print('------------------------------------------------------------------------------------------------',file=arq)
    count = count + 1
    print()        
    print('Have been configured',count,'Routing Policy')
    print('VyOS')
if __name__ == '__main__':
    vyos_policy()