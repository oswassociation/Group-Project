from pathlib import Path
import csv

fp = Path.cwd()/ "csv_reports" / "overheads-day-90.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        overheads = []
        for row in reader: 
            overheads.append([row[0],row[1]])

# creating a function to find out which overhead expense is the highest 
def overheadscalc(): 
        # assigning 0 to the variable highest_value
        highest_value = 0
        # using for loop to loop the data from the overheads list and looping it to continuously check the data with each other to find the highest
        for data in overheads: 
            # checking if the percentage from the list is higher than 0
            if float(data[1]) > highest_value:
                # assigning the highest value to the variable highest_value
                highest_value = float(data[1])
                # assigning the category name to the variable 
                highest_category = data[0].upper()
        # creating a txt file            
        fp_cwd = Path.cwd() / "summary_report.txt" 
        fp_cwd.touch()
        # writing the statement of highest overhead into the txt file
        with fp_cwd.open(mode="w", encoding="UTF-8") as file:
            file.write(f'[HIGHEST OVERHEAD] {highest_category}: {highest_value}%\n')

overheadscalc()




        


