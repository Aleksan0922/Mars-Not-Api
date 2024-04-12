from requests import post, get, delete
import datetime

print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/1').json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader':  '1',
                 'job':  'u',
                 'work_size':  24 * 7,
                 'collaborators':  '2, 3',
                 'start_date':  '2024-03-03 20:20:20',
                 'end_date':  '2024-03-03 20:20:21',
                 'is_finished':  False}).json())

print(post('http://localhost:5000/api/jobs/2',
           json={'team_leader':  '1',
                 'job':  'u',
                 'work_size':  24 * 7,
                 'collaborators':  '2, 3',
                 'start_date':  '2024-03-03 20:20:20',
                 'end_date':  '2024-03-03 20:20:58',
                 'is_finished':  False}).json())
print(get('http://localhost:5000/api/jobs').json())

print(delete('http://localhost:5000/api/jobs/2').json())


print(get('http://localhost:5000/api/jobs/1000').json())
print(get('http://localhost:5000/api/jobs/г').json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': '1',
                 'job': 'u',
                 'work_size': 24 * 7}).json())

print(delete('http://localhost:5000/api/jobs/10000').json())
print(delete('http://localhost:5000/api/jobs/н').json())

print(post('http://localhost:5000/api/jobs/2',
           json={'team_leader':  '1',
                 'job':  'u',
                 'work_size':  24 * 7,}).json())

print(post('http://localhost:5000/api/jobs/123431',
           json={'team_leader':  '1',
                 'job':  'u',
                 'work_size':  24 * 7,}).json())



