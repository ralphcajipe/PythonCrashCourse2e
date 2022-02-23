# Avoiding Infinite Loops
x = 1
while x <= 5:
    print(x)
    x += 1

##
# This loop runs forever!
# x = 1
# while x <= 5:
#    print(x)
#
# Output:
# 1
# 1
# 1
# ... infinity
##