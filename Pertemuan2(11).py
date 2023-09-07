def getBagi(myList):
    bagi = 1
    for i in myList:
        bagi/=i
    print (bagi)

getBagi([1,2,3,4])
getBagi([7,3,5,11,8,10])
getBagi([-2,4,5,-7,9,4,5])