import json

'''
These functions take json files (saved as is from the Greenhouse API)
and cleans them into only the information that we are interested it.
'''


def clean_apps():
    f = open('./json/raw/apps.json')
    apps = json.load(f)
    cleaned_apps = []
    for app in apps:
        clean_app = {}
        clean_app['id'] = app['id']
        clean_app['candidate_id'] = app['candidate_id']
        clean_app['prospect'] = app['prospect']
        clean_app['applied_at'] = app['applied_at']
        clean_app['job_name'] = app['jobs'][0]['name'] if app['jobs'] else None
        clean_app['job_id'] = app['jobs'][0]['id'] if app['jobs'] else None
        clean_app['status'] = app['status']
        clean_app['current_stage_name'] = app['current_stage']['name'] if app['current_stage'] else None
        clean_app['current_stage_id'] = app['current_stage']['id'] if app['current_stage'] else None
        cleaned_apps.append(clean_app)

    with open('./json/clean/apps.json', 'w') as f:
        json.dump(cleaned_apps, f)


def clean_offers():
    f = open('./json/raw/offers.json')
    offers = json.load(f)
    cleaned_offers = []
    for offer in offers:
        clean_offer = {'application_id': offer['application_id']}
        cleaned_offers.append(clean_offer)
    with open('./json/clean/offers.json', 'w') as f:
        json.dump(cleaned_offers, f)


def clean_jobs():
    f = open('./json/raw/jobs.json')
    jobs = json.load(f)
    cleaned_jobs = []
    for job in jobs:
        clean_job = {}
        clean_job['id'] = job['id']
        clean_job['name'] = job['name']
        clean_job['status'] = job['status']
        clean_job['opened_at'] = job['opened_at']
        clean_job['department'] = job['departments'][0]['name'] if job['departments'][0] is not None else 'None'
        offices = len(job['offices'])
        if offices == 0:
            clean_job['office_0'] = 'None'
            clean_job['office_1'] = 'None'
            clean_job['office_2'] = 'None'
        elif offices == 1:
            clean_job['office_0'] = job['offices'][0]['name']
            clean_job['office_1'] = 'None'
            clean_job['office_2'] = 'None'
        elif offices == 2:
            clean_job['office_0'] = job['offices'][0]['name']
            clean_job['office_1'] = job['offices'][1]['name']
            clean_job['office_2'] = 'None'
        else:
            clean_job['office_0'] = job['offices'][0]['name']
            clean_job['office_1'] = job['offices'][1]['name']
            clean_job['office_2'] = job['offices'][2]['name']

        clean_job['number_of_openings'] = len([d for d in job['openings'] if d['status'] in 'open'])

        if job['custom_fields']['employment_type']:
            clean_job['employment_type'] = job['custom_fields']['employment_type']
        else:
            clean_job['employment_type'] = 'None'

        cleaned_jobs.append(clean_job)

    with open('./json/clean/jobs.json', 'w') as f:
        json.dump(cleaned_jobs, f)


def clean_job_stages():
    f = open('./json/raw/job_stages.json')
    job_stages = json.load(f)
    cleaned_job_stages = []
    for job_stage in job_stages:
        clean_job_stage = {'id': job_stage['id'],
                           'name': job_stage['name'],
                           'job_id': job_stage['job_id'],
                           'priority': job_stage['priority']
                           }
        cleaned_job_stages.append(clean_job_stage)

    with open('./json/clean/job_stages.json', 'w') as f:
        json.dump(cleaned_job_stages, f)
