[![Python 3.6](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Greenhouse Data Analysis MVP
A python script to pull from Greenhouse's Harvest API and turn it in to a file for analysis in Excel. Specifically, the script creates two .csv files: 
- Applications: Containing all the companies applications and data about the application.
- Jobs: Containing all companies jobs ("roles") and data about them.

## Installation
Uses [this python library](https://github.com/alecraso/grnhse-api) as a helper for accessing GreenHouse's API:
- ```pip install grnhse-api```
- ```pip install six```

## Usage
1. Replace 'GREENHOUSE_API_KEY' with your greenhouse api key in main.py
2. Run ```python3 main.py```

The script runs three processes:
1. Pull all the data (applications, offers, jobs, job_stages) and save it as json.
2. Cleans the raw json and saves the cleaned json.
3. Combine the data in a way that makes for easier analysis and save in .csv files (app.csv, jobs.csv)

To change, comment out, or manipulate any of these steps, see main.py

## Future features
- Package for non-python users
- Only retrieve new data from the api using date as a search param
- Refactor utils/table function that combines jobs and job_stages
- Change the batch size for the api calls to the max (500) rather than the default (100)