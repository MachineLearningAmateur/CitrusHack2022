from scan import Scan
from add_classmate import Add_Classmate

add = Add_Classmate()
add.start()

while True:
    q = input("Would you like to add another student? (y/n): ")
    if (q == 'n'):
        break
    elif (q == 'y'):
        add.start()
    else:
        continue

check = Scan()
check.start()