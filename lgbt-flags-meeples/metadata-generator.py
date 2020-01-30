## -- Takes a list of entries from list.csv and writes and populates metadata.csv with it

import csv, os
# Import itemgetter for advanced sort
from operator import itemgetter
# Set up directory
dirname = os.path.dirname(__file__)
list_file = os.path.join(dirname, 'list.csv')
metadata_file = os.path.join(dirname, 'metadata.csv')
# Set up lists
list_fields = []
metadata_fields = []
subjects = []
input_dict = []
# Open list CSV and add contents to above lists
with open(list_file) as list_csv:
    print("Reading file list.csv")
    reader = csv.DictReader(list_csv)
    list_fields = reader.fieldnames
    # Update entries list with all rows from CSV
    for row in reader:
        # Bring in row as a dict
        subject = {}
        subject.update(row)
        # And then append the dict to the subjects list
        subjects.append(subject)
        print("Added {subject} to subjects list".format(subject=row[list_fields[0]]))
    print("Finished reading file\n---------------------")

# Read in headers from metadata.csv to allow for changes to headers
with open(metadata_file) as meta_csv:
    print("Reading file metadata.csv")
    reader = csv.DictReader(meta_csv)
    print("Updating headers list")
    metadata_fields = reader.fieldnames
    print("Finshed reading file\n---------------------")

print("Creating input dictionary\n---------------------")
# Loop through the subjects list to create a dictionary entry with the subject's metadata
for item in subjects:
    input_dict.append({metadata_fields[0]: "{subject} pride painted meeple".format(subject=item[list_fields[0]].title()), metadata_fields[1]: "board games, boardgames, gamer, boardgamer, board gamer, tabletop, meeple, painted, graffiti, nerd, geek, flag, pride, {subject_type}, {subject}".format(subject_type=item[list_fields[1]], subject=item[list_fields[0]]), metadata_fields[2]: "Can't decide between declaring your {subject} pride and your board-gamer pride? Now you don't have to with this vibrant, {subject} pride, painted meeple design!".format(subject=item[list_fields[0]])})

# Sort the subjects list so the final metadata.csv is in alphabetical order, this uses itemgetter as it is a list of dicts
sorted_input_dict = sorted(input_dict, key=lambda k: k['title'])

# Write entries to metadata.csv
with open(metadata_file, "w", newline="") as meta_csv:
    print("Writing to file metadata.csv")
    writer = csv.DictWriter(meta_csv, fieldnames=metadata_fields)
    writer.writeheader()
    for item in sorted_input_dict:
        writer.writerow(item)
        print("Wrote a new row for {item}".format(item=item["title"]))
    print("Finished writing to file\n---------------------")
