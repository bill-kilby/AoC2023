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
    print(f"\nThe Silver Solution to Day 2 -> {silver}")
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
            # Identical - today, the puzzle input has not changed.
            processedGold = {}
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
                processedGold[i] = line
                i = i + 1
    except:
        raise FileNotFoundError(f"Day 2's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def SilverSolution(solutionData):
    """
    Calculate the total of valid game IDs based on specific play rules.

    Processes a dictionary of game data where each key is a game identifier and the value is a string 
    representing the sequence of plays. Each play is categorized by color (red 'r', green 'g', or blue 'b') 
    followed by a number. Validates each play against color-specific rules:
    - Red plays ('r') must have a number <= 12
    - Green plays ('g') must have a number <= 13
    - Blue plays (default) must have a number <= 14
    Invalid plays result in the game's ID being set to 0. The function sums and returns the total of all valid game IDs.

    :param solutionData: A dictionary with game identifiers as keys and strings of game plays as values.
    :type solutionData: dict
    :returns: The sum of valid game IDs after applying the play validation rules.
    :rtype: int
    """
    print("\nSILVER SOLUTION OUTPUTS: ")
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
                    try:
                        draw = int(draw.replace("r", ""))
                        if (draw > 12):
                            currentID = 0
                    except:
                        print("No number can be found!")
                elif ("g" in draw): # Green
                    try:
                        draw = int(draw.replace("g", ""))
                        if (draw > 13):
                            currentID = 0
                    except:
                        print("No number can be found!")
                else: # Blue
                    try:
                        draw = int(draw.replace("b", ""))
                        if (draw > 14):
                            currentID = 0
                    except:
                        print("No number can be found!")
        # Add idTotals
        idTotals = idTotals + currentID
        print(f"Game {currentID}: {solutionData[game].strip()} -> Total ID Sum: {idTotals}")
    return idTotals

def GoldSolution(solutionData):
    """
    Calculate the total "power" of all games based on the highest numbers drawn in each color category.

    This function processes a dictionary of game data where each key is a game identifier and the value is a string 
    representing the sequence of plays in the game. Each play is categorized by color (red 'r', green 'g', or blue 'b') 
    followed by a number. The function determines the highest number drawn for each color in each game and calculates 
    the game's "power" as the product of these highest numbers across the three color categories. It sums and returns 
    the total "power" for all games.

    :param solutionData: A dictionary with game identifiers as keys and strings of game plays as values.
    :type solutionData: dict
    :returns: The total "power" calculated across all games.
    :rtype: int
    """
    print("\nGOLD SOLUTION OUTPUTS: ")
    gamePowerTotals = 0
    for game in solutionData:
        highestNumbers = [0, 0, 0] # [R, G, B]
        # First we get the information off of the current game.
        currentGame = solutionData[game]
        currentGame = currentGame.split(":")
        # Storing the ID, ready to process the rest of the game.
        currentID = currentGame[0]
        currentGame = currentGame[1]
        # Then getting all the rounds.
        currentGameRounds = currentGame.split(";")
        for round in currentGameRounds:
            # Looping through every round, and getting each "play".
            currentRoundDraws = round.split(",")
            for draw in currentRoundDraws:
                # Looping through every draw, seeing if it is larger than the previous one.
                if ("r" in draw): # Red
                    try:
                        draw = int(draw.replace("r", ""))
                        if (draw > highestNumbers[0]):
                            highestNumbers[0] = draw
                    except:
                        print("No number can be found!")
                elif ("g" in draw): # Green
                    try:
                        draw = int(draw.replace("g", ""))
                        if (draw > highestNumbers[1]):
                            highestNumbers[1] = draw
                    except:
                        print("No number can be found!")
                else: # Blue
                    try:
                        draw = int(draw.replace("b", ""))
                        if (draw > highestNumbers[2]):
                            highestNumbers[2] = draw
                    except:
                        print("No number can be found!")
        # Calculate game power and add it on
        gamePowerTotals = gamePowerTotals + (highestNumbers[0] * highestNumbers[1] * highestNumbers[2])
        print(f"Game {currentID}: {solutionData[game].strip()} -> Power: {highestNumbers[0] * highestNumbers[1] * highestNumbers[2]} -> Total: {gamePowerTotals}") # Debug print.
    return gamePowerTotals