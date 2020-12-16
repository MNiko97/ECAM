import csv
import random
import time

city_file_name = "Cities.csv"
char_file_name = "Characters.csv"
initial_homes_file_name = "InitialHomesOfArtemia.csv"
result_file_name = "output.csv"

char_data = {}
city_data = {}
available_chars = []


def extract_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        content = []
        for row in csv_reader:
            content.append(row[0])
    return content


def write_csv(filename, content):
    with open(filename, 'w') as writer:
        for city, char_list in content.items():
            writer.write("%s, %s\n" % (city, char_list))


def initial_distribution():
    available_cities = extract_csv(city_file_name)
    chars = extract_csv(char_file_name)

    for char in chars:
        initial_city_for_char = random.choice(available_cities)

        # Used a dictionary with list as items because several characters will be able to be in the same city
        city_data[initial_city_for_char] = [char]
        char_data[char] = [initial_city_for_char]
        available_cities.remove(initial_city_for_char)
        available_chars.append(char)

    for city in available_cities:
        city_data[city] = []


def choose_four_char_and_destination():
    chars = []
    destinations = []
    for i in range(4):
        if not available_chars:
            break
        char = random.choice(available_chars)
        available_chars.remove(char)
        # The last city is where he currently is at
        destination = char_data[char][-1]
        while destination == char_data[char][-1]:
            destination = random.choice(list(city_data.keys()))

        chars.append(char)
        destinations.append(destination)

    for char in chars:
        available_chars.append(char)

    return chars, destinations


def teleport(char, destination):
    start_city = char_data[char][-1]
    city_data[start_city].remove(char)

    if len(city_data[destination]) < 2:
        city_data[destination].append(char)
        char_data[char].append(destination)
        print("Successfully teleported %s from %s to %s" % (char, start_city, destination))
    else:
        char_data[char].append("TheNowhere")
        available_chars.remove(char)
        print("%s tried to teleport to %s and was sent to TheNowhere" % (char, destination))


def game():
    print(available_chars)
    print(city_data)
    print(city_data.keys())
    print(char_data)
    for i in range(42):
        print("Using teleportspell " + str(i+1))
        if not available_chars:
            print("All in Nowhere")
            break
        chars, destinations = choose_four_char_and_destination()
        for char, destination in zip(chars, destinations):
            teleport(char, destination)
    time.sleep(0.04)


def adapt():
    rows = []
    for i in range(42):
        row = []
        for history in char_data.values():
            if len(history) <= i:
                row.append(" ")
            else:
                row.append(history[i])
        rows.append(row)

    return rows

def write_result(filename):
    rows = adapt()
    chars = extract_csv(char_file_name)
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(list(char_data.keys()))
        csvwriter.writerows(rows)

initial_distribution()
game()
write_result(result_file_name)