n = int(input("Enter a Number that to be checked : "))
temp = n
rev = 0
while (n >0):
    dig = n%10
    rev = rev * 10 + dig
    n = n // 10
if (temp == rev):
    print ("True")
else:
    print ("False")
