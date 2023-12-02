import os

def RunSolution():
    """
    Executes and displays the solutions for Day 2.

    This function runs two separate functions: SilverSolution and GoldSolution,
    which compute the solutions for the silver and gold stars of Day 2, respectively.
    It then prints out these solutions.
    """
    print("Running Day 2 Solution...")
    # Getting the file contents.
    processedFile = FileImport()
    # Get the silver star solution.
    silver = SilverSolution(processedFile[0])
    # Get the gold star solution.
    golden = GoldSolution(processedFile[1])
    print(f"The Silver Solution to Day 2 -> {silver}")
    print(f"The Golden Solution to Day 2 -> {golden}")

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
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_2", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_2\silver.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            processedSilver = {}
            i = 1
            for line in daySpec:
                # Cleaning up the string. This is likely pretty inefficient but running low on time today.
                # TODO: Make the string cleanup more efficient (regex?)
                line = line.replace(" ", "")
                line = line.replace("Game", "")
                line = line.replace("blue", "b")
                line = line.replace("red", "r")
                line = line.replace("green", "g")
                # Storing the line, and interating.
                processedSilver[i] = line
                i = i + 1

    except:
        raise FileNotFoundError(f"Day 2's silver import file cannot be found!")
    # Getting the gold solution.
    try:
        scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_2", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_2\gold.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            #TODO: Process the file import here depending on what comes.
            processedGold = 0
    except:
        raise FileNotFoundError(f"Day 2's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def SilverSolution(solutionData):
    """
    Processes the provided solution data to find the silver solution.

    This function takes in data, typically from a file or a similar source, processes it to figure out the solution, 
    and then returns that solution. The current implementation is a placeholder and indicates if the day's solution 
    has not been completed yet.

    Args:
        solutionData (type): The data that needs to be processed to find the solution. 
                             The exact type of this data depends on what the solution requires.

    Returns:
        str: The results of the current day.
    """
    idTotals = 0
    for game in solutionData:
        # First we get the information off of the current game.
        currentGame = solutionData[game]
        currentGame = currentGame.split(":")
        # Storing the ID, ready to process the rest of the game.
        currentID = int(currentGame[0])
        currentGame = currentGame[1]
        # Then getting all the rounds.
        currentGameRounds = currentGame.split(";")
        for round in currentGameRounds:
            # Looping through every round, and getting each "play".
            currentRoundDraws = round.split(",")
            for draw in currentRoundDraws:
                # Looping through every draw, seeing if it breaks the rules.
                if ("r" in draw): # Red
                    draw = int(draw.replace("r", ""))
                    if (draw > 12):
                        currentID = 0
                elif ("g" in draw): # Green
                    draw = int(draw.replace("g", ""))
                    if (draw > 13):
                        currentID = 0
                else: # Blue
                    draw = int(draw.replace("b", ""))
                    if (draw > 14):
                        currentID = 0
        # Add idTotals
        idTotals = idTotals + currentID

    return idTotals

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