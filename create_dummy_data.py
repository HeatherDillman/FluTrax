import pandas as pd
from random import randint

if __name__ == '__main__':
    data = []
    dates = ['2/10/2020', '2/11/2020', '2/12/2020', '2/13/2020', '2/14/2020', '2/15/2020']
    states = list(pd.read_csv('us_states.csv')['Abbreviation'].to_numpy())
    for state in states:
        pop = randint(15000, 25000)
        for date in dates:
            month, day, year = [int(s) for s in date.split('/')]
            pop = pop + randint(-250, 2500)
            data.append((year, month, day, state, pop))

    df = pd.DataFrame(data, columns=['Year', 'Month', 'Day', 'State', 'Population'])
    df.to_csv('data.csv', index=False)
