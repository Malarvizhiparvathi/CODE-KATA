def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
a=raw_input("")
print(isinteger(a))
