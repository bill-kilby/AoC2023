from scripts import *
import sys, os

def ParseCommandLineArgs():
    """
    Parses command line arguments for a specific use case.

    This function is designed to handle 0 or 2 arguments. The first argument should be an integer representing a day request, 
    and the second argument should be a boolean indicating whether to output the problem or not.

    Returns:
        tuple: A tuple containing (dayRequest, explainMode). 'dayRequest' is an integer, and 'explainMode' is a boolean.
              Returns (None) if no arguments are passed.

    Raises:
        Exception: If the number of arguments is not 0 or 2.
        TypeError: If the first argument is not an integer or the second argument is not 'True' or 'False'.
        ValueError: If the first argument (dayRequest) is not between 1 and 25.
    """
    # Return if no arguments have been passed.
    if (len(sys.argv) == 1):
        return (None)
    # Raise an exception if an incorrect amount of arguments have been passed through.
    if (len(sys.argv) != 3):
        raise Exception("You must pass 0, or 2, arguments. Please see README.md for further information.")
    
    # Store requested day, checking if it an integer.
    try:
        dayRequest = int(sys.argv[1])
    except:
        raise TypeError("The first argument must be an Integer.")
    
    # Check to see if dayRequest is 0-25.
    if (dayRequest > 25 or dayRequest < 1):
        raise ValueError("The first argument must be between 0 and 26.")
    
    # Store whether or not the program should output the problem, checking if it is a boolean.
    if (sys.argv[2] not in ["True", "true", "False", "false"]):
        raise TypeError("The second argument must be 'True' or 'False'. Please see README.md for further information.")
    else:
        # If they've selected true, set it as true. Else, don't.
        if(sys.argv[2] in ["True", "true"]):
            explainMode = True
        else:
            explainMode = False
    # Return formatted arguments.
    return (dayRequest, explainMode)

def RunSpecifiedSolution(selectedDay):
    """
    Executes a specific solution based on the selected day.

    This function maps each day to a corresponding solution function and executes the selected solution. It relies on a dictionary `solutions` which pairs days with their respective solution functions.

    Parameters:
    selectedDay (int): An integer representing the day for which the solution needs to be run. Should be a value between 1 and 25, inclusive.

    Raises:
    KeyError: If `selectedDay` is not in the range 1 to 25.

    Returns:
    None: The function does not return any value but executes the function associated with `selectedDay`.

    Example:
    To run the solution for day 3, call `RunSpecifiedSolution(3)`.
    """
    # Setting up a dictionary of functions to improve conciseness and readability.
    solutions = {
        1: main_1.RunSolution, 2: main_2.RunSolution, 3: main_3.RunSolution, 4: main_4.RunSolution, 5: main_5.RunSolution,
        6: main_6.RunSolution, 7: main_7.RunSolution, 8: main_8.RunSolution, 9: main_9.RunSolution, 10: main_10.RunSolution,
        11: main_11.RunSolution, 12: main_12.RunSolution, 13: main_13.RunSolution, 14: main_14.RunSolution, 15: main_15.RunSolution,
        16: main_16.RunSolution, 17: main_17.RunSolution, 18: main_18.RunSolution, 19: main_19.RunSolution, 20: main_20.RunSolution,
        21: main_21.RunSolution, 22: main_22.RunSolution, 23: main_23.RunSolution, 24: main_24.RunSolution, 25: main_25.RunSolution
    }
    # Running the specified solution.
    solutions[selectedDay]()

def OutputDaySpecification(requestData):
    """
    Outputs the specification for a specified day from a text file.

    This function takes a request for a specific day's specification, constructs the file path for the corresponding text file, and prints its content. It assumes the text files are named in a specific format and located in a directory named 'specifications'.

    Parameters:
    requestData (list): A list where the first element is an integer representing the day for which the specification is requested.

    Raises:
    FileNotFoundError: If the text file corresponding to the requested day does not exist or cannot be found.

    Returns:
    None: The function does not return any value but prints the content of the specification file for the requested day.

    Example:
    To output the specification for day 5, call `OutputDaySpecification([5])`.

    Note:
    The function assumes that the text files are stored in a 'specifications' directory within the same directory as this script. The files should be named 'day_X.txt', where X is the day number.
    """
    # Loading the solution explanation .txt file.
    if(requestData[1] == True):
        try:
            dayDirectory = "specifications\\day_"+str(requestData[0])+".txt" # Creating the relative path string.
            scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
            fileDirectory = os.path.join(scriptDirectory, dayDirectory) # Creating the total path string.
            with open(fileDirectory) as daySpec:
                print(daySpec.read()) # Output the file.
        except:
            raise FileNotFoundError(f"The Day {requestData[0]} explanation file cannot be found!")

def DayMenuSelection():
    """
    This function is designed to display a menu from a text file and allow the user to select a day's challenge.
    
    The function first attempts to read and display a menu from an ASCII art file. If the file is not found, 
    it raises a FileNotFoundError. Then, it prompts the user to select a number corresponding to a day's challenge. 
    If the input is not an integer or is outside the valid range (1-25), it asks the user to re-enter. 
    Finally, it asks if the user wants to see the problem's specification and proceeds accordingly.

    Raises:
    FileNotFoundError: If the menu.txt art file cannot be found.

    """
    # Outputting the cute ASCII art menu.
    try:
        dayDirectory = "art\\menu.txt" # Creating the relative path string.
        scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
        fileDirectory = os.path.join(scriptDirectory, dayDirectory) # Creating the total path string.
        with open(fileDirectory) as daySpec:
            print(daySpec.read()) # Output the file.
    except:
        raise FileNotFoundError(f"The menu.txt art file cannot be found!")
    # Allowing user to have a get a number, repeating until they are correct.
    while True:
        try:
            # Allowing user to enter a number, then checking if it's valid.
            print("ENTER NUMBER BELOW")
            dayChoice = int(input("")) 
        except:
            print("You must enter an Integer between 1-25!")
        if ((dayChoice > 25) or (dayChoice < 1)):
            print("You must enter an Integer between 1-25!")
        else:
            # Allowing user to print the problem, then checking if it's valid.
            print("Do you want to see the problem's specification?")
            explainChoice = input("")
            if(explainChoice not in ["Yes", "yes", "No", "no"]):
                print("You must enter Yes or No!")
            else:
                if(explainChoice in ["Yes", "yes"]):
                    explainChoice = True
                else:
                    explainChoice = False
                # Running the commands which output the explanation (if chosen), and the problem solution.z
                OutputDaySpecification([dayChoice, explainChoice])
                RunSpecifiedSolution(dayChoice)
                break

        

if __name__ == "__main__":
    # Accept command line arguments.
    args = ParseCommandLineArgs()
    print("Advent of Code 2024")
    print("        - BKDEV")
    print("")

    # Decide whether to directly run, or present menu.
    if (args is not None):
        OutputDaySpecification(args)
        print("")
        RunSpecifiedSolution(args[0])
    else:
        DayMenuSelection()