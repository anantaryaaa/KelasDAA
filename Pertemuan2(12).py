# fungsi pembagian

def getavg(myList):
    rata2 = 0
    for i in myList:
        rata2 += i
        hasil = rata2/len(myList)
    print (hasil)

getavg([1,2,3,4])
getavg([7,3,5,11,8,10])
getavg([-2,4,5,-7,9,4,5])