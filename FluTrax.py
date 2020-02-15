import matplotlib.pyplot as plt
import datetime
import numpy as np

dates = ['2/03/2020', '2/04/2020', '2/05/2020', '2/06/2020', '2/07/2020', '2/08/2020', '2/09/2020']

dateIndex = list(range(len(dates)))

numberOfPatients = [10000, 80000, 60000, 200000, 300000, 400000, 450000]

plt.ylim(0, 500000)
plt.plot(numberOfPatients, marker="o")
plt.ylabel("Number of Patients")
plt.xlabel("Date")
plt.xticks(dateIndex, dates)
plt.title("Trend of Increasing Rate of Flu Hospitalizations For Patients")

plt.show()

date_prompt = 'Do you want to update this data? If yes, type: y. If not, type: n\n'

userDate = input(date_prompt)
while userDate != 'y' and userDate != 'n':
    userDate = input(date_prompt)

if_leap_year = False


def validate_date(year: str, month: str, day: str):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


while True:
    date_input_prompt = 'Please enter the date (mm/dd/yyyy): '
    date_input = input(date_input_prompt)
    month, day, year, *_ = date_input.split('/')
    while not validate_date(year, month, day):
        date_input = input(date_input_prompt)
        year, month, day, *_ = date_input.split('/')

    numberOfPatientsInput = -1
    while int(numberOfPatientsInput) < 0:
        numberOfPatientsInput = input("Enter the number of patients: ")

    if int(numberOfPatientsInput) < 100000:
        print("SUGGESTION: GET VACCINATED.")
    elif int(numberOfPatientsInput) < 250000:
        print("REQUIRED: TAKE ACTIONS EVERY DAY TO HELP STOP THE SPREAD OF GERMS.")
    else:
        print("WARNING: NEED ANTIVIRAL MEDICATION TO TREAT FLU.")

    dates.append('{}/{}/{}'.format(month, day, year))
    numberOfPatients.append(int(numberOfPatientsInput))
    userInput = input("To exit the program, type: e\n")
    if userInput == 'e':
        break

dateIndex = list(range(len(dates)))

plt.ylim(0, 500000)
plt.plot(numberOfPatients, marker="o")
plt.ylabel("Number of Patients")
plt.xlabel("Date")
plt.xticks(dateIndex, dates)
plt.title("Increasing Rate of Flu Virus in Patients")

plt.show()
