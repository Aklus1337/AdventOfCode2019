input = 0

def dups(a):
    npairs = 0
    for x in range(0,5):
        if a[x] == a[x+1]:
            npairs += 1
        else:
            if npairs == 1:
                return True
            npairs = 0
    return npairs == 1

def find_dec(a):
    for d in range(0, 5):
        if re[d + 1] < re[d]:
            return False
    return True

for i in range(136818, 685979):
    re = [int(x) for x in str(i)]
    if dups(re) and find_dec(re):
        input += 1

print(input)
