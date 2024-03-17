from requests import post, get, delete
import datetime

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())

print(post('http://localhost:5000/api/v2/users',
           json={'surname':  'Qwerty',
                 'name':  'Йцукен',
                 'age':  '33',
                 'position':  'who',
                 'speciality':  'idk',
                 'address':  'GdeToDaleko',
                 'email':  '1@34.5',
                 'hashed_password':  'u',
                 'modified_date':  'now'}).json())

print(delete('http://localhost:5000/api/v2/users/2').json())


print(get('http://localhost:5000/api/v2/users/1000').json())
print(get('http://localhost:5000/api/v2/users/у').json())

print(post('http://localhost:5000/api/v2/users',
           json={'surname':  'Qwerty',
                 'name':  'Йцукен',
                 'hashed_password':  'u',
                 'modified_date':  'now'}).json())

print(delete('http://localhost:5000/api/v2/users/10000').json())
print(delete('http://localhost:5000/api/v2/users/н').json())