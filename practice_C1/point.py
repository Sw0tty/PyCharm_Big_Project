class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot: {self.x, self.y}'


p1 = Dot(1, 2)
p2 = Dot(1, 2)
print(p1 == p2)
print(str(p1))
print(p2)


class IPAddressWithoutSTR:
    def __init__(self, ip):
        self.ip = ip


ip1 = IPAddressWithoutSTR('10.1.1.1')

print(ip1)


class IPAddressWithSTR:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return f"IpAddress {self.ip}"


ip1 = IPAddressWithSTR('10.1.1.1')

print(ip1)
