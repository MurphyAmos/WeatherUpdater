####THIS IS MY PROFESSIONAL DISPLAY AND DOES NOT WORK UNLESS YOU HAVE YOUR OWN TWILIO ACCOUNT, AND INFO
import json, requests, time
from twilio.rest import Client
from citiesReader import pullCityData

class MessageForecast:
    pullCityObj = pullCityData
    global latLong
    latLong = pullCityObj.readnReturn()    

    def forecastPull():
        def pullGrid(latNlong):
	    #pulling grid points and returning them
            gridInfo=requests.get(f"https://api.weather.gov/points/{latNlong}")
            gridInfoJson = json.loads(gridInfo.text)
            gridXPoint=gridInfoJson["properties"]["gridX"]
            gridYPoint=gridInfoJson["properties"]["gridY"]
            gridXnY = (f"{gridXPoint},{gridYPoint}")
            return gridXnY    
        gridPoints =pullGrid(latLong)
        ####start of forecastPull()
        #request the JSON; grid and office are static for Houston texas
        forecastInfo=requests.get(f"https://api.weather.gov/gridpoints/HGX/{gridPoints}/forecast")
        #turn it in to text
        forecastInfoJson = json.loads(forecastInfo.text)
		#might make variables and hold them or just directly pull them in text message sender thingy	

		###in this half of the function i will hold the info in some global variables
        global temperatureAfternoon
        global shortForecastAfternoon
        global percipChance

		#here we are just using json and oulling the temp,short forecast, and rain%
		#yes this is hard to read, but i dont really care as it wont change 
        temperatureAfternoon = forecastInfoJson["properties"]["periods"][0]["temperature"]
        shortForecastAfternoon= forecastInfoJson["properties"]["periods"][0]["shortForecast"]
        percipChance = forecastInfoJson["properties"]["periods"][0]["probabilityOfPrecipitation"]["value"]
        ####end of forecastPull()
    def sendText():  
    ####start of sendText()
		#putting the phone numbers into variables allowing for easyyyyyy change
        fromNumber = "+1[TWILIO_FROM_NUMBER]"			
        toNumber = "+1[TWILIO_TO_NUMBER]"

		###this will be used as a text to send this is the outline it works boom pow
        account_sid = "[TWILIO SID]"
        auth_token = "[TWILIO_API_KEY/TOKEN]"
        client = Client(account_sid, auth_token)

		###the next half will be me making and sending the text itself!

        message = client.messages.create(
        from_=f"{fromNumber}",
        body = f"Hi! The forecast for the day is:\n Temperature: {temperatureAfternoon}°F \n Rain Probibility in area is: {percipChance}% \n Weather Report says: {shortForecastAfternoon}",
        to=f"{toNumber}")
 	####end of sendText()
	####end of functions 


####Run Sequence
####start of run sequence	
	#i put this in forever while loop
    while True:
        forecastPull()
	sendText()
	###this loop is infinite will make it leave loop, i will make input detection so will leave on command 
        time.sleep((60*60)*24)#24hours
	
####end of Run sequence
