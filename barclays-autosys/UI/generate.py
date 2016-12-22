
jil = []

with open('../Machine Description.txt', 'rb') as file:
    for row in file:
        if (not row.startswith('#')):
            jil.append(row.strip())

    jobs = []
    job_indices = []

    for i in range(len(jil)):
        if (jil[i].startswith('insert_job')):
            job_indices.append(i)
    jobs = []
    for i in range(len(job_indices) - 1):
        jobs.append(jil[job_indices[i]:job_indices[i + 1]])

    jobs.append(jil[job_indices[len(job_indices)-1]:])


def nodes():

    nodes = []

    for job in jobs:
        d = {}
        d['default'] = "10"
        d['isGroup'] = ""
        for line in job:
            if line.startswith('insert_job'):
                d['key'] = line.split(':')[1].strip()
            if line.startswith('box_name'):
                d['group'] = line.split(':')[1].strip()
            if line.startswith('job_type: box'):
                d['isGroup'] = "true"
                d['text'] = ""
            if line.startswith('default'):
                d['default'] = line.split(':')[1].strip()
        if (not d['isGroup'] == "true"):
            d['text'] = "%s (%s)" % (d['key'], d['default'])
            del d['isGroup']
        nodes.append(d)

    return nodes

def links():
    links = []

    for job in jobs:
        d = {}
        name = ""
        for line in job:
            
            if line.startswith('insert_job'):
                name = line.split(':')[1].strip()
            if line.startswith('condition'):
                d['to'] = name
                d['from'] = line.split('(')[1].split(')')[0]
        if (not d == {}):
            links.append(d)
           

    return links