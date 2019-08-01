
import requests

URL = 'https://gen-net.herokuapp.com/api/users/{}'


#search user for email
URL = 'https://gen-net.herokuapp.com/api/users/'

res = requests.get(URL)
users = res.json()

userEmail = input('Digite seu email: ')

for user in users:
	if user.get('email') == userEmail:
		print(user)