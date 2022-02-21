from grnhse import Harvest
from utils.clean import *
from utils.table import *

api_key = 'GREENHOUSE_API_KEY'
hvst = Harvest(api_key)

'''
First pull all the data we need and save them in json
1. All applications (currently only getting 1,000 for testing)
2. All offers made
3. All jobs
4. All job_stages
'''
# applications
apps = hvst.applications
all_apps = apps.get()
while apps.records_remaining:
    all_apps.extend(apps.get_next())
with open('json/raw/apps.json', 'w') as f:
    json.dump(all_apps, f)

# offers
offers = hvst.offers
all_offers = offers.get()
while offers.records_remaining:
    all_offers.extend(offers.get_next())
with open('json/raw/offers.json', 'w') as f:
    json.dump(all_offers, f)

# jobs postings
jobs = hvst.jobs
all_jobs = jobs.get()
while jobs.records_remaining:
    all_jobs.extend(jobs.get_next())
with open('json/raw/jobs.json', 'w') as f:
    json.dump(all_jobs, f)

# job_stages
job_stages = hvst.job_stages
all_job_stages = job_stages.get()
while job_stages.records_remaining:
    all_job_stages.extend(job_stages.get_next())
with open('json/raw/job_stages.json', 'w') as f:
    json.dump(all_job_stages, f)

'''
Next we clean the data as needed
'''
# applications
clean_apps()

# offers
clean_offers()

# jobs
clean_jobs()

# job_stages
clean_job_stages()


'''
And finally, we combine the data as we wanted and save as csv
'''
# applications
create_applications_csv()

# jobs
create_jobs_csv()
