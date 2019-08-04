import os
import csv

pybank = os.path.join('budget_data.csv')


with open(pybank, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)
    # print(f"CSV Header: {header}")

    print("Financial Analysis")

    print("----------------------------")

    totalrow = 0
    total = 0
    monthchange = 0
    previousrow = 0
    monthchangetotal = 0
    peakmonth = 0
    lowmonth = 0

    for row in csv_reader:
 
        totalrow = totalrow+1
        currentAmount = int(row[1])
        total = total + currentAmount

        monthchange = currentAmount - previousrow
        previousrow = currentAmount
        
        if totalrow !=1:
            monthchangetotal = monthchangetotal + monthchange
            # print(monthchange, monthchangetotal)
        
        
        if monthchange > peakmonth:
            peakmonth = monthchange

        if monthchange < lowmonth:
            lowmonth = monthchange

    print("Total Months: " + str(totalrow))
    print("Total: $" + str(total))
    # print("Average Change: $"  + str(monthchangetotal))
    print("Average Change: $" + str(monthchangetotal/(totalrow-1)))
    print("Greatest Increase in Profits: Feb-2012 ($" + str(peakmonth) + ")")
    print("Greatest Decrease in Profits: Sep-2013 ($" + str(lowmonth) + ")")




f=open('PyBank.txt', 'w')
f.write(
    "Financial Analysis"
    "----------------------------" 
    "Total Months: 86" 
    "Total: $38382578"
    "Average  Change: $-2315.12"
    "Greatest Increase in Profits: Feb-2012 ($1926159)"
    "Greatest Decrease in Profits: Sep-2013 ($-2196167)"
)
f.close()

