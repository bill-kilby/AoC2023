import os

def RunSolution():
    """
    Executes and displays the solutions for Day 4.

    This function runs two separate functions: SilverSolution and GoldSolution,
    which compute the solutions for the silver and gold stars of Day 4, respectively.
    It then prints out these solutions.
    """
    print("Running Day 4 Solution...")
    # Getting the file contents.
    processedFile = FileImport()
    print(processedFile)
    # Get the silver star solution.
    silver = SilverSolution(processedFile[0])
    # Get the gold star solution.
    golden = GoldSolution(processedFile[1])
    print(f"The Silver Solution to Day 4 -> {silver}")
    print(f"The Golden Solution to Day 4 -> {golden}")

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
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_4", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_4\silver.txt" # Adding the file import.
        processedSilver = []
        with open(scriptDirectory) as daySpec:
            for line in daySpec:
                # For each line, seperate the part into a tuple of ([winning], [actual])
                cardData = line.split(":")[1]
                winningAndActual = cardData.split("|")
                winningNumbers = winningAndActual[0].split()
                actualNumbers = winningAndActual[1].split()
                processedSilver.append( (winningNumbers, actualNumbers))
    except:
        raise FileNotFoundError(f"Day 4's silver import file cannot be found!")
    # Getting the gold solution.
    try:
        scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_4", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_4\gold.txt" # Adding the file import.
        processedGold = []
        with open(scriptDirectory) as daySpec:
            for line in daySpec:
                # For each line, seperate the part into a tuple of ([winning], [actual]). Identical to silver.
                cardData = line.split(":")[1]
                winningAndActual = cardData.split("|")
                winningNumbers = winningAndActual[0].split()
                actualNumbers = winningAndActual[1].split()
                processedGold.append( (winningNumbers, actualNumbers))
    except:
        raise FileNotFoundError(f"Day 4's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def GetCardTotal(card):
    # This feels pretty inefficient -> surely a better way than just looping through? Potential sorting (timsort?) and then searching?
    totalWinningNumbers = 0
    # Loop through the winning cards.
    for winningNumber in card[0]:
        # Loop through the actual cards
        for actualNumber in card[1]:
            # If they won, add 1 to the total number of winnings.
            if (winningNumber == actualNumber):
                totalWinningNumbers = totalWinningNumbers + 1
    print(f"Card completed with {totalWinningNumbers} matches!")
    # Now all winning cards have been calculated, calculate total power.
    if (totalWinningNumbers != 0):
        # Set up the initial (1) number.
        totalNumber = 1
        totalWinningNumbers = totalWinningNumbers - 1
        # Loop through remaining winning numbers and loop each time. 
        for i in range (0, totalWinningNumbers):
            totalNumber = totalNumber * 2 # TODO: There is probably just a simple equation here rather than a forloop.
        return totalNumber
    return 0 # Return 0 if no winning numbers are found.

def SilverSolution(solutionData):
    #TODO: Process the data, figure out the solution, and return the solution.
    totalWinning = 0
    # Loop through every card and get the winning number.
    for card in solutionData:
        totalWinning = totalWinning + GetCardTotal(card)
    return totalWinning

def GetCardWinners(card, index):
    # Get the total amount of card winners (same code as the first part of Silver) TODO: Refactor this into its own function.
    # This feels pretty inefficient -> surely a better way than just looping through? Potential sorting (timsort?) and then searching?
    totalWinningNumbers = 0
    # Loop through the winning cards.
    for winningNumber in card[0]:
        # Loop through the actual cards
        for actualNumber in card[1]:
            # If they won, add 1 to the total number of winnings.
            if (winningNumber == actualNumber):
                totalWinningNumbers = totalWinningNumbers + 1
    print(f"Card completed with {totalWinningNumbers} matches!")
    # Now that the winners have been found, return a tuple containing (amountOfWinners, [nextCards])
    cardWinners = (totalWinningNumbers, [])
    # Add the future winners.
    for i in range(1, totalWinningNumbers+1):
        cardWinners[1].append(index+i)


def GoldSolution(solutionData):
    # Idea for this one: Solve for all of the scratchcards, save them in a dictionary.
    # Dictionary of results {CardNumber: [List of future scratch cards]}
    # Then just loop through each one iteratively like a queue.
    #
    # After all cards solved:
    # Set up queue of cards
    # For each card in queue:
    #   Find corresponding cards
    #   Add total amount of new cards to total
    #   Add new cards to queue.



    # First we need to find all solutions to the cards.
    
    # Variable for holding the total amount scratch cards done.
    totalScratchcardAmount = 0
    return totalScratchcardAmount