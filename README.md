# Greenhouse Data Analysis
## General
Pull data from Greenhouse's Harvest API and turn it in to a file for analysis in Excel. Specifically, the script creates two .csv files: 
- Applications: Containing all the companies applications and data about the application.
- Jobs: Containing all companies jobs ("roles") and data about them.

## Dependencies
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

## Possible Future features
- Only retrieve new data from the api using date as a search param
- Change the batch size for the api calls to the max (500) rather than the default (100)