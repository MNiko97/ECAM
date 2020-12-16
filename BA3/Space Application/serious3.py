import csv
import random
import time
"""
Given the size of the assignment, I kept it all in one file.
The functions are ordered by usage.
"""

# The names of the files
city_file_name = r"C:\Users\Niko\OneDrive - ECAM\ECAM\GitHub\ECAM\BA3\Space Application\Cities.csv"
char_file_name = r"C:\Users\Niko\OneDrive - ECAM\ECAM\GitHub\ECAM\BA3\Space Application\Characters.csv"
initial_homes_file_name = "InitialHomesOfArtemia.csv"
result_file_name = "CharacterJourney.csv"

# 3 data structures used by different functions
char_itinerary_dic = {}  # A dictionary, with chars as keys and a list of the cities they have been to
city_population_dic = {}  # A dictionary, with cities as keys and a list of chars that are in the city
available_chars_for_teleportation = []  # Characters that can be chosen for teleportation


# Extracts data from csv files that only contain a column of data to a list
def extract_csv(filename: str):
    with open(filename, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        content = []
        for row in csv_reader:
            content.append(row[0])
    return content


# Writes the initial character distribution into a csv file
def write_cities_with_populations_to_file(filename):
    with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        for city, population in city_population_dic.items():
            row = [city]
            # This part is not needed if only use this function when cities have at most 1 person
            # I added it so that the function truly works like its name states
            for person in population:
                row.append(person)
            csvwriter.writerow(row)  # Write the prepared rows with the itinerary


# Randomly place the characters in one city making sure that there is no more than one character in one city
def initial_distribution():
    available_cities = extract_csv(city_file_name)
    chars = extract_csv(char_file_name)

    for char in chars:
        initial_city_for_char = random.choice(available_cities)
        available_cities.remove(initial_city_for_char)

        # Update all data structures
        city_population_dic[initial_city_for_char] = [char]
        char_itinerary_dic[char] = [initial_city_for_char]
        available_chars_for_teleportation.append(char)

    for city in available_cities:
        # prepare empty list for cities with no population
        city_population_dic[city] = []


# Chooses four random chars and four random destinations, with is not their current location
def choose_four_char_and_destination():
    chosen_chars = []
    destinations = []
    for i in range(4):
        # To avoid errors, we stop if all characters are in the NoWhere
        if not available_chars_for_teleportation:
            break

        chosen_char = random.choice(available_chars_for_teleportation)
        available_chars_for_teleportation.remove(chosen_char)  # Prevents choosing a character twice with the same spell

        current_char_position = char_itinerary_dic[chosen_char][-1]

        """ We simulate a do-while loop by starting with the current position as destination,
        then we choose new random destinations until one is not the current position. 
        Because of the odds, this should never waste much time. 
        If often choosing the same city was likely, I would create another city list without the current position,
        and randomly choose from that.  
        """
        destination = current_char_position
        while destination == current_char_position:
            destination = random.choice(list(city_population_dic.keys()))

        chosen_chars.append(chosen_char)
        destinations.append(destination)

    for chosen_char in chosen_chars:
        available_chars_for_teleportation.append(chosen_char)

    return chosen_chars, destinations


# Executes a teleport
def teleport(char, destination):
    start_city = char_itinerary_dic[char][-1]
    city_population_dic[start_city].remove(char)

    if len(city_population_dic[destination]) < 2:
        city_population_dic[destination].append(char)
        char_itinerary_dic[char].append(destination)
        print("Successfully teleported %s from %s to %s" % (char, start_city, destination))
    else:
        char_itinerary_dic[char].append("TheNowhere")
        available_chars_for_teleportation.remove(char)
        print("%s tried to teleport to %s and was sent to TheNowhere" % (char, destination))


def game():
    for i in range(42):
        start_time = time.time()
        print("\n Using teleportspell n°" + str(i+1))
        chars, destinations = choose_four_char_and_destination()
        for char, destination in zip(chars, destinations):
            teleport(char, destination)
        time.sleep(start_time+0.04 - time.time())
    

# Since there is no direct way (i know of) to fill a csv file vertically, we prepare the rows before
def create_itinerary_output():
    rows = []
    for i in range(42):
        row = []
        for history in char_itinerary_dic.values():
            if len(history) <= i:
                row.append(" ")
            else:
                row.append(history[i])
        rows.append(row)

    return rows


def write_result(filename):
    rows = create_itinerary_output()
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(list(char_itinerary_dic.keys()))  # Add chars as headers
        csvwriter.writerows(rows)  # Write the prepared rows with the itinerary


initial_distribution()
write_cities_with_populations_to_file(initial_homes_file_name)
game()
write_result(result_file_name)