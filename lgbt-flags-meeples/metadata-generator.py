## -- Takes a list of entries from list.csv and writes and populates metadata.csv with it

import csv, os, shutil
# Import itemgetter for advanced sort
from operator import itemgetter
# Import tempfile to allow writing back to orignal file without overwtriting
from tempfile import NamedTemporaryFile

# Set up directory
dirname = os.path.dirname(__file__)
list_file = os.path.join(dirname, 'list.csv')
metadata_file = os.path.join(dirname, 'metadata.csv')
tempfile = NamedTemporaryFile(mode="w", delete=False, newline="")
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
        # Only bring in new rows
        if row[list_fields[2]] == "":
            # Bring in row as a dict
            subject = {}
            subject.update(row)
            # And then append the dict to the subjects list
            subjects.append(subject)
            print("Added {subject} to subjects list".format(subject=row[list_fields[0]]))
    print("Finished reading file\n---------------------")

# Only continue if changes were made
if subjects:
    # Update rows taken from file to add "done" flag
    print("Opening temporary file version of list file")
    with open(list_file, "r") as list_csv, tempfile:
        reader = csv.DictReader(list_csv, fieldnames=list_fields)
        writer = csv.DictWriter(tempfile, fieldnames=list_fields)
        # Update new rows to show that they have been processed
        for row in reader:
            if row[list_fields[2]] == "":
                print("Setting row for {subject} to done".format(subject=row[list_fields[0]]))
                # We only need to pass the new value to the done column
                row[list_fields[2]] = "y"
            # Rebuild the row dictionary ready to write to the file
            row = {list_fields[0]: row[list_fields[0]], list_fields[1]: row[list_fields[1]], list_fields[2]: row[list_fields[2]]}
            # Write the row to the temp file
            writer.writerow(row)
        print("Finished writing to file")
    print("Overwriting list file with temp version\n---------------------")
    shutil.move(tempfile.name, list_file)

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
else:
    print("No new items were found")