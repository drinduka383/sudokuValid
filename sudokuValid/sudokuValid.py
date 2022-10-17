import pandas as pd

files = ["basicGrid","basicGrid2","columnError","rowError","outOfRangeError","outOfRangeError2","rubbishError","subGridError","sumValidationError"]
file = None

while True:
    file = input("basicGrid, basicGrid2, columnError, rowError, outOfRangeError, outOfRangeError2, rubbishError, subGridError, sumValidationError.\nPlease write the name of the csv file you want to check. (No extension): ")
    if file not in files:
        print(f"\nNo file named '{file}' found. Please try again.\n")
    else: 
        break 
    
df = pd.read_csv(f"Test Cases\{file}" + ".csv", header=None)
sudoku = pd.array(data=df,dtype=int)

def rreshti(sdk, row):             # checks if specific row is valid

    setRreshti = set()
 
    for i in range(0, 9):
        setRreshti.add(sdk[row][i]) # storing values in set to be checked

    if len(setRreshti) == 9: 
        if sum(setRreshti) == 45:
            return True             # if its valid, return True 
        
    return False                    # otherwise, return False

def kolona(sdk, col):               # checks if specific column is valid with the same method

    setKolona = set()
 
    for i in range(0, 9):
        setKolona.add(sdk[i][col])
    
    if len(setKolona) == 9:
        if sum(setKolona) == 45:
            return True
        
    return False

def kutia(sdk, row, col):          # checks if a 3x3 area is valid the same way
 
    setKutia = set()
 
    for i in range(0, 3):
        for j in range(0, 3):
            setKutia.add(sdk[i + row][j + col])
            
    if len(setKutia) == 9:
        if sum(setKutia) == 45:
            return True

    return False

def fullSudoku(sdk):    # combines all 3 functions!
    
    for i in range(0, 9):
        for j in range (0, 9):
            
            if rreshti(sdk, i) == False or kolona(sdk, j) == False or kutia(sdk, i - i % 3, j - j % 3) == False:
                return False
    return True

if fullSudoku(sudoku) == True:
    print (True)
else:
    print (False)