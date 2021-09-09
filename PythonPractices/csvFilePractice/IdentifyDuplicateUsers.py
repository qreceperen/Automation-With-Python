import csv
from types import CellType
# TODO find all the users

entries = []
duplicate_entries = [] 
with open ('/Users/eren/Automation-With-Python/PythonPractices/csvFilePractice/CleanDuplicateUsers.csv', 'r') as csv_file:
    my_file = csv.reader(csv_file)
    for line in my_file:
        combineFirstLastName = line[0]+line[1]
        if combineFirstLastName not in entries:
            entries.append(combineFirstLastName)
        else:
            duplicate_entries.append(combineFirstLastName)

        print(duplicate_entries)

        # print(combineFirstLastName)
    #     columns = line.strip().split(',')
    #     if columns[1] not in entries:
    #         entries.append(columns[1])
    #     else:
    #         duplicate_entries.append(columns[1])
    # print(duplicate_entries)


# with open ('/Users/eren/Automation-With-Python/PythonPractices/csvFilePractice/CleanDuplicateUsers.csv', 'r') as csv_file:
#    CleanDuplicateUsers = csv.reader(csv_file)
#    for line in CleanDuplicateUsers:
#        print(line[0:2])

       # Line 8 is log in time

# ('/Users/eren/Automation-With-Python/PythonPractices/csvFilePractice/CleanDuplicateUsers.csv', 'r')





# TODO combine first and last name
# TODO find all duplicate users from their name