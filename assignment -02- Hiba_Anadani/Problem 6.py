def checkIP(ipaddress):
    octets = ipaddress.split('.')
    if len(octets) != 4:
        return False
    for i in octets:
        value = int(i)
        if value < 0 or value > 255:
            return False

        if i[0] == '0' and len(i) > 1:
            return False
    return True

IPAddress = input("Input: ")
print("Output:", checkIP(IPAddress))