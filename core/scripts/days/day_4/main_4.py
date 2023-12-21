from msvcrt import SEM_NOALIGNMENTFAULTEXCEPT
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

def GetCardWinners(card, index, solutions):
    # This feels pretty inefficient -> surely a better way than just looping through? Potential sorting (timsort?) and then searching?
    totalWinningNumbers = 0
    totalCards = 0
    # Loop through the winning cards.
    for winningNumber in card[0]:
        # Loop through the actual cards
        for actualNumber in card[1]:
            # If they won, add 1 to the total number of winnings.
            if (winningNumber == actualNumber):
                totalWinningNumbers = totalWinningNumbers + 1
    print(f"Card has won another {totalWinningNumbers}.")
    totalCards = totalCards + totalWinningNumbers
    # Loop through the amount of winning numbers and add their solutions.
    for i in range (1, totalWinningNumbers+1):
        print(f"In addition, adding Card {index+i}'s extra {solutions.get(index+i)} cards.")
        totalCards  = totalCards + solutions.get(index+i)
    print(f"Therefore, this card has a total of {totalCards} extra cards.")
    # Then return the total amount of cards
    return totalCards


def GoldSolution(solutionData):
    print("\nRunning Gold Solution")
    # Set up empty dictionary.
    scratchcardSolutions = {}
    for i in range(0, len(solutionData)):
        scratchcardSolutions[i] = 0
    print(scratchcardSolutions)
    # Set up the total result as the initial set.
    totalScratchcardAmount = len(solutionData)
    print(solutionData)
    # Loop from end to start.
    for card in range(len(solutionData)-1, -1, -1):
        print(f"\nCalculating card {card}.")
        # Getting the total amount of added cards.
        scratchcardSolutions[card] = GetCardWinners(solutionData[card], card, scratchcardSolutions)
        # Adding it to the total
        totalScratchcardAmount = totalScratchcardAmount + scratchcardSolutions[card]
    # Once all cards are done, return the total.
    return totalScratchcardAmount