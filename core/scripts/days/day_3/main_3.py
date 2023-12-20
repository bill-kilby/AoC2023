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
    silver = Silver2(processedFile[0])
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
            # Saving the input as a simple 2D array. TODO: Add a border to this.
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
    except:
        raise FileNotFoundError(f"Day 3's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def Silver2(data):
    enginePartSum = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x].isdigit():
                # Check if the current digit is adjacent to a symbol
                if TestForSymbols(data, x, y):
                    # Form the complete number starting at this digit
                    currentNumber = data[y][x]
                    offset = 1
                    while x + offset < len(data[y]) and data[y][x + offset].isdigit():
                        currentNumber += data[y][x + offset]
                        offset += 1
                    enginePartSum += int(currentNumber)
                    # Skip the rest of the digits in this number
                    x += offset - 1
    return enginePartSum

def SilverSolution(solutionData):
    # Treat the schematic as a 2D array: loop through, until a number is found, and see if that number is true. 
    # Then check the right index to see if there's another number.
    return 0

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

