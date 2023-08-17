## required imports
import os
import csv
import pandas as pd
import numpy as np
from scipy.spatial.distance import hamming


## variable declaration
scale = 16
binary_list  = []
binary_list2 = []
## for csv
init_response_list = []
second_response_list = []
init_response_size = []
second_response_size = []
intra_hd_list = []

## response folder location
folder_path = "/home/stark/thesis/sram/arduino/"  
## list of files in the folder
file_names = os.listdir(folder_path)
# sort file names
file_names.sort()


## initial response to load
init_file_name = "response-49.txt"
init_file_path = os.path.join(folder_path, init_file_name)
init_response  = os.path.splitext(init_file_name)[0]


## load initial response 
with open(init_file_path, 'r') as file:
    lines = [line.strip() for line in file]
    ## split memory response for each byte
    split = [words for segments in lines for words in segments.split()]   

## integer list for verifying results again (results are same)
#int_list = []
for i in split:
    binary_list.append(bin(int(i, scale))[2:].zfill(8))
    #int_list.append(int(i, 16))
print("Received PUF response 1 lenth: " + str(len(binary_list)) + "bytes")

## iterating over multiple files
for file_to_compare in file_names:
    if file_to_compare != init_file_name:
        ## load another response
        second_file_path = os.path.join(folder_path, file_to_compare)
        with open(second_file_path, 'r') as second_file:
            lines2 = [line.strip() for line in second_file]
            split2 = [words2 for segments2 in lines2 for words2 in segments2.split()]

        ## convering response into binary list
        ## integer list for verifying results again (results are same)
        #int_list2 = []
        for i in split2:
            binary_list2.append(bin(int(i, scale))[2:].zfill(8))
            #int_list2.append(int(i, 16))

        #print(len(binary_list2))
        print("Received PUF response 2 lenth: " + str (len(binary_list2)) + "bytes")

        ## calculate fractional hamming distance
        distance = hamming(binary_list, binary_list2)

        ## verifyig again with the integer distance (same result)
        #distance = hamming(int_list, int_list2) * len(int_list2)
        print("Fractional hamming distance between 2 PUF responses: " + str(distance))

        ## csv writing preparation
        init_response_list.append(init_response)
        init_response_size.append(str (len(binary_list)))
        second_response_list.append(os.path.splitext(file_to_compare)[0])
        second_response_size.append(str (len(binary_list2)))
        intra_hd_list.append(distance)
        

        ## flush second list
        binary_list2.clear() 


# dictionary of lists
dict = {'Response-one': init_response_list, 
        'Response-one-size (bytes)': init_response_size, 
        'Response-two': second_response_list,
        'Response-two-size (bytes)': second_response_size,
        'Intra-Hamming Distance': intra_hd_list
        }

## convert into data frame     
df = pd.DataFrame(dict)

## arrange index to write at the begining of the data frame
#df.index = np.arange(1, len(df) + 1)
df.index = df.index + 1
     
# saving the dataframe
df.to_csv('/home/stark/thesis/sram/csv/test7.csv')