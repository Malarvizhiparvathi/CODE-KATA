a = raw_input("")
try:
    i = float(a)
    print("yes")
except (ValueError, TypeError):
    print('no')
