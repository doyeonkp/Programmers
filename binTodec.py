# binary to decimal
# int(binary, 2) -> 2 is base => it can convert to decimal
# but if you want to make this logic program
# follow the below
binary = raw_input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print decimal
