# This script is used to clean and filter the data from the statments from BMO 

# To filter , the statemnts must always be of the same type

import pandas
import numpy


def main():

    filePath = input(""" Please provide the path of the file.
          Please remember that a new csv with a same file name and a NEW prefex """)
    
    """
    with open(filePath + '.csv' , "r+") as sourceFileOpen:
        eachLines = sourceFileOpen.readlines()


        sourceFileOpen.seek(0)
        # truncate the file
        sourceFileOpen.truncate()

        # start writing lines except the first line
        # lines[1:] from line 2 to last line
        sourceFileOpen.writelines(eachLines[1:])   

    """
    """
    with open(filePath + 'Fixed' + '.csv' , "w"):

        print("A")
    """

    

    sourceDataframe = pandas.read_csv(filePath+'.csv')

    newDataframe = []


    print(df.head(10))


main()


