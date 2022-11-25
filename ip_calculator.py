"""
Determines de IPv4 CIDR Notation base on data input

"""
CLASSES = {'A':(0,127,8,1), 'B':(128,191,16,2), 'C':(192,223,24,3)}


def inputData():
    """
    Asks por the information needed
    """
    data = {}
    
    # ASK FOR CLASS NETWORK
    while True:
        clas = input("What would be de Class of the network (A,B.C) (Q to quit): ").upper()
        if clas == "Q":
            exit(0)
        if clas in "ABC" and len(clas) == 1:
            data['class'] = clas
            break
        print("Error: wrong input. Should be A,B,C or Q")
    
    # ASK FOR FIRST OCTET BASED ON CLASS
    while True:
        try:
            octet = int(input(f"Number for first octet (range {CLASSES[clas][0]} - {CLASSES[clas][1]}) (999 to quit): "))
        except:
            print("Error: Invalid Data")
            continue
        
        if octet == 999:
            exit(0)
        if octet >= CLASSES[clas][0] and octet <= CLASSES[clas][1]:
            data['octect1'] = octet
            break
        print(f"Error: range must be {CLASSES[clas][0]} - {CLASSES[clas][1]} (999 to quit)")

    # ASK FOR SECOND AND THIRD OCTET BASED ON CLASS
    for i in (2,3):
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
        print(f"Error: range must be 0 - 254 (999 to quit)")

    # ASK FOR MAX NUMBER OF DEVICES IN NETWORK
    while True:
        try:
            devices = int(input(f"Maximum Number for devices in network (range 1 - 254) (999 to quit): "))
        except:
            print("Error: Invalid Data")
            continue
        
        if devices == 999:
            exit(0)
        if devices >= 1 and devices <= 254:
            data['devices'] = devices
            break
        print(f"Error: range must be 1 - 254 (999 to quit)")
        
    return data

def ip_calculator(dat: dict) -> str:
    ip = str(dat['octect1'])+'.'+str(dat['octect2'])+'.'+str(dat['octect3'])+'.'
    mask = 254 - dat['devices'] 
    binary = bin(mask).replace("0b", "")
    count = binary.count('1')
    ip +='0/'+str(CLASSES[dat['class']][2]+count)
    ip +=' or mask: '
    ip += ('255.'*CLASSES[dat['class']][3])
    ip += ('0.'*(3-CLASSES[dat['class']][3]))
    ip += str(mask)
    return ip

def main():
    dat = inputData()
    ip = ip_calculator(dat)
    print(ip)


if __name__ == "__main__":
    main()
