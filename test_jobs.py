from requests import post, get, delete
import datetime

print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/1').json())

print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader':  '1',
                 'job':  'u',
                 'work_size':  24 * 7,
                 'collaborators':  '2, 3',
                 'start_date':  '12.12.12:12',
                 'end_date':  'Kogdato',
                 'is_finished':  False}).json())

print(delete('http://localhost:5000/api/v2/jobs/2').json())


print(get('http://localhost:5000/api/v2/jobs/1000').json())
print(get('http://localhost:5000/api/v2/jobs/г').json())

print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': '1',
                 'job': 'u',
                 'work_size': 24 * 7}).json())

print(delete('http://localhost:5000/api/v2/jobs/10000').json())
print(delete('http://localhost:5000/api/v2/jobs/н').json())