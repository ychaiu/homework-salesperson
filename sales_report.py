"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# salespeople = []
# melons_sold = [] # empty list

# f = open("sales-report.txt") # opens the text file, creating file object
# for line in f: # iterate over each line in the file
#     line = line.rstrip() #strip any spaces to the right of each line
#     entries = line.split("|") # split on the pipe
#     salesperson = entries[0] # first item in entries is the salesperson name
#     melons = int(entries[2]) # third item in entries is the number melons sold

#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)


# for i in range(len(salespeople)):
#     print("{} sold {} melons".format(salespeople[i], melons_sold[i]))

# rewrite using dictionaries

ppl_melons_sold = {}

f = open("sales-report.txt") # opens the text file, creating file object
for line in f: # iterate over each line in the file
    line = line.rstrip() #strip any spaces to the right of each line
    entries = line.split("|") # split on the pipe
    salesperson = entries[0]
    ppl_melons_sold[salesperson] = ppl_melons_sold.get(salesperson, 0) + int(entries[2])

for salesperson, melons_sold in ppl_melons_sold.items():
    print("{} sold {} melons".format(salesperson, melons_sold))
