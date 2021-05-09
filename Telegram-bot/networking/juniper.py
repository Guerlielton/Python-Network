def routepolicy():
    arq = open('Juniper-Policy.txt','w')
    count = 0
    file = open('asn-list.txt', 'r')
    t = []
    for line in file.readlines():
        line = line.rstrip()
        t.append(line)
    for i in range(len(t)):
           if 'AS' in t[i]:   
                ipv6 = []
                ipv4 = []
                k = 1
                while ('/' in t[i+k] ):
                    if ('::' in t[i+k]):
                        ipv6.append(i+k)
                    else:
                        ipv4.append(i+k)
                    k = k + 1
                for l in range(len(ipv4)):
                    print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V4 from route-filter {t[ipv4[l]]} upto /24',file=arq)
                
                print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V4 then local-preference 700',file=arq)
                print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V4 then community set COSTOMER-ISP',file=arq)
                print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V4 then community add EXPORT-ONLY-ISP2',file=arq)
                print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V4 then accept \n',file=arq)

                for p in range(len(ipv6)):
                    print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V6 from route-filter {t[ipv6[p]]} upto /48',file=arq)
                print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V6 then local-preference 700',file=arq)
                print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V6 then community set COSTOMER-ISP',file=arq)
                print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V6 then community add EXPORT-ONLY-ISP2',file=arq)
                print(f'set policy-options policy-statement eBGP-DOWNSTREAM-ASN-1234-SPO-IN term {t[i]}-V6 then accept \n',file=arq)
                print('------------------------------------------------------------------------------------------------',file=arq)
                count = count + 1
    print()        
    print('Have been configured',count,'Routing Policy')
    print('Junos OS')
if __name__ == "__main__":
    routepolicy()
