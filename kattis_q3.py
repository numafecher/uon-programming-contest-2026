n = int(input())

# print(bin(n))
# print(int(bin(n)))

og_bin = bin(n)
# print(og_bin)

og_bin_split = [char for char in og_bin]
# print(og_bin_split)

og_bin_split.pop(0)
og_bin_split.pop(0)
# print(og_bin_split)

new_og_bin = "".join(og_bin_split)

n = int(''.join(map(str, reversed(new_og_bin))), 2)

print(n)