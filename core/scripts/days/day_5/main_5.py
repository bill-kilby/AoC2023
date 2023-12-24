from math import inf
import os
from turtle import distance

# TODO: Remove all the int() calls. its inefficient, just do it on parsing.

def RunSolution():
    """
    Executes and displays the solutions for Day 5.

    This function runs two separate functions: SilverSolution and GoldSolution,
    which compute the solutions for the silver and gold stars of Day 5, respectively.
    It then prints out these solutions.
    """
    print("Running Day 5 Solution...")
    # Getting the file contents.
    processedFile = FileImport()
    print(processedFile)
    # Get the silver star solution.
    silver = SilverSolution(processedFile[0])
    # Get the gold star solution.
    golden = GoldSolution(processedFile[1])
    print(f"The Silver Solution to Day 5 -> {silver}")
    print(f"The Golden Solution to Day 5 -> {golden}")

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
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_5", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_5\silver.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            # Variable for storing the current section it is on.
            currentSection = 0
            processedSilver = {"seeds": [], "seed_to_soil": [], "soil_to_fertilizer": [], "fertilizer_to_water": [],
                               "water_to_light": [], "light_to_temperature": [], "temperature_to_humidity": [], "humidity_to_location": []}
            # Looping through everyline to save the information.
            for line in daySpec:
                # Check if blank line -> If so, increase by 1.
                if (line == "\n"):
                    currentSection = currentSection+1
                    # Then skip current section
                    continue
                if (currentSection == 0): # Seeds
                    # Add seed information
                    processedSilver["seeds"] = line.split(":")[1].split()
                elif(currentSection == 1): # seed to soil
                    if(line[0].isdigit()): # Only if it part of the map.
                        processedSilver["seed_to_soil"].append(line.split())
                elif(currentSection == 2): # soil to fertilizer
                    if(line[0].isdigit()):
                        processedSilver["soil_to_fertilizer"].append(line.split())
                elif(currentSection == 3): # fertilizer to water
                    if(line[0].isdigit()):
                        processedSilver["fertilizer_to_water"].append(line.split())
                elif(currentSection == 4): # water to light
                    if(line[0].isdigit()):
                        processedSilver["water_to_light"].append(line.split())
                elif(currentSection == 5): # light to temperature
                    if(line[0].isdigit()):
                        processedSilver["light_to_temperature"].append(line.split())
                elif(currentSection == 6): # temperature to humidity
                    if(line[0].isdigit()):
                        processedSilver["temperature_to_humidity"].append(line.split())
                elif(currentSection == 7): # humidity to location
                    if(line[0].isdigit()):
                        processedSilver["humidity_to_location"].append(line.split())
    except:
        raise FileNotFoundError(f"Day 5's silver import file cannot be found!")
    # Getting the gold solution.
    try:
        scriptDirectory = os.path.dirname(__file__) # Finding the current directory string.
        scriptDirectory = scriptDirectory.replace("\scripts\days\day_5", "") # Removing up to core.
        scriptDirectory = scriptDirectory+"\inputs\day_5\gold.txt" # Adding the file import.
        with open(scriptDirectory) as daySpec:
            # Variable for storing the current section it is on.
            currentSection = 0
            processedGold = {"seeds": [], "seed_to_soil": [], "soil_to_fertilizer": [], "fertilizer_to_water": [],
                               "water_to_light": [], "light_to_temperature": [], "temperature_to_humidity": [], "humidity_to_location": []}
            # Looping through everyline to save the information.
            for line in daySpec:
                # Check if blank line -> If so, increase by 1.
                if (line == "\n"):
                    currentSection = currentSection+1
                    # Then skip current section
                    continue
                if (currentSection == 0): # Seeds
                    # Add seed information
                    processedGold["seeds"] = line.split(":")[1].split()
                elif(currentSection == 1): # seed to soil
                    if(line[0].isdigit()): # Only if it part of the map.
                        processedGold["seed_to_soil"].append(line.split())
                elif(currentSection == 2): # soil to fertilizer
                    if(line[0].isdigit()):
                        processedGold["soil_to_fertilizer"].append(line.split())
                elif(currentSection == 3): # fertilizer to water
                    if(line[0].isdigit()):
                        processedGold["fertilizer_to_water"].append(line.split())
                elif(currentSection == 4): # water to light
                    if(line[0].isdigit()):
                        processedGold["water_to_light"].append(line.split())
                elif(currentSection == 5): # light to temperature
                    if(line[0].isdigit()):
                        processedGold["light_to_temperature"].append(line.split())
                elif(currentSection == 6): # temperature to humidity
                    if(line[0].isdigit()):
                        processedGold["temperature_to_humidity"].append(line.split())
                elif(currentSection == 7): # humidity to location
                    if(line[0].isdigit()):
                        processedGold["humidity_to_location"].append(line.split())
    except:
        raise FileNotFoundError(f"Day 5's gold import file cannot be found!")
    # Returning the found processed silver, and gold, imports.
    return (processedSilver, processedGold)

def FindShortestRoute(num, map):
    # Loop through every map and see if there is a path.
    shortestPath = 0
    for path in map:
        #print(f"Map : {path}")
        # Each path contains a (destination, start, range).
        #print(f"{path[1]} < {num} < {int(path[1]) + int(path[2])}")
        if (int(path[1]) <=  num <= (int(path[1])+int(path[2]))):
            # If the number is in the map ->
            difference = abs(int(path[1]) - num)
            #print(f"Seed {num} mapped onto {path[1]} with difference {difference}!")
            return int(path[0]) + difference
    return num # Return same number if not mapped on

def SilverSolution(solutionData):
    print("\nStarting Silver Solution...")
    # Variable for storing the final locations of seeds.
    seedLocations = []
    # Loop through each seed and send it down the map.
    for seed in solutionData["seeds"]:
        print(f"\nProcessing seed {seed}!")
        soil = FindShortestRoute(int(seed), solutionData["seed_to_soil"])
        print(f"Seed {seed} mapped onto Soil {soil}!")
        fertilizer = FindShortestRoute(soil, solutionData["soil_to_fertilizer"])
        print(f"Soil {soil} mapped onto Fertilizer {fertilizer}!")
        water = FindShortestRoute(fertilizer, solutionData["fertilizer_to_water"])
        print(f"Fertilizer {fertilizer} mapped onto Water {water}!")
        light = FindShortestRoute(water, solutionData["water_to_light"])
        print(f"Water {water} mapped onto Light {light}!")
        temperature = FindShortestRoute(light, solutionData["light_to_temperature"])
        print(f"Light {light} mapped onto Temperature {temperature}!")
        humidity = FindShortestRoute(temperature, solutionData["temperature_to_humidity"])
        print(f"Temperature {temperature} mapped onto Humidity {humidity}!")
        location = FindShortestRoute(humidity, solutionData["humidity_to_location"])
        print(f"Humidty {humidity} mapped onto Location {location}!")
        seedLocations.append(location)
    # Then just return the smallest location.
    return min(seedLocations)

def FindShortestRanges(ranges, map):
    # where ranges are the possible ranges and the maps are the maps.
    # for each range in ranges:
    #   for each path in map
    #       if any part of range is in map
    #           split part of map in range with part outside
    #           apply transformation of map in range
    newRanges = []
    # Loop through every range.
    for distanceRange in ranges:
        hasBeenSplit = False
        # For each range, check if its in any map
        for path in map:
            print(f"\nChecking {distanceRange} in {path}!")
            if (int(path[1]) <= distanceRange[0] <= int(path[1])+int(path[2])):
                # If start of range is inside of path.
                print(f"First part in range! -> {path[1]} < {distanceRange[0]} < {int(path[1])+int(path[2])}")
                if (distanceRange[1] > int(path[1])+int(path[2])):
                    #TODO: I NEED TO APPLY THE CHANGES TO THE RANGE IN THE AREA..
                    #TODO: -> WHY WHY WHY IS THIS NOT WORKING
                    # I NEED TO MAKE IT SO THAT THE NUMBERS (IN) THE RANGES ARE CHANGED. NOT THE OTHERS. HOW?
                    # (PATH + DIFFERENCE, END-OF-MAP-WITH-CONVERSION??? HOW DO I DO THIS)
                    print("Splitting ranges!")
                    # Add on the first range (start of range) -> (map end), with conversion.
                    newRanges.append((int(path[0]) + abs(int(path[1]) - distanceRange[0]), int(path[1])+int(path[2])))
                    # Add on second range (map end) -> (end of range), without conversion.
                    newRanges.append((int(path[1])+int(path[2]), distanceRange[1]))
                    # Let the algo know that it has been split
                    hasBeenSplit = True
                else:
                    print(f"Second part in range! -> {path[1]} < {distanceRange[1]} < {int(path[1])+int(path[2])}")
                    # If end of range is inside of path, all of it is inside of path, so just add updated range.
                    newRanges.append((int(path[0]) + abs(int(path[1]) - distanceRange[0]), int(path[0]) + abs(int(path[1]) - distanceRange[1])))
                    # Let the algo know the range has been updated.
                    hasBeenSplit = True
        # If no splits have been made, it just maps on as per usual.
        if (hasBeenSplit == False):
            newRanges.append(distanceRange)
    # Remove any duplicates.
    newRanges = list( dict.fromkeys(newRanges) )
    print(f"From {ranges} to {newRanges}!")
    return newRanges


def GoldSolution(solutionData):
    print("\nStarting Gold Solution...")
    smallestSeed = inf
    # Similiar to the approach of the past one.
    # Loop through every pair of seeds:
    #   # Find map for them. For each map, if it is found, find the exact range and make a new set with that range. 
    #   EXAMPLE: [1..10] with map [2..3] should split into [1], [2..3], [4..10]
    #   Apply the differneces to these new ranges.
    #   Rpeat the above steps for all te ranges provided in the seeds
    totalSeeds = []
    # Loop through each pair of data.
    for seed in range(0, len(solutionData["seeds"]), 2):
        # Seed range contains tuples of (start_of_range, end_of_range)
        seedRange = [(int(solutionData["seeds"][seed]),int(solutionData["seeds"][seed])+int(solutionData["seeds"][seed+1]))]
        # Pass seedRange through a function that returns the new list of seed ranges.
        soilRange = FindShortestRanges(seedRange, solutionData["seed_to_soil"])
        print("============================================SOIL DONE")
        fertilizerRange = FindShortestRanges(soilRange, solutionData["soil_to_fertilizer"])
        print("============================================FERTILIZER DONE")
        waterRange = FindShortestRanges(fertilizerRange, solutionData["fertilizer_to_water"])
        print("============================================WATER DONE")
        lightRange = FindShortestRanges(waterRange, solutionData["water_to_light"])
        print("============================================LIGHT DONE")
        temperatureRange = FindShortestRanges(lightRange, solutionData["light_to_temperature"])
        print("============================================TEMPERATURE DONE")
        humidityRange = FindShortestRanges(temperatureRange, solutionData["temperature_to_humidity"])
        print("============================================HUMIDITY DONE")
        locationRange = FindShortestRanges(humidityRange, solutionData["humidity_to_location"])
        print("============================================LOCATION DONE")
        # Loop through each possible location and store the shortest one.
        for location in locationRange:
            totalSeeds.append(location[0])
    # Then just return the smallest location.
    print(totalSeeds)
    return min(totalSeeds)