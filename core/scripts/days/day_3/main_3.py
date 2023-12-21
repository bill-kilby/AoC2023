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
        processedGold= [1]
    except:
        raise FileNotFoundError(f"Day 3's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def CheckForSymbol(data, line, char):
    # Check around the character for special symbols.
    symbols = ["/","*","@","%","$","+","-","=","&", "#"]
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

def GoldSolution(solutionData):
    """
    Processes the provided solution data to find the golden solution.

    This function takes in data, typically from a file or a similar source, processes it to figure out the solution, 
    and then returns that solution. The current implementation is a placeholder and indicates if the day's solution 
    has not been completed yet.

    Args:
        solutionData (type): The data that needs to be processed to find the solution. 
                             The exact type of this data depends on what the solution requires.

    Returns:
        str: The results of the current day.
    """
    #TODO: Process the data, figure out the solution, and return the solution.
    print("")
    return "Day has not been completed yet!"

