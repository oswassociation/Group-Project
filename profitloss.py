from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    day_profit = []
    for row in reader:
        day_profit.append([row[0],row[4]])

#Creating an empty list and assigning it to the variable profit_deficit
def profitlosscalc():
    """
    - This function does not accept any parameters 
    - This function checks if the net profit on the current day is lower than the previous day 
    - This function will find the difference between the current and previous day net profit if the current day net profit is lower 
    """
    filepath = Path.cwd()/"summary_report.txt"
    filepath.touch()
    # using "a" to append the data from the function to the txt file 
    with filepath.open(mode="a",encoding = "UTF-8") as file :
    # creating an empty list and assigning it to the variable profit_deficit 
        profit_deficit=[]
        # using a for loop to loop the data from the range of 1, length of the day_profit list 
        for day in range(1,len(day_profit)) :
            # calculating the netprofit if the current day's profit is lower than that of the previous day 
            netprofit=int(day_profit[day-1][1])- int(day_profit[day][1])
            # using if to check if the current day profit is more than the previous day 
            if int(day_profit[day][1]) > int(day_profit[day-1][1]) and netprofit > 0:
                # returning the statement if the the current day profit is more than that of the previous day
                print ("NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
            # checking if the profit of the current day is lower than that of the previous day 
            elif int(day_profit[day][1]) < int(day_profit[day-1][1]):
                # assigning the day from the day_profit list to the day_num variable 
                day_num = day_profit[day][0] 
                # appending the day and calculated ne profit into the empty profit_deficit list 
                profit_deficit.append([day_num,netprofit]) 
        # assigning the profit deficit statement to the statement variable and using join() to insert a newline after each statement
        # and using a for loop to loop the day and amount data from the profit_deficit list 
        for day,amount in profit_deficit:
            file.write(f"[PROFIT DEFICIT] DAY: {day},AMOUNT: USD {amount}\n")
profitlosscalc()






