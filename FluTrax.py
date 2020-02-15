import matplotlib.pyplot as plt
import numpy as np

date = ['2/03/2020', '2/04/2020', '2/05/2020', '2/06/2020', '2/07/2020', '2/08/2020', '2/09/2020']

dateIndex = list(range(len(date)))

numberOfPatients = [10000, 80000, 60000, 200000, 300000, 400000, 450000]

plt.ylim(0, 500000)

plt.plot(numberOfPatients, marker = "o")

plt.ylabel("Number of Patients")

plt.xlabel("Date")

plt.xticks(dateIndex, date)

plt.title("Trend of Increasing Rate of Flu Hospitalizations For Patients")

plt.show()

userDate = input("Do you want to update this data? If yes, type: y. If not, type: n\n")

while userDate != 'y' and userDate != 'n':

    userDate = input("Do you want to update this data? If yes, type: y. If not, type: n\n")

if_leap_year = False

while True:
    yearInput = input("Enter the year: ")
    while int(yearInput) > 2020 or int(yearInput) < 0:
        yearInput = input("Enter the year: ")
    if int(yearInput) / 4 == 0:
        if int(yearInput) / 100 == 0:
            if int(yearInput) / 400 == 0:
                if_leap_year = True
        else:
            if_leap_year = True
    monthInput = input("Enter the month: ")
    while int(monthInput) > 12 or int(monthInput) < 1:
        monthInput = input("Enter the month: ")
    dayInput = input("Enter the day: ")
    if monthInput == '2' and if_leap_year == True:
        while int(dayInput) < 0 or int(dayInput) > 29:
            dayInput = input("Enter the day: ")
    if monthInput == '2' and if_leap_year == False:
        while int(dayInput) < 0 or int(dayInput) > 28:
            dayInput = input("Enter the day: ")
    if monthInput == '1' or monthInput == '3' or monthInput == '5' or monthInput == '7' or monthInput == '8' or monthInput == '10' or monthInput == '12':
        while int(dayInput) < 0 or int(dayInput) > 31:
            dayInput = input("Enter the day: ")
    else:
        while int(dayInput) < 0 or int(dayInput) > 30:
            dayInput = input("Enter the day: ")
    numberOfPatientsInput = input("Enter the number of patients: ")
    while int(numberOfPatientsInput) < 0:
        numberOfPatientsInput = input("Enter the number of patients: ")
        
    if int(numberOfPatientsInput) < 100000:
        print("SUGGESTION: GET VACCINATED.")
    elif int(numberOfPatientsInput) < 250000:
        print("REQUIRED: TAKE ACTIONS EVERY DAY TO HELP STOP THE SPREAD OF GERMS.")
    else:
        print("WARNING: NEED ANTIVIRAL MEDICATION TO TREAT FLU.")
    
    date.append('{}/{}/{}'.format(monthInput, dayInput, yearInput))
    numberOfPatients.append(int(numberOfPatientsInput))
    userInput = input("To exit the program, type: e\n")
    if userInput == 'e':
        break

dateIndex = list(range(len(date)))

plt.ylim(0, 500000)

plt.plot(numberOfPatients, marker = "o")

plt.ylabel("Number of Patients")

plt.xlabel("Date")

plt.xticks(dateIndex, date)

plt.title("Increasing Rate of Flu Virus in Patients")

plt.show()