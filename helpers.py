
def generate_short_url(val):
    val = list(val)
    print(val)
    val = list(map(lambda x: chr(ord(x)-1), val))
    return ''.join(val)