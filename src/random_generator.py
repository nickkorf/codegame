import csv
import random
import sys

WORDS_CSV_FILE = '../resources/words_english.csv'
dictionary = None
teamA = []
teamB = []
neutral = []
initial_selection = []
forbidden = None


def get_dictionary():
    thesaurus = None
    with open(WORDS_CSV_FILE, "r") as csv_file:
        reader = csv.reader(csv_file)
        thesaurus = {rows[0]:rows[1].strip() for rows in reader}
    return thesaurus


def main(thesaurus_size):
    dictionary = get_dictionary()
    while len(teamA) < 9:
        key = random.randint(1, int(thesaurus_size))
        if not dictionary[str(key)] in teamA:
            teamA.append(dictionary[str(key)])
        if int(key) in range(0,  20):
            print(key)
    for e in teamA:
        print(e)

if __name__ == '__main__':
    main(sys.argv[1])
