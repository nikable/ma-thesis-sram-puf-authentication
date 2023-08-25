## required imports
import os
from scipy.spatial.distance import hamming

## load initial response
with open("/home/stark/Arduino/values/arduino_uno_reading_1.txt") as file:
    lines = [line.strip() for line in file]
    ## split memory response for each byte
    split = [words for segments in lines for words in segments.split()] 

## convering response into binary list
binary_list = []
## integer list for verifying results again (results are same)
#int_list = []
scale = 16
for i in split:
    binary_list.append(bin(int(i, scale))[2:].zfill(8))
    #int_list.append(int(i, 16))
print("Received PUF response 1 lenth: " + str(len(binary_list)) + "bytes")
#print(len(int_list))

## load another response
with open("/home/stark/Arduino/values/arduino_uno_reading_2.txt") as file:
    lines2 = [line.strip() for line in file]
    split2 = [words2 for segments2 in lines2 for words2 in segments2.split()]

## convering response into binary list
binary_list2 =[]
## integer list for verifying results again (results are same)
#int_list2 = []
for i in split2:
    binary_list2.append(bin(int(i, scale))[2:].zfill(8))
    #int_list2.append(int(i, 16))

#print(len(binary_list2))
print("Received PUF response 2 lenth: " + str (len(binary_list2)) + "bytes")


## calculate fractional hamming distance
distance = hamming(binary_list, binary_list2)

## verifyig again with the integer distance
#distance = hamming(int_list, int_list2) * len(int_list2)
print("Fractional hamming distance between 2 PUF responses: " + str(distance))




