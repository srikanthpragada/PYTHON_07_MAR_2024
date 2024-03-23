def extract_digits(s):
    digits = ''
    for c in s:
        if c.isdigit():
            digits += c

    return digits


#print(extract_digits('a123'), extract_digits('ab7c5'))

data = ['AB123', '45XY', 'PQR', '345D']

for n in map(extract_digits, data):
    print(n)
