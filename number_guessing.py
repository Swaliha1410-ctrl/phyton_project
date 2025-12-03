#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MY PC
#
# Created:     03-12-2025
# Copyright:   (c) MY PC 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#no. gessing game
import random
ran_num=random.randint(1,100)
while True:
    try:
        num=int(input('ENTER ANY NUMBER:-'))
        if num<ran_num:
            print('To low!!')
        elif num>ran_num:
            print('To high!')
        elif num==ran_num:
            print('congratulations!! you got right one')
            break
    except :
        print('Enter valid digits only!!')