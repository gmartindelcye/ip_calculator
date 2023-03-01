from ..ip_utilities import validate_ip, validate_cidr, GenericIP, cidr2netmask, netmask2cidr, ip2bin, bin2ip, binary_and, get_network, binary_or, binary_not, get_broadcast, str2dict


def test_validate_ip():
    assert validate_ip('192.168.1') == False
    assert validate_ip('192.a.1.1') == False
    assert validate_ip('192.168.999.10') == False
    assert validate_ip('192.168.-1.1') == False
    assert validate_ip('192.168.1.1') == True


def test_validate_cidr():
    assert validate_cidr('') == False
    assert validate_cidr('30') == False
    assert validate_cidr('aaa') == False
    assert validate_cidr('/') == False
    assert validate_cidr('/AA') == False
    assert validate_cidr('/0') == False
    assert validate_cidr('/99') == False
    assert validate_cidr('/16') == True


def test_cidr2netmask():
    m = cidr2netmask('/29')
    assert m == '255.255.255.248'
    m = cidr2netmask('/24')
    assert m == '255.255.255.0'
    m = cidr2netmask('/20')
    assert m == '255.255.240.0'
    m = cidr2netmask('/14')
    assert m == '255.252.0.0'
    m = cidr2netmask('/8')
    assert m == '255.0.0.0'


def test_netmask2cidr():
    m = netmask2cidr('255.255.255.248')
    assert m == '/29'
    m = netmask2cidr('255.255.255.0')
    assert m == '/24'
    m = netmask2cidr('255.255.240.0')
    assert m == '/20'
    m = netmask2cidr('255.252.0.0')
    assert m == '/14'
    m = netmask2cidr('255.0.0.0')
    assert m == '/8'


def test_ip2bin():
    b = ip2bin('192.168.2.101')
    assert b == '11000000101010000000001001100101'


def test_bin2ip():
    i = bin2ip('11000000101010000000000000000001')
    assert i == '192.168.0.1'


def test_binary_and():
    a = '11111111111111111111111111111000'
    b = '11000000101010000000001001100101'
    c = binary_and(a,b)
    assert c == '11000000101010000000001001100000'


def test_binary_or():
    a = '11111111111111111111111111111000'
    b = '11000000101010000000001001100101'
    c = binary_or(a,b)
    assert c == '11111111111111111111111111111101'


def test_binary_not():
    a = '11111111111111111111111111111000'
    c = binary_not(a)
    assert c == '00000000000000000000000000000111'


def test_get_network():
    ip = '192.168.101.111'
    nm = '255.255.248.0'
    m = get_network(ip,nm)
    assert m == '192.168.96.0'

def test_get_broadcast():
    ip = '130.45.34.36'
    nm = '255.255.240.0'
    b = get_broadcast(ip,nm)
    assert b == '130.45.47.255'


def test_str2dict():
    s = 'ip:130.45.34.36 network:130.45.32.0 cidr:/20 netmask:255.255.240.0 broadcast:130.45.47.255'
    d = str2dict(s)
    assert d == {'ip': '130.45.34.36', 'network': '130.45.32.0', 'cidr': '/20', 'netmask': '255.255.240.0', 'broadcast': '130.45.47.255'}


def test_class_empty_GenericIP():
    a = GenericIP()
    assert a.ip == None
    assert a.network == None
    assert a.netmask == None
    assert a.cidr == None
    assert a.broadcast == None
    assert a.info() == "ip:None network:None cidr:None netmask:None broadcast:None"


def test_class_wrong_GenericIP():
    a = GenericIP('192.168.0','AA','999.999.999.999','','-1.-1.-1.-1')
    assert a.info() == "ip:None network:None cidr:None netmask:None broadcast:None"


def test_class_ip_and_cidr_GenericIP():
    a = GenericIP('192.168.0.101', cidr='/24')
    assert a.info() == "ip:192.168.0.101 network:None cidr:/24 netmask:None broadcast:None"


def test_class_GenericIP_calculate_values():
    a = GenericIP('192.168.0.101', cidr='/24')
    a.calculate_values()
    assert a.info() == "ip:192.168.0.101 network:192.168.0.0 cidr:/24 netmask:255.255.255.0 broadcast:192.168.0.255"


def test_class_GenericIP_dict():
    a = GenericIP('192.168.0.101', cidr='/24')
    a.calculate_values()
    d = a.dict()
    assert d == {'ip': '192.168.0.101', 'network': '192.168.0.0', 'cidr': '/24', 'netmask': '255.255.255.0', 'broadcast': '192.168.0.255'}
