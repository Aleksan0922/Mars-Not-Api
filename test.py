from requests import post, get


print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/1').json())

print(get('http://localhost:5000/api/jobs/9000').json())

print(get('http://localhost:5000/api/jobs/u').json())