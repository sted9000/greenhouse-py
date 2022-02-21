import json
import csv

'''
Functions to combine json files into a singular dictionary and save that dictionary as a usable csv file. 
'''


def create_applications_csv():
    f = open('./json/clean/apps.json')
    apps = json.load(f)
    f = open('./json/clean/offers.json')
    offers = json.load(f)

    combined_apps = []
    for app in apps:
        if app['id'] in [x['application_id'] for x in offers]:
            app['offered'] = True
            combined_apps.append(app)
        else:
            app['offered'] = False
            combined_apps.append(app)

    fields = combined_apps[0].keys()
    with open('./csv/apps.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(combined_apps)


def create_jobs_csv():
    f = open('./json/clean/jobs.json')
    jobs = json.load(f)
    f = open('./json/clean/job_stages.json')
    job_stages = json.load(f)

    combined_jobs = []
    for job in jobs:
        counter = 0
        combined_job = job
        for job_stage in job_stages:
            if job['id'] == job_stage['job_id']:
                combined_job[f'stage_{counter}'] = job_stage['name']
                counter += 1
        combined_jobs.append(combined_job)

    # normalize the keys
    length_of_dict = [len(x.keys()) for x in combined_jobs]
    elements_of_longest_job = max(length_of_dict)
    index_of_longest_job = length_of_dict.index(elements_of_longest_job)
    keys_of_longest_job = combined_jobs[index_of_longest_job].keys()
    normalized_jobs = []
    for j in combined_jobs:
        nj = {}
        for key in keys_of_longest_job:
            if key in j:
                nj[key] = j[key]
            else:
                nj[key] = None
        normalized_jobs.append(nj)

    with open('./csv/jobs.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys_of_longest_job)
        writer.writeheader()
        writer.writerows(normalized_jobs)
