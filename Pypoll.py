    #Import the OS module "Step#1"
import os
#Module for reading the Csv "Step#2"
import csv

# Declaring Variables "Step#6"

total_votes = 0

khan_votes = 0

correy_votes = 0

li_votes = 0

otooley_votes = 0

pypoll= os.path.join("C:/Users/jgj2079/Desktop/BootCamp/Python-Challenge/PyPoll/election_data.csv")
print(pypoll)


# Open the CSV
with open(pypoll) as csvfile:
#Syntax error urg

     # CSV reader specifies delimiter and variable that holds contents "Step#3"
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header) "Step#4"
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header "Step#5"
    for row in csvreader:
        print(row)


 # Calculate Total Number Of Votes Cast"Step#7"

        total_votes += 1

# Calculate Total Number Of Votes Each Candidate Received. "Step#8"

    if (row[2] == "Khan"):

            khan_votes += 1

    elif (row[2] == "Correy"):

            correy_votes += 1

    elif (row[2] == "Li"):

            li_votes += 1

    else:

            otooley_votes += 1

# Calculate Percentage Of Votes Each Candidate Won "Step#9"

    kahn_percent = khan_votes / total_votes

    correy_percent = correy_votes / total_votes

    li_percent = li_votes / total_votes

    otooley_percent = otooley_votes / total_votes

    
# Calculate Winner Of The Election Based On Popular Vote "Step#10"

    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)


    if winner == khan_votes:

        winner_name = "Khan"

    elif winner == correy_votes:

        winner_name = "Correy"

    elif winner == li_votes:

        winner_name = "Li"

    else:

        winner_name = "O'Tooley" 


# Print Analysis "Step#11"

print(f"Election Results")

print(f"---------------------------")

print(f"Total Votes: {total_votes}")

print(f"---------------------------")

print(f"Kahn: {kahn_percent:.3%}({khan_votes})")

print(f"Correy: {correy_percent:.3%}({correy_votes})")

print(f"Li: {li_percent:.3%}({li_votes})")

print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")

print(f"---------------------------")

print(f"Winner: {winner_name}")

print(f"---------------------------")

#convert to text_file "Final Step#12"

output_file = os.path.join("C:/Users/jgj2079/Desktop/BootCamp/Python-Challenge/PyPoll/pypoll.txt")

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents

with open(output_file, 'w',) as txtfile:

# Write New Data

    txtfile.write(f"Election Results\n")

    txtfile.write(f"---------------------------\n")

    txtfile.write(f"Total Votes: {total_votes}\n")

    txtfile.write(f"---------------------------\n")

    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")

    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")

    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")

    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")

    txtfile.write(f"---------------------------\n")

    txtfile.write(f"Winner: {winner_name}\n")

    txtfile.write(f"---------------------------\n")