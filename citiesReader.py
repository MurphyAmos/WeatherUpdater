import csv



class pullCityData:
    global stateName, cityName, countyName
    stateName =str(input("Name Of State: "))
    cityName =str(input("\tCity: "))
    countyName =str(input("\tCounty:"))
 
    def returnCity():
        return cityName

    global latnLong
    def readnReturn():  
        reader = csv.reader(open('us_cities.csv','r'))
        for i in reader:
            stateIndex = i[2]
            cityIndex = i[3]
            countyIndex = i[4]
            lata = i[5]
            longa =i[6]
            if(stateIndex.lower() == stateName.lower()) and (cityIndex.lower() == cityName.lower()) and(countyIndex.lower() == countyName.lower()):
                latnLong = (f"{float(lata)},{float(longa)}")
                return(latnLong)
    
