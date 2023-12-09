def numbers(a,b,c):
    if a >0 and b >0:
        return True
    elif a >0 and c > 0:
        return True
    elif b > 0 and c > 0:
        return True
    elif b > 0 and a > 0:
        return True
    else:
        return False
print (numbers(3,-5,-6))