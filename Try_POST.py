import requests

url = 'http://localhost:8088/post'
tila = 3
r = None
if tila == 1:
    p_load = {'username': 'Olivia', 'password': '123'}
elif tila == 2:
    p_load = "Tavallinen merkkijono"
elif tila == 3:
    x = {'id': 1, 'name': 'ram sharma'}
    r = requests.post(url, json=x)
    print(f'request r {r.text}')
    exit(0)

if not r:
    r = requests.post(url, data=p_load)
print(r.text)
