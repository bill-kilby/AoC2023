import os

def RunSolution():
    """
    Executes and displays the solutions for Day 3.

    This function runs two separate functions: SilverSolution and GoldSolution,
    which compute the solutions for the silver and gold stars of Day 3, respectively.
    It then prints out these solutions.
    """
    print("Running Day 3 Solution...")
    # Getting the file contents.
    processedFile = FileImport()
    print(processedFile)
    # Get the silver star solution.
    silver = SilverSolution(processedFile[0])
    # Get the gold star solution.
    golden = GoldSolution(processedFile[1])
    print(f"The Silver Solution to Day 3 -> {silver}")
    print(f"The Golden Solution to Day 3 -> {golden}")

def FileImport():
    """
    Imports data from specific silver and gold solution files.

    This function locates and reads data from two separate text files, named 'silver.txt' and 'gold.txt'. 
    It first attempts to import data from the 'silver.txt' file, processes it, and then does the same for the 'gold.txt' file.

    Returns:
        tuple: A tuple containing two elements. The first element is the processed data from 'silver.txt',
               and the second element is the processed data from 'gold.txt'.

    Raises:
        FileNotFoundError: If either 'silver.txt' or 'gold.txt' cannot be found in the expected directory.
    """
    try:
        scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_3", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_3\silver.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            # Saving the input as a simple 2D array with a border of Bs.
            processedSilver = []
            firstLine = True
            for line in daySpec:
                if (firstLine == True):
                    lineLength = len(line)
                    processedSilver.append("B"*(lineLength + 2))
                    firstLine = False
                currentLine = ["B"]
                for char in line:
                    if (char != "\n"): # Ignore endline chars.
                      currentLine.append(char)
                currentLine.append("B")
                processedSilver.append(currentLine)
            processedSilver.append("B"*(lineLength + 2))
    except:
        raise FileNotFoundError(f"Day 3's silver import file cannot be found!")
    # Getting the gold solution.
    try:
        scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_3", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_3\gold.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            # Saving the input as a simple 2D array with a border of Bs. Identical to silver today.
            processedGold = []
            firstLine = True
            for line in daySpec:
                if (firstLine == True):
                    lineLength = len(line)
                    processedGold.append("B"*(lineLength + 2))
                    firstLine = False
                currentLine = ["B"]
                for char in line:
                    if (char != "\n"): # Ignore endline chars.
                      currentLine.append(char)
                currentLine.append("B")
                processedGold.append(currentLine)
            processedGold.append("B"*(lineLength + 2))
    except:
        raise FileNotFoundError(f"Day 3's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def CheckForSymbol(data, line, char):
    # Check around the character for special symbols.
    symbols = ["/","*","@","%","$","+","-","=","&","#"]
    if data[line-1][char] in symbols:
        return True # North
    elif data[line-1][char+1] in symbols:
        return True # North-east
    elif data[line][char+1] in symbols:
        return True # East
    elif data[line+1][char+1] in symbols:
        return True # South-east
    elif data[line+1][char] in symbols:
        return True # South
    elif data[line+1][char-1] in symbols:
        return True # South-west
    elif data[line][char-1] in symbols:
        return True # West
    elif data[line-1][char-1] in symbols:
        return True # North-west
    else:
        return False # Else no symbol was found
    


def SilverSolution(solutionData):
    # Set up variables
    totalNumber = 0
    currentNumber = ""
    valid = False
    # Loop through every line.
    for line in range(1, len(solutionData)):
        for character in range(1, len(solutionData[line])):
            # If the current character is a number.
            if (solutionData[line][character].isdigit()):
                # Check if it is sorrounded by stuff.
                if (CheckForSymbol(solutionData, line, character) == True):
                    # If it is, set valid to true, and add it on.
                    valid = True
                elif ((CheckForSymbol(solutionData, line, character) == False) and valid == False):
                    # If it isn't keep valid false.
                    valid = False
                # Either way, add it onto the total number
                currentNumber = currentNumber + solutionData[line][character]
            else:
                # If it is not a digit, check if it was valid, and add on if so.
                if (valid == True):
                    print(f"{currentNumber} was valid. Adding onto total.")
                    totalNumber = totalNumber + int(currentNumber)
                    print(f"The total is now {totalNumber}.\n")
                # Then reset variables.
                currentNumber = ""
                valid = False
    return totalNumber

def GetFullNumber(data, line, char):
    # Setting up pointers for checking if the number is continuing.
    leftPointer = -1
    rightPointer = 1
    # Variable for storing the total number found, starting with the number selected.
    totalNumber = ""+data[line][char]
    # Loop through while left pointer is at a digit.
    while (data[line][char + leftPointer].isdigit()):
        # Add number to beginning of string
        totalNumber = data[line][char + leftPointer] + totalNumber
        # Increment pointer by 1.
        leftPointer = leftPointer - 1
    # Loop through while right pointer is at a digit.
    while (data[line][char + rightPointer].isdigit()):
        # Add number to end of string.
        totalNumber = totalNumber + data[line][char + rightPointer]
        # Increment pointer by 1
        rightPointer = rightPointer + 1
    # Return the total number as an int
    return int(totalNumber)


def GetGearRatio(data, line, char):
    # Setting up a list for all the variables sorrounding a gear
    totalNumbers = []
    # Checking top line.
    left, middle, right = 0,0,0
    if (data[line-1][char-1].isdigit()): # North west
        left = GetFullNumber(data, line-1, char-1)
    if (data[line-1][char].isdigit()): # North
        middle = GetFullNumber(data, line-1, char)
    if (data[line-1][char+1].isdigit()): # North east
        right = GetFullNumber (data, line-1, char+1)
    # If middle is a number, then theres only 1 number
    if (middle != 0):
        totalNumbers.append(middle)
    else:
        # Else, left and right are numbers.
        totalNumbers.append(left)
        totalNumbers.append(right)
        
    # Checking middle line. These will never overlap so immediately add to list.
    if (data[line][char-1].isdigit()): # West
        totalNumbers.append(GetFullNumber(data, line, char-1))
    if (data[line][char+1].isdigit()):
        totalNumbers.append(GetFullNumber(data, line, char+1))
    
    # Checking bottom line.
    left, middle, right = 0,0,0
    if (data[line+1][char-1].isdigit()): # South west.
        left = GetFullNumber(data, line+1, char-1)
    if (data[line+1][char].isdigit()): # South
        middle = GetFullNumber(data, line+1, char)
    if (data[line+1][char+1].isdigit()): # South east
        right = GetFullNumber(data, line+1, char+1)
    # Same thing, if middle is a number, theres only 1 number.
    if (middle != 0):
        totalNumbers.append(middle)
    else:
        # Else, left and right are numbers.
        totalNumbers.append(left)
        totalNumbers.append(right)

    # Clean up total numbers by removing the null numbers (0).
    for zero in range(0, totalNumbers.count(0)):
        totalNumbers.remove(0)

    # Now all the numbers have been collected, see if there are more than 2.
    if (len(totalNumbers) == 2):
        print(f"The gear is valid -> Returning {totalNumbers[0] * totalNumbers[1]}.\n")
        # If so, return multiplication.
        return (totalNumbers[0] * totalNumbers[1])
    # Else return 0 as it is invalid.
    print("The gear is invalid -> Returning 0.\n")
    return 0

def GoldSolution(solutionData):
    print(" Running gold solution")
    totalNumber = 0
    # Loop through all lines.
    for line in range(1, len(solutionData)-1):
        # Loop through all characters in line
        for character in range (1, len(solutionData[line])-1):
            # If it is a gear...
            if (solutionData[line][character] == "*"):
                print(f"Gear (*) found at ({character},{line}).")
                # Get the gear ratio of the gear.
                gearRatio = GetGearRatio(solutionData, line, character)
                # Add it onto the total.
                totalNumber = totalNumber + gearRatio
    return totalNumber

