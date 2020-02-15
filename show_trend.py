import pandas as pd
import matplotlib.pyplot as plt
import easygui


def encode_date(row):
    return f"{row['Month']}/{row['Day']}/{row['Year']}" if (row['Index'] % 3 == 0) else ''


def show_trend():
    title = "Trend of Increasing Rate of Flu Hospitalizations For Patients"
    filename = 'data.csv'
    data = pd.read_csv(filename)
    dateIndex = list(range(len("{}/{}/{}".format(data['Month'], data['Day'], data['Year']))))
    states_df = pd.read_csv('us_states.csv')
    states = {state: abbr for state, abbr in states_df.to_numpy()}
    choices = states.keys()
    choice = easygui.choicebox("Please choose the state you want to update: ", title, list(choices))

    data = data.loc[data['State'] == states[choice]]
    data['Index'] = data.index
    plt.ylim(data['Population'].min() * 0.8, data['Population'].max() * 1.2)

    plt.plot(data['Population'].to_numpy(), marker="o")
    plt.ylabel("Number of Patients")
    plt.xlabel("Date")
    print(data['Population'].count())
    plt.xticks(range(data.count()[0]), data.apply(encode_date, axis=1).to_numpy())
    # plt.xticks(dateIndex, "{}/{}/{}".format(data['Month'], data['Day'], data['Year']))
    plt.title("Trend of Increasing Rate of Flu Hospitalizations For Patients")

    plt.show()
