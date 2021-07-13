print(2**3)

def raise_to(base, power):
    result = 1
    for i in range(power):
        result = result*base
    return result

print(raise_to(3,2))
print(raise_to(5,4))

