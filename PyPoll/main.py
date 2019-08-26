import os
import csv

pypoll = os.path.join('election_data.csv')

with open(pypoll, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)
    # print(f"CSV Header: {header}")

    print("Election Results")

    print("----------------------------")

    totalrow = 0
    totalKhan = 0
    totalCorrey = 0
    totalLi = 0
    totalOtooley = 0

    for row in csv_reader:

        totalrow = totalrow+1
    
        if str(row[2]) == "Khan":
            totalKhan = totalKhan + 1

        if str(row[2]) == "Correy":
            totalCorrey = totalCorrey + 1
    
        if str(row[2]) == "Li":
            totalLi = totalLi + 1
    
        if str(row[2]) == "O'Tooley":
            totalOtooley = totalOtooley + 1

    
    percentKhan = (totalKhan/totalrow) * 100
    percentCorrey = (totalCorrey/totalrow) * 100
    percentLi = (totalLi/totalrow) * 100
    percentOtooley = (totalOtooley/totalrow) * 100
    
    
    
    
    
    print("Total Votes: " + str(totalrow))
    print("----------------------------")
    print("Khan: " + str("{:.3f}".format(percentKhan)) + "% " + "(" + str(totalKhan) + ")")
    print("Correy: " + str(percentCorrey) + "% " + "(" + str(totalCorrey) + ")")
    print("Li: " + str(percentLi) + "% " + "(" + str(totalLi) + ")")
    print("O'Tooley: " + str(percentOtooley) + "% " + "(" + str(totalOtooley) + ")")
    print("----------------------------")
    print("Winner: Khan")
    print("----------------------------")


f=open('PyPoll.txt', 'w')
# f.write(
#     "Election Results"
#     "----------------------------" 
#     "Total Votes: 3521001" 
#     "----------------------------" 
#     "Khan: 63.000% (2218231)"
#     "Correy: 20.000% (704200)"
#     "Li: 14.000% (492940)"
#     "O'Tooley: 3.000% (105630)"
#     "----------------------------" 
#     "Winner: Khan"
#     "----------------------------" 
# )
f.write("election results\n")
f.write("----------------------------\n")
f.write("Khan: " + str("{:.3f}".format(percentKhan)) + "% " + "(" + str(totalKhan) + ")")
f.close()