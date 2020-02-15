import easygui
import datetime
import pandas as pd
import FluTrax


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

    # Show the country map

    # Update data
    msg = "Do you want to update the data?"

    if easygui.ynbox(msg, title):
        while True:
            states_df = pd.read_csv('us_states.csv')
            states = {state: abbr for state, abbr in states_df.to_numpy()}
            choices = states.keys()
            choice = easygui.choicebox("Please choose the state you want to update: ", title, choices)

            date_input = easygui.enterbox("Please enter the date (mm/dd/yyyy): ")

            month, day, year, *_ = date_input.split('/')
            while not validate_date(year, month, day):
                date_input = easygui.enterbox("Please enter the date (mm/dd/yyyy): ")
                year, month, day, *_ = date_input.split('/')

            numberOfPatientsInput = -1
            while int(numberOfPatientsInput) < 0:
                numberOfPatientsInput = easygui.enterbox("Enter the increasing number of patients: ")
                # Update the data
                update_data = pd.read_csv('data.csv')
                if not update_data.loc[
                    (update_data['Year'] == year) & (update_data['Month'] == month) & (update_data['Day'] == day) & (
                            states[choice] == update_data['State'])].empty:
                    update_data['Population'] += numberOfPatientsInput

                # Give the warning
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
                pass
                # Return to the main page

    # Draw the line chart
    # while True:
