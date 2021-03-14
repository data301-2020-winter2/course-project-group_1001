def loaddata():
    data = pd.read_csv('../../data/raw/olympic_dataset.csv', low_memory=False, encoding = 'utf-8')
    return data

def nocMedals (data, noc):
    newdata=data[data['NOC']== team].dropna()
    return newdata

def nocathletes(data, noc):
    newdata=data[data['NOC'] == team]
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

def nocMedalsYear(data, NOC, year):
    newdata=data[(data['NOC'] == team) & (data[('Year')] == year)].dropna()
    return newdata

def nocAthletesYear(data, NOC, year):
    newdata=data[(data['NOC'] == team) & (data[('Year')] == year)]
    return newdata
                
def getnoc(data, cname):
    row=data[(data['Team'] == country)]
    noc=row['NOC'].iloc[0]
    return noc
