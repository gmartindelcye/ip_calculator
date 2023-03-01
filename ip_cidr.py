"""
Determines subnets base on network and CIDR.

"""


def inputData():
    """
    Asks por the information needed
    """
    data = {}
    
   
    # ASK FOR  OCTET's 
    for i in range(1,5):
        while True:
            try:
                octet = int(input(f"Number for octet {i} (range 0 - 254) (999 to quit): "))
            except:
                print("Error: Invalid Data")
                continue
        
            if octet == 999:
                exit(0)
            if octet >= 0 and octet <= 254:
                data[f'octect{i}'] = octet
                break
            else:
                print(f"Error: range must be 0 - 254 (999 to quit)")

    # ASK FOR CIDR
    while True:
        try:
            cidr = int(input(f"Inpt CIDR (as integer from 1 to 32): (999 to quit): "))
        except:
            print("Error: Invalid Data")
            continue
        
        if cidr == 999:
            exit(0)
        if cidr >= 1 and cidr <= 32:
            data['cidr'] = cidr
            break
        else:
            print(f"Error: range must be 1 - 32 (999 to quit)")
        
    return data


def place2bin(num: int) -> int:
    octect = num // 8
    bit = num   % 8
    n = 32 - num 
    s = '1'+ ('0' * n)
    return int(s,2)  # 2 is for base 2 (binary)




def ip_calculator(dat: dict) -> str:
    ip = str(dat['octect1'])+'.'+str(dat['octect2'])+'.'+str(dat['octect3'])+'.'+str(dat['octect4'])
    x = place2bin(dat['cidr'])
    
    # mask = 254 - dat['devices'] 
    # binary = bin(mask).replace("0b", "")
    # count = binary.count('1')
    # ip +='0/'+str(CLASSES[dat['class']][2]+count)
    # ip +=' or mask: '
    # ip += ('255.'*CLASSES[dat['class']][3])
    # ip += ('0.'*(3-CLASSES[dat['class']][3]))
    # ip += str(mask)
    return x

def main():
    dat = inputData()
    ip = ip_calculator(dat)
    print(ip)


if __name__ == "__main__":
    main()
