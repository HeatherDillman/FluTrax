import easygui
import datetime
import pandas as pd


def validate_date(year: str, month: str, day: str):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        datetime.datetime(year, month, day)
        return 2000 < year <= 2020
    except ValueError:
        return False


def update_info():
    title = "Trend of Increasing Rate of FLu Hospitalizations For Patients"

    # Show the country map

    # Update data
    msg = "Do you want to update the data?"

    if easygui.ynbox(msg, title):
        states_df = pd.read_csv('us_states.csv')
        states = {state: abbr for state, abbr in states_df.to_numpy()}
        choices = states.keys()
        filename = 'data.csv'
        update_data = pd.read_csv(filename)
        while True:
            choice = easygui.choicebox("Please choose the state you want to update: ", title, list(choices))

            date_input = easygui.enterbox("Please enter the date (mm/dd/yyyy): ")
            month, day, year, *_ = date_input.split('/')
            while not validate_date(year, month, day):
                date_input = easygui.enterbox("Please enter the date (mm/dd/yyyy): ")
                year, month, day, *_ = date_input.split('/')
            year, month, day = [int(s) for s in (year, month, day)]

            number_of_patients_input = -1
            while int(number_of_patients_input) < 0:
                number_of_patients_input = easygui.enterbox("Enter the number of patients: ")
            # Update the data
            conditional = (update_data['Year'] == year) & (update_data['Month'] == month) & \
                          (update_data['Day'] == day) & (update_data['State'] == states[choice])
            if update_data.loc[conditional].empty:
                update_data = update_data.append(
                    {'Year': year, 'Month': month, 'Day': day, 'State': states[choice],
                     'Population': int(number_of_patients_input)}
                    , ignore_index=True)
            else:
                update_data.loc[conditional, 'Population'] = int(number_of_patients_input)

            # Give the warning
            if int(number_of_patients_input) < 100000:
                msg = "GET VACCINATED."
                title = "SUGGESTION:"
                easygui.msgbox(msg, title)
            elif int(number_of_patients_input) < 250000:
                msg = "TAKE ACTIONS EVERY DAY TO HELP STOP THE SPREAD OF GERMS."
                title = "REQUIRED:"
                easygui.msgbox(msg, title)
            else:
                msg = "NEED ANTIVIRAL MEDICATION TO TREAT FLU."
                title = "WARNING:"
                easygui.msgbox(msg, title)
            msg = "Do you want to continue?"
            if not easygui.ynbox(msg, title):
                break
        update_data.to_csv(filename, index=False)
