import easygui
import datetime
import pandas as pd

def validate_date(year: str, month: str, day: str):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False

if __name__ == '__main__':

    title = "Trend of Increasing Rate of FLu Hospitalizations For Patients"

    while True:

        states_df = pd.read_csv('us_states.csv')
        states = {abbr:state for state, abbr in states_df.to_numpy()}
        choices = states.values()
        choice = easygui.choicebox("Please choose the state you want to see: ", title, choices)

        easygui.msgbox()

        msg = "Do you want to update the data?"
        if easygui.ynbox(msg, title):
            pass
        else:
            exit(0)

        date_input = easygui.enterbox("Please enter the date (mm/dd/yyyy): ")

        month, day, year, *_ = date_input.split('/')
        while not validate_date(year, month, day):
            date_input = easygui.enterbox("Please enter the date (mm/dd/yyyy): ")
            year, month, day, *_ = date_input.split('/')

        numberOfPatientsInput = -1
        while int(numberOfPatientsInput) < 0:
            numberOfPatientsInput = easygui.enterbox("Enter the number of patients: ")

        if int(numberOfPatientsInput) < 100000:
            msg = "GET VACCINATED."
            title = "SUGGESTION:"
            easygui.msgbox(msg, title)
        elif int(numberOfPatientsInput) < 250000:
            msg = "TAKE ACTIONS EVERY DAY TO HELP STOP THE SPREAD OF GERMS."
            title = "REQUIRED:"
            easygui.msgbox(msg, title)
        else:
            msg = "NEED ANTIVIRAL MEDICATION TO TREAT FLU."
            title = "WARNING:"
            easygui.msgbox(msg, title)

        msg = "Do you want to continue?"
        if easygui.ynbox(msg, title):
            continue
        else:
            exit(0)

