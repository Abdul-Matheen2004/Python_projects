def ins():
    inp = input ("Enter your binary: ")
    order = []
    for n in inp:
        if int(n) == 0 or int(n) == 1:
            order.append(n)
        else:
            print ("Please type a binary")
            break
    return order
def culc(order):
    result = 0
    order[::-1]
    for n in range(len(order)):
        if order[n] == '1':
            result += 2**n
        else:
            continue
    print (result)
culc(ins())