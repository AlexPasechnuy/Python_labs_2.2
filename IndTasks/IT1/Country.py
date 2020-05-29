from IndTasks.IT1.City import City

class Country:
    def __init__(self, name):
        self.name = name
        self.cities = []

    def addCities(self, dict):
        for key, value in dict.items():
            self.addCity(key, value)

    def addCity(self, cityName, streetsNum):
        city = City(cityName, streetsNum)
        self.cities.append(city)

    def createCityDict(self):
        cityDict = dict()
        for i in self.cities:
            cityDict[i.name] = i.streetsnum
        return cityDict