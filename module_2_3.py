my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Fan = 0
while Fan <  len(my_list):
    if my_list[Fan] < 0:
        break
    elif my_list[Fan] == 0:
        Fan += 1
        continue
    else:
        print(my_list[Fan])
    Fan += 1

