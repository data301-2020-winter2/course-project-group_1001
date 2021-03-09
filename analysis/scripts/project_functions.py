def loaddata():
    data = pd.read_csv('../../data/raw/olympic_dataset.csv', low_memory=False, encoding = 'utf-8')
    return data

def teamMedals (data, team):
    newdata=data[data['Team'] == team].dropna()
    return newdata

def teamAthletes(data, team):
    newdata=data[data['Team'] == team]
    return newdata

def athletesMedals(data):
    newdata=data.dropna()
    return newdata

def medalsYear(data, year):
    newdata=data[data['Year'] == year].dropna()
    return newdata

def athletesYear(data, year):
    newdata=data[data['Year'] == year]
    return newdata

def teamMedalsYear(data, team, year):
    newdata=data[(data['Team'] == team) & (data[('Year')] == year)].dropna()
    return newdata

def teamAthletesYear(data, team, year):
    newdata=data[(data['Team'] == team) & (data[('Year')] == year)]
    return newdata
