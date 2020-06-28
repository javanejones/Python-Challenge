#Import the OS module "Step#1"
import os
#Module for reading the Csv "Step#2"
import csv

# Declaring Variables "Step#5"

total_months = 0

net_amount = 0

monthly_change = []

month_count = []

greatest_increase = 0

greatest_increase_month = 0

greatest_decrease = 0

greatest_decrease_month = 0

budget = os.path.join("C:/Users/jgj2079/Desktop/BootCamp/Python-Challenge/Pybank/Resources/budget_data.csv")
print(budget)
# Open the CSV
with open(budget) as csvfile:
#Syntax error urg

#Csv reader will specifies delimiter and variable "Step#3"
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
#Print Reader "Step#4"
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    for row in csvreader:
        print(row)


# Calculate Values "Step#6"

    previous_row = int(row[1])

    total_months += 1

    net_amount += int(row[1])

    greatest_increase = int(row[1])

    greatest_increase_month = row[0]

    
# Read Each Row Of Data After The Header "Step#7"

    for row in csvreader:
        
# Calculate Total Number Of Months Included In Dataset "Step#8"

        total_months += 1

# Calculate Net Amount Of "Profit/Losses" Over The Entire Period "Step#9"

        net_amount += int(row[1])


# Calculate Change From Current Month To Previous Month "Step#9"

        revenue_change = int(row[1]) - previous_row

        monthly_change.append(revenue_change)

        previous_row = int(row[1])

        month_count.append(row[0])

        
# Calculate The Greatest Increase "Step#10"

        if int(row[1]) > greatest_increase:

            greatest_increase = int(row[1])

            greatest_increase_month = row[0]

            
# Calculate The Greatest Decrease "Step#10"

        if int(row[1]) < greatest_decrease:

            greatest_decrease = int(row[1])

            greatest_decrease_month = row[0]  

        
 # Calculate The Average & The Date "Step#11"

average_change = sum(monthly_change)/len(monthly_change)
    
highest = max(monthly_change)

lowest = min(monthly_change)

 # Print Analysis "Step#12"

print(f"Financial Analysis")

print(f"---------------------------")

print(f"Total Months: {total_months}")

print(f"Total: ${net_amount}")

print(f"Average Change: ${average_change:.2f}")

print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")

print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

#convert to text_file "Final Step#13"

output_file = os.path.join("C:/Users/jgj2079/Desktop/BootCamp/Python-Challenge/Pybank/Resources/budget.txt")

with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")

    txtfile.write(f"---------------------------\n")

    txtfile.write(f"Total Months: {total_months}\n")

    txtfile.write(f"Total: ${net_amount}\n")

    txtfile.write(f"Average Change: ${average_change}\n")

    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")

    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")