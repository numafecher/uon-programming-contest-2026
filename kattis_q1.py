a_str = input()

# for i in a_str:
#     test = ord(chr(a_str))
#     print(test)

new_str = []

a_split = [char for char in a_str]
for i in a_split:
    if (ord(i) <= 90 and ord(i) >= 65):
        # upper to lower
        lower_char = ord(i) + 32
        # print(chr(lower_char))
        new_str.append(chr(lower_char))
    elif (ord(i) <= 122 and ord(i) >= 97):
        # lower to upper
        lower_char = ord(i) - 32
        # print(chr(lower_char))
        new_str.append(chr(lower_char))
    else:
        new_str.append(i)


output = "".join(new_str)
print(output)