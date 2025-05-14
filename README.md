This project fetches weather forecast data from the U.S. National Weather Service and sends it via SMS using Twilio. It requires a user to input a U.S. city, county, and state to pull localized weather data.

Files Overview
citiesReader.py
Handles city data extraction from a CSV file containing U.S. city info.

Key Components:

User Input: Prompts for state, city, and county.

readnReturn() Method: Parses us_cities.csv to match user input and return the corresponding latitude and longitude.

Make sure the us_cities.csv file has state, city, and county data in the expected column positions (indexes 2, 3, 4 for state, city, county, and 5, 6 for lat/long).

messageForecast.py Fetches weather forecasts from the National Weather Service API and sends a text message via Twilio with the daily forecast.

Key Components:
  forecastPull() Method: Uses latitude/longitude to pull forecast data (temperature, precipitation, summary).
  
  sendText() Method: Sends the forecast via Twilio SMS.
  
  Run Loop: Runs every 24 hours indefinitely, sending updates daily.
