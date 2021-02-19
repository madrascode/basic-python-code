def loop_of_hcf(x, y):  # highest common divisior that pefectly divides both numbers
    # hcf can only be equal to or less than smaller number for that we have consider the smaller number.
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i)== 0 and (y % i) == 0:
            hcf = i
    return hcf


# This method of loop is not that efficient for hcf

def eucladian_hcf(xx,yy):
    while(yy):
        xx, yy = yy, xx%yy  # in this algorithm we divide the greater number by smaller number and takes the remainder then we divide the smaller number by reaminder ...this is repeated until we get 0
    return xx

# print(loop_of_hcf(54, 24)) 6
# print(eucladian_hcf(54, 24))