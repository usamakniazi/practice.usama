import socket
import psutil

def get_ip_addresses(family):
ip address 192.168.121.254 255.255.255.248 





    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                yield (interface, snic.address)


ip address 172.82.255.1 255.255.255.248




