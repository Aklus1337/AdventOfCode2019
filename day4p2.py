input = 0


def dups(a):
    npairs = 0
    apair = 0
    for x in range(0,5):
        if a[x] == a[x+1]:
            npairs += 1
            apair.append(a[x+1])
    if npairs > 0:
        if len(set(apair)) == 1: # there are 2 types of pairs
            return True
    return False

a=[1,2,3,4,4,4]

print(dups(a))

'''
def dups(a):
    npairs = 0
    apair = 0
    for x in range(0,5):
        if a[x] == a[x+1]:
            npairs += 1
            apair.append(a[x+1])
    if npairs > 0:
        if len(set(apair)) == 1: # there are 2 types of pairs
            return True
    return False



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


'''
