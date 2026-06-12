import random
from random import choice

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
chose= choice(friends)
print(chose)
random.randint(0,4)
if random.randint(0,4) == 0:
    print("alice")
elif random.randint(0,4) == 1:
    print("bob")
elif random.randint(0,4) == 2:
    print("charlie")
elif random.randint(0,4) == 3:
    print("david")
else:
    print("emanuel")