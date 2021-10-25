def route_xr():
    arq = open('Cisco-XR-Route-Policy.txt','w')
    count = 0
    file = open('asn-list.txt', 'r')
    t = []
    for line in file.readlines():
        line = line.rstrip()
        t.append(line)
    for i in range(len(t)):
           if 'AS' in t[i]:   
                count = count + 1
                print(f'prefix-set PL-{t[i]}-V4 \n {t[i+1]} ge 22 le 24',file=arq) 
                print('end-set\n',file=arq)
                print(f'route-policy eBGP-DOWNSTREAM-ASN-{t[i]}-V4-IN',file=arq)
                print(f'  if destination in PL-{t[i]}-V4 then',file=arq)
                print('    set local-preference 700',file=arq)
                print('    set community COSTOMER-ISP additive',file=arq)
                print('    set community EXPORT-ONLY-ISP2 additive',file=arq)
                print('    done \n','endif',file=arq)
                print('------------------------------------------------------------------------------------------------',file=arq)
    print('Cisco IOS-XR')
    print('Have been configured',count,'Route Policy')
if __name__ == "__main__":
    route_xr()