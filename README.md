TO USE THIS YOU MUST HAVE A TWILIO ACCOUNT AND SET IT UP. A LINK WILL BE PUT BELOW FOR ACCOUNT SET UP
TWILIO : https://www.twilio.com/en-us


Weather.Gov Api Explanation:

  This program takes the weather from the weather.gov API. To get this data we take the location of whatever the user would like to look at!
If you would like to change it, you must first locate the grid points of said city by Using this endpoint 'https://api.weather.gov/points/{latitude},{longitude}' to request the grid points of your city via latitude and longitude. 
After this you can do 'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast' to request/pull the data with the grid points you have just returned. 
