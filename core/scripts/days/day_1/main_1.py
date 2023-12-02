import os, re

def RunSolution():
    """
    Executes and displays the solutions for Day 1.

    This function runs two separate functions: SilverSolution and GoldSolution,
    which compute the solutions for the silver and gold stars of Day 1, respectively.
    It then prints out these solutions.
    """
    print("Running Day 1 Solution...")
    # Getting the file contents.
    processedFile = FileImport()
    # Get the silver star solution.
    silver = SilverSolution(processedFile[0])
    # Get the gold star solution.
    golden = GoldSolution(processedFile[1])
    print(f"\nThe Silver Solution to Day 1 -> {silver}")
    print(f"The Golden Solution to Day 1 -> {golden}")

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
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_1", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_1\silver.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            # Looping through the lines and loading the data.
            processedSilver = []
            for line in daySpec:
                processedSilver.append(line)
    except:
        raise FileNotFoundError(f"Day 1's silver import file cannot be found!")
    # Getting the gold solution.
    try:
        scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_1", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_1\gold.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            # Looping through the lines and loading the data. Same as Silver today.
            processedGold = []
            for line in daySpec:
                processedGold.append(line)
    except:
        raise FileNotFoundError(f"Day 1's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def SilverSolution(solutionData):
    """
    Computes the sum of the first and last numeric characters in each string of a list.

    The function iterates through each string in the provided list. It first finds the first numeric character
    by scanning from the beginning of the string, and then finds the last numeric character by scanning from
    the end. It concatenates these two characters to form a number, which is then added to a running total.

    :param solutionData: A list of strings, each potentially containing numeric characters.
    :type solutionData: list
    :return: The sum of the concatenated first and last numeric characters in each string.
    :rtype: int

    :Example:

    >>> SilverSolution(["123", "4567", "89a"])
    110

    In the example, "123" contributes 13 (1 + 3), "4567" contributes 47 (4 + 7), and "89a" contributes 89 (8 + 9),
    leading to a total of 110.
    """
    print("\nSILVER SOLUTION OUTPUTS: ")
    solution = 0
    for line in solutionData:
        for char in line:
            try:
                int(char) # Check if it is an int. If it isn't, move on.
                last = char
            except:
                None
        # Repeat backwards.
        for char in reversed(line):
            try:
                int(char)
                first = char
            except:
                None
        # Then append and calculate.
        solution = solution + int(first+last)
        print(f"{line.strip()} -> {first+last}") # Debug output
    return solution 

def GoldSolution(solutionData):
    """
    Computes a sum based on specific rules applied to each line in the provided data.

    This function processes a list of strings (`solutionData`). For each string, it uses a regular expression to find
    all occurrences of specified number words (like "one", "two", etc.) and digits, including overlapping matches. 
    It then determines the first and last number in the discovered list, converts them to their numeric equivalents 
    (if they are words), concatenates them to form a new number, and adds this number to a running total.

    The number words are defined in the `numberStrings` dictionary and are converted to their numeric equivalents.

    :param solutionData: A list of strings, each containing numbers as digits or words.
    :type solutionData: list
    :return: The sum of the concatenated first and last numbers (as digits) found in each string.
    :rtype: int

    :Example:

    >>> GoldSolution(["onetwothree21"])
    21

    In this example, "onetwothree21" would result in a first number of '1' (from "one") and a last number of '1' (the digit),
    thus contributing '11' to the sum.
    """
    print("\nGOLD SOLUTION OUTPUTS: ")
    # The idea here is different -> Instead using regex to find all occurances of the words in the string, and then combining them.
    numberStrings = {"one" : 1,"two" : 2,"three" : 3,"four" : 4,"five" : 5,"six" : 6,"seven" : 7,"eight" : 8,"nine" : 9}
    solution = 0
    for line in solutionData:
        # Find all occurances of the words above, including overlaps.
        regex = r'(?=(' + '|'.join(numberStrings.keys()) + "|\d" + r'))'
        discoveredNumberList = re.findall(regex, line)
        # If discovered, then format and calculate.
        if(len(discoveredNumberList) != 0):
            # Check to see if int or number, saving accordingly for the first occurance.
            try:
                int(discoveredNumberList[0])
                first = discoveredNumberList[0]
            except:
                first = str(numberStrings[discoveredNumberList[0]])
            # Check to see if int or number, saving accordingly for the last occurance.
            try:
                int(discoveredNumberList[len(discoveredNumberList)-1])
                last = discoveredNumberList[len(discoveredNumberList)-1]
            except:
                last = str(numberStrings[discoveredNumberList[len(discoveredNumberList)-1]])
            # Formatting number, and then calculating.
            formattedNumber = first+last
            solution = solution + int(formattedNumber)
            print(f"{line.strip()} -> {discoveredNumberList} : {formattedNumber}") # Debug output
        else:
            print(f"{line.strip()} -> {discoveredNumberList} : No formatted numbers exist!") # Debug output
    return solution