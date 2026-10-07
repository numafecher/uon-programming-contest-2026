x = input()
s = input()

s = [char for char in s]

n = int(x.split()[0]) #length of bridge
k = int(x.split()[1]) # num kids

kids_pass = k
choice = "L"
first_kid = 1
fall_flag = 0

while s and kids_pass > 0:
    # First kid first try
        if first_kid == 1:
            
            if "L" != s[0]:
                # print("splash")
                kids_pass = kids_pass - 1
                choice = "L"
                s.pop(0)
            else:
                # print("safe")
                choice = "R"
                s.pop(0)
            first_kid = 0
        
        # Not first kid first try
        else:
            if choice != s[0]:
                # print("splash")
                kids_pass = kids_pass - 1
                # choice doesn't change
            else:
                # print("safe")

                # switch choice
                if choice == "R":
                    choice = "L"
                else:
                    choice = "R"
            s.pop(0)

print(kids_pass)