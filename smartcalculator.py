responses = [
    "Welcome to smart calculator",
    "Calculator Build by Amit",
    "Thanks for using",
    "Sorry, this is beyond by ability",
]


def extract_numbers_from_text(text):
    l = []
    for t in text.split(" "):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    """
    Multiplication of two Numbers
    @param a : First integer
    @param b : Second Integer
    """
    return a * b


def division(a, b):
    return a / b


def end():
    print(responses[2])
    input("Press enter key to exit")
    exit()


def myname():
    print(responses[1])


def sorry():
    print(responses[3])


operations = {
    "PLUS": add,
    "ADD": add,
    "ADDITION": add,
    "SUM": add,
    "MINUS": sub,
    "SUBSTRACTION": sub,
    "DIFFERENCE": sub,
    "PRODUCT": multiply,
    "MULTIPLICATION": multiply,
    "MULTIPLY": multiply,
    "DIVIDE": division,
    "DIVISION": division,
    "LCM": lcm,
    "L.C.M": lcm,
    "HCF": hcf,
    "H.C.f": hcf,
}


commands = {"NAME": myname, "END": end, "EXIT": end, "CLOSED": end}
