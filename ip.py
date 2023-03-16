from ip_utilities import GenericIP, netmask2cidr, validate_cidr, validate_ip
from network_base_address import get_network_info, d2str


def parse_ip_or_net(s: str):
    if '/' in s:
        ip, cidr = s.split('/')
        cidr = '/' + cidr
        tipe = 'c'
    elif ' ' in s:
        ip, cidr = s.split(' ')
        tipe = 'm'
    
    if not (validate_ip(ip) and (validate_cidr(cidr) or validate_ip(cidr))):
        ip = ''
        cidr = ''
        tipe = ''

    
    return ip, cidr, tipe


def ask_ip():
    respuesta = input('Ingrese datos como:\n ip/cidr o ip mask:\n ej, 192.168.1.101/24 o 192,168.1.101 255.255.255.0: ')
    ip, x, t = parse_ip_or_net(respuesta)
    if not t:
        return('Error: datos inválidos.')
    if t == 'm':
        c = netmask2cidr(x)
    else:
        c = x
    a = GenericIP(ip,cidr=c)
    a.calculate_values()
    print('\n',a.info(),'\n')


def ask_net():
    respuesta = input('cidr como /nn o\nmask como w.x.y.z: ')
    datos = get_network_info(respuesta)
    print('\n',d2str(datos),'\n')


def main():
    while True:
        respuesta = int(input('1. ip\n2. red\n0. salir: '))
        if respuesta not in [0, 1, 2]:
            continue
        if not respuesta:
            exit(0)
        if respuesta == 1:
            ask_ip()
        else:
            ask_net()


if __name__ == '__main__':
    main()
   