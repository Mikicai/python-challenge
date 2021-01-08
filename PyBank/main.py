# Import modules
import os
import csv

# set the path for the resource file
budget_data=os.path.join("Resources","budget_data.csv")

#create lists to store data for total months and total profit and loss and variables
months=[]
profit_loss=[]
total_monthly_change=[]
# max_date=""
# greatest_decrease_date=""


# Read csv file
with open(budget_data,'r') as csvfile:

    #read the csv file with split between commas
    csvreader=csv.reader(csvfile,delimiter=',')

    #skip the head row
    header=next(csvreader)
    


    # loop through each row in csv file
    for row in csvreader:

        # add the months to the months list
        months.append(row[0])

        # add the total of profit and loss to profit_loss list
        profit_loss.append(int(row[1]))

        #calculate the total month in the month list
        total_months=len(months)

        #calcualte the total profit and loss
        total_profit_loss=sum(profit_loss)

        #calculate the average change of profit/loss
        for i in range (0,len(profit_loss)-1):
            monthly_change=int(profit_loss[i+1])-int(profit_loss[i])
            total_monthly_change.append(monthly_change)

    # find out the greatest increase in profit
    max_increase=max(total_monthly_change)
  
    # work out the month that match the result
    max_date=months[profit_loss.index(max(profit_loss))]
   

    # find out the greatest decrease in loss
    greatest_decrease=min(total_monthly_change)
   

    #find out the month that matches the greatest decrease
    greatest_decrease_date=months[profit_loss.index(min(profit_loss))]


    # work out the average change.
    average_change=sum(total_monthly_change)/len(total_monthly_change)





# print the result
    print(f"Financial Anysis")          
    print(f"------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: {average_change:2f}")
    print(f"Greatest Increase in Profits: {max_date} ($ {max_increase})")
    print(f"Greatest Decrease in Loss: {greatest_decrease_date} ($ {greatest_decrease})")

#output the result as txtfile
output_file=os.path.join("Analysis","result.txt")

#write result to txt file
with open("result.txt","w") as txtfile:
    print(f"Financial Anysis\n", file=txtfile)          
    print(f"------------------------------------------\n",file=txtfile)
    print(f"Total Months: {total_months}\n",file=txtfile)
    print(f"Total: ${total_profit_loss}\n",file=txtfile)
    print(f"Average Change: {average_change:2f}\n",file=txtfile)
    print(f"Greatest Increase in Profits: {max_date} ($ {max_increase})\n",file=txtfile)
    print(f"Greatest Decrease in Loss: {greatest_decrease_date} ($ {greatest_decrease})\n",file=txtfile)

