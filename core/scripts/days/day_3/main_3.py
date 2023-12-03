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
            # Saving the input as a simple 2D array.
            processedSilver = []
            for line in daySpec:
                currentLine = []
                for char in line:
                    if (char != "\n"): # Ignore endline chars.
                      currentLine.append(char)
                processedSilver.append(currentLine)
    except:
        raise FileNotFoundError(f"Day 3's silver import file cannot be found!")
    # Getting the gold solution.
    try:
        scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_3", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_3\gold.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            # Saving the input as a simple 2D array.
            processedGold = []
            for line in daySpec:
                currentLine = []
                for char in line:
                    currentLine.append(char)
                processedGold.append(currentLine)
    except:
        raise FileNotFoundError(f"Day 3's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def SilverSolution(solutionData):
    # Treat the schematic as a 2D array: loop through, until a number is found, and see if that number is true. 
    # Then check the right index to see if there's another number.
    enginePartSum = 0
    print(f"Y TOTAL {len(solutionData)}. X TOTAL {len(solutionData[0])}")
    for y in range (0, len(solutionData)):
        for x in range (0, len(solutionData[y])-1):
            isValid = TestForSymbols(solutionData, x, y) # Testing for symbols
            # If it is valid -> then check for number next to it (check if x+1 is .)
            # If there is no number, then if valid, add to engine part sum.
            print(f"Current symbol: {solutionData[y][x]} -> {isValid}")
    return enginePartSum

def TestForSymbols(solutionData, x, y):
    # This is incredibly in(if)ficient.
    symbols = ["#", "*", "/", "%", "=", "@", "$", "+", "-"]
    if ((y == 0) and (x == 0)):
        # If 0,0 -> Check east, south-east and south.
        if(solutionData[y][x+1] in symbols): # East
            return True
        elif(solutionData[y+1][x+1] in symbols): # South-east
            return True
        elif(solutionData[y+1][x] in symbols): # South
            return True
    elif ((y==0) and (x == len(solutionData[y])-1)):
        # If x..n,y -> Check west, south-west and south.
        if(solutionData[y][x-1] in symbols): # West
            return True
        elif(solutionData[y+1][x-1] in symbols): # South-west
            return True
        elif(solutionData[y+1][x] in symbols): # South
            return True
    elif ((y == len(solutionData)-1) and (x == 0)):
        # If x,y..n -> Check north, north-east, east.
        if (solutionData[y-1][x] in symbols): # North
            return True
        elif (solutionData[y-1][x+1] in symbols): # North-east
            return True
        elif (solutionData[y][x+1] in symbols): # East
            return True
    elif((y == len(solutionData)-1) and (x == len(solutionData[y])-1)):
        # If x..n,y..n -> Check north, north-west, west.
        if (solutionData[y-1][x] in symbols): # North
            return True
        elif (solutionData[y-1][x-1] in symbols): # North-west
            return True
        elif (solutionData[y][x-1] in symbols): # West
            return True
    elif((y == 0)):
        # If x,0 -> west, south-west, south, south-east, east.
        if (solutionData[y][x-1] in symbols): # West
            return True
        elif(solutionData[y+1][x-1] in symbols): # South-west
            return True
        elif(solutionData[y+1][x] in symbols): # South
            return True
        elif(solutionData[y][x+1] in symbols): # East
            return True
        elif(solutionData[y+1][x+1] in symbols): # South-east
            return True
    elif((y == len(solutionData)-1)):
        # If x,y..n -> west, north-west, north, north-east, east.
        if(solutionData[y][x-1] in symbols): # West
            return True
        elif (solutionData[y-1][x-1] in symbols): # North-west
            return True
        elif (solutionData[y-1][x] in symbols): # North
            return True
        elif (solutionData[y-1][x+1] in symbols): # North-east
            return True
        elif (solutionData[y][x+1] in symbols): # East
            return True
    elif((x == 0)):
        # If 0,y -> north, north-east, east, south-east, south.
        if (solutionData[y-1][x] in symbols): # North
            return True
        elif (solutionData[y-1][x+1] in symbols): # North-east
            return True
        elif (solutionData[y][x+1] in symbols): # East
            return True
        elif(solutionData[y+1][x+1] in symbols): # South-east
            return True
        elif(solutionData[y+1][x] in symbols): # South
            return True
    elif((x == len(solutionData[y])-1)):
        # If x..n,y -> north, north-west, west, south-west, south.
        if (solutionData[y-1][x] in symbols): # North
            return True
        elif (solutionData[y-1][x-1] in symbols): # North-west
            return True
        elif (solutionData[y][x-1] in symbols): # West
            return True
        elif(solutionData[y+1][x-1] in symbols): # South-west
            return True
        elif(solutionData[y+1][x] in symbols): # South
            return True
    else:
        # Else, it's not going to be an edge-case (bdmtshh), so just scan all around.
        # If x!=0,y!=0 -> north, north-east, east, south-east, south, south-west, west, north-west.
        if (solutionData[y-1][x] in symbols): # North
            return True
        elif (solutionData[y-1][x+1] in symbols): # North-east
            return True
        elif (solutionData[y][x+1] in symbols): # East
            return True
        elif(solutionData[y+1][x+1] in symbols): # South-east
            return True
        elif(solutionData[y+1][x] in symbols): # South
            return True
        elif(solutionData[y+1][x-1] in symbols): # South-west
            return True
        elif (solutionData[y][x-1] in symbols): # West
            return True
        elif (solutionData[y-1][x-1] in symbols): # North-west
            return True
    


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