#mini project  using random module in python

import random
name = random.randrange(1,100)
show = int (input("enter the number:"))
if name>show:
    print("this is randome name:",name)
elif show<name:
    print("try again show:",show)
else:
    print("congratulation you are winner")
