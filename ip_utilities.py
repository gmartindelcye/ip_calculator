from dataclasses import dataclass


def validate_ip(s:str) -> bool:
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def validate_cidr(s:str) -> bool:
    if len(s) == 0:
        return False
    if s[0] != '/':
        return False
    if not s[1:].isdigit():
        return False
    i = int(s[1:])
    if i < 8 or i > 30:
        return False
    return True


def cidr2netmask(c:str) -> str:
    """ Transform cidr notation to netmask"""
    if not validate_cidr(c):
        return ''
    cidr = int(c[1:])
    mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
    return (
            str((0xff000000 & mask) >> 24) + '.' +
            str((0x00ff0000 & mask) >> 16) + '.' +
            str((0x0000ff00 & mask) >> 8) + '.' +
            str((0x000000ff & mask)) 
           )


def netmask2cidr(s:str) -> str:
    if not validate_ip(s):
        return ''
    cidr = sum(bin(int(x)).count('1') for x in s.split('.'))
    return f"/{cidr}"


def ip2bin(i:str) -> str:
    octets = i.split('.')
    b = ''
    for n in octets:
        x = bin(int(n))[2:]
        b += x.zfill(8)
    return b


def bin2ip(s:str) -> str:
    i = ''
    for x in range(4):
        n = s[8*x:8*(x+1)]
        i += str(int(n,2))
        if x < 3:
            i += '.'
    return i


def binary_and(a:str, b:str) -> str:
    """ Makes AND operation between binary strings"""
    x = int(a,2)
    y = int(b,2)
    z = x & y
    return bin(z)[2:]


def binary_or(a:str, b:str) -> str:
    """ Makes OR operation between binary strings"""
    x = int(a,2)
    y = int(b,2)
    z = x | y
    return bin(z)[2:]


def binary_not(a:str) -> str:
    """ Makes binary string NOT or Invert operation"""
    z = ''
    for x in a:
        if x == '1':
            z += '0'
        else:
            z += '1'
    return z


def get_network(ip:str, netmask:str) -> str:
    i = ip2bin(ip)
    n = ip2bin(netmask)
    m = binary_and(i,n)
    return bin2ip(m)


def get_broadcast(ip:str, netmask:str) -> str:
    i = ip2bin(ip)
    n = ip2bin(netmask)
    nn = binary_not(n)
    b = binary_or(i,nn)
    return bin2ip(b)


def str2dict(s:str) -> dict:
    """ 
    Converts a string with pairs separated
    by spaces and values with colons
    """
    result = dict((a,b) for a, b in (element.split(':') for element in s.split(' ')))
    return result


@dataclass
class GenericIP:
    ip: str
    network : str
    netmask : str
    cidr: str
    broadcast: str

    def __init__(self,ip:str='',network:str='',netmask:str='',cidr:str='',broadcast:str='') -> None:
        if validate_ip(ip): 
            self.ip = ip
        else:
            self.ip = None
        if validate_ip(network):
            self.network = network
        else:
            self.network = None
        if validate_ip(netmask):
            self.netmask = netmask
        else:
            self.netmask = None
        if validate_cidr(cidr):
            self.cidr = cidr
        else:
            self.cidr = None
        if validate_ip(broadcast):
            self.broadcast = broadcast
        else:
            self.broadcast = None


    def __repr__(self) -> str:
        if self.ip == None:
            return 'None'
        return self.ip


    def __str__(self) -> str:
        return self.__repr__()


    def info(self) -> str:
        return f"ip:{self.ip} network:{self.network} cidr:{self.cidr} netmask:{self.netmask} broadcast:{self.broadcast}"


    def calculate_values(self) -> None:
        if not self.ip:
            return "Error: No ip set."
        if(not self.cidr) or (self.netmask):
            return "Error: CIDR o netmask not provided."
        if self.cidr and not self.netmask:
            self.netmask = cidr2netmask(self.cidr)
        self.network = get_network(self.ip,self.netmask)
        self.cidr = netmask2cidr(self.netmask)
        self.broadcast = get_broadcast(self.ip,self.netmask)


    def dict(self) -> dict:
        return str2dict(self.info())


def main():
    a = GenericIP('192.168.0.101', cidr='/24')
    a.calculate_values()
    j = a.json()
    print(j)
 
if __name__ == '__main__':
    main()