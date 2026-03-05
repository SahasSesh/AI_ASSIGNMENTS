# Real-Time AQI Tracker Using OpenWeatherMap API

## Overview

This project implements a Simple Reflex AI Agent that evaluates real-time air pollution data and determines the Air Quality Index (AQI) using the official Indian AQI methodology (0–500 scale). The system retrieves pollutant concentration values from the OpenWeatherMap API and applies predefined condition–action rules to classify air quality into standard health categories.

## Agent Design (Simple Reflex Model)

The system is modeled as a Simple Reflex Agent, which operates using predefined condition–action rules based only on the current percept.

- **Environment:** Real-world air quality conditions  
- **Percept:** Pollutant concentration values retrieved from the API (PM2.5, PM10, NO₂, etc.)  
- **Condition–Action Rules:** AQI threshold ranges defined by Indian AQI standards  
- **Action:** Display the computed AQI value and its corresponding health category  

The agent does not store past pollution values and does not adapt or learn over time. It reacts solely to the current input data, satisfying the characteristics of a simple reflex agent.

## Features

- Fetches real-time air pollution data using the OpenWeatherMap API  
- Computes AQI sub-indices for individual pollutants  
- Determines overall AQI using the maximum sub-index rule (Indian AQI standard)  
- Classifies air quality into health categories  
- Displays AQI results with color-coded output

## Technologies Used

- Python  
- Requests library  
- OpenWeatherMap API  
- Google Colab / Jupyter Notebook

## Installation & Usage

1. Clone the repository:
   git clone https://github.com/yourusername/aqi-checker.git
2. Open the .ipynb notebook file from the repository.
3. Run the notebook in:
   - Google Colab (recommended), or
   - Jupyter Notebook locally
4. If running locally, install the required dependency:
   pip install requests
5. Insert your OpenWeatherMap API key in the placeholder provided in the code before running the cells.

## How It Works

1. The user inputs a city name.

2. The system finds that lat and long of the city if it is valid and sends a request to the OpenWeatherMap API to retrieve current air pollution data.

3. The API returns pollutant concentration values in JSON format.

4. Each pollutant (PM2.5, PM10, NO₂, etc.) is evaluated using predefined AQI threshold rules based on Indian AQI standards.

5. A sub-index is calculated for each pollutant.

6. The overall AQI is determined by selecting the maximum sub-index value, as per Indian AQI methodology.

7. The final AQI value is classified into a health category and displayed using color-coded output.

## AQI Classification (Indian Standard)

| AQI Range | Category       | Color        |
|------------|---------------|--------------|
| 0–50       | Good          | Dark Green   |
| 51–100     | Satisfactory  | Light Green  |
| 101–200    | Moderate      | Yellow       |
| 201–300    | Poor          | Orange       |
| 301–400    | Very Poor     | Red          |
| 401–500    | Severe        | Maroon       |
