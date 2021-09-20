import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
    """Downloads the data"""
    if not url:
        return None # strictly return data in url only
    with urllib.request.urlopen('') as response:
        html = response.read() # read file in URL
    return url

def processData(file_content):
    with open('employee_birthday.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(
                f'\t{row["name"]} was born in {row["birthday"]}.')
                line_count += 1
        dict.get(id[name, birthday=object], default=None)

    LOG_FILENAME = 'logging_example.out'
    logging.basicConfig(
        filename=assignment2,
        level=logging.DEBUG,
    )

    logging.debug('Error processing line #<linenum> for ID #<id>')

    with open(LOG_FILENAME, 'rt') as f:
        body = f.read()

    print('FILE:')
    print(body)

def displayPerson(id, personData):
    """
    Print the name and birthday of a given user identified by the input id .
    """
    if not id:
        return None
    if not personData:
        return None
    try:
        print ("Person #{id} is <name> with a birthday of <date>.")
    except KeyError:
        logger.error("No user found with that id.")

def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser(--url)
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    downloadData(url)
    while True:
        try:
            id = int(raw_input("Enter a person ID: "))
        except ValueError:
            print
            "Invalid input. Please try again."
            continue
        if id <= 0:
            print
            "Exiting program."
            sys.exit()
    processData(csvData)
    main(args.url)