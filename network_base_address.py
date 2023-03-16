from ip_utilities import validate_cidr, validate_ip, netmask2cidr

network_addresses = [
    {'cidr':'/30', 'ta':4, 'ua':2, 'mask':'255.255.255.252', 'octet':4},
    {'cidr':'/29', 'ta':8, 'ua':6, 'mask':'255.255.255.248', 'octet':4},
    {'cidr':'/28', 'ta':16, 'ua':14, 'mask':'255.255.255.240', 'octet':4},
    {'cidr':'/27', 'ta':32, 'ua':30, 'mask':'255.255.255.224', 'octet':4},
    {'cidr':'/26', 'ta':64, 'ua':62, 'mask':'255.255.255.192', 'octet':4},
    {'cidr':'/25', 'ta':128, 'ua':126, 'mask':'255.255.255.128', 'octet':4},
    {'cidr':'/24', 'ta':256, 'ua':254, 'mask':'255.255.255.0', 'octet':3},
    {'cidr':'/23', 'ta':512, 'ua':510, 'mask':'255.255.254.0', 'octet':3},
    {'cidr':'/22', 'ta':1024, 'ua':1022, 'mask':'255.255.252.0', 'octet':3},
    {'cidr':'/21', 'ta':2048, 'ua':2046, 'mask':'255.255.248.0', 'octet':3},
    {'cidr':'/20', 'ta':4096, 'ua':4094, 'mask':'255.255.240.0', 'octet':3},
    {'cidr':'/19', 'ta':8192, 'ua':8190, 'mask':'255.255.224.0', 'octet':3},
    {'cidr':'/18', 'ta':16384, 'ua':16382, 'mask':'255.255.192.0', 'octet':3},
    {'cidr':'/17', 'ta':32768, 'ua':32766, 'mask':'255.255.128.0', 'octet':3},
    {'cidr':'/16', 'ta':65536, 'ua':65534, 'mask':'255.255.0.0', 'octet':2},
    {'cidr':'/15', 'ta':131072, 'ua':131068, 'mask':'255.254.0.0', 'octet':2},
    {'cidr':'/14', 'ta':262144, 'ua':262140, 'mask':'255.252.0.0', 'octet':2},
    {'cidr':'/13', 'ta':524288, 'ua':524284, 'mask':'255.248.0.0', 'octet':2},
    {'cidr':'/12', 'ta':1048576, 'ua':1048572, 'mask':'255.240.0.0', 'octet':2},
    {'cidr':'/11', 'ta':2097152, 'ua':2097148, 'mask':'255.224.0.0', 'octet':2},
    {'cidr':'/10', 'ta':4194304, 'ua':4194300, 'mask':'255.192.0.0', 'octet':2},
    {'cidr':'/9', 'ta':8388608, 'ua':8388604, 'mask':'255.128.0.0', 'octet':2},
    {'cidr':'/8', 'ta':16777216, 'ua':16777212, 'mask':'255.0.0.0', 'octet':1},
]

def get_network_info(s:str) -> dict:
    if not validate_cidr(s) and not validate_ip(s):
        return {}
    if validate_ip(s):
        c = netmask2cidr(s)
    else:
        c = s

    for l in network_addresses:
        if c == l['cidr']:
            y = l
            break
    
    return y


def d2str(d:dict) -> str:
    if d:
        return f"cidr:{d['cidr']} total addresses:{d['ta']} usable addresses:{d['ua']} netmask:{d['mask']} octet:{d['octet']}"
    else:
        return 'None'

def main():
    a = get_network_info('/24')
    b = get_network_info('255.255.0.0')
    c = get_network_info('')
    d = get_network_info('24')

    print(d2str(a))
    print(d2str(b))
    print(d2str(c))
    print(d2str(d))


if __name__ == '__main__':
    main()