
import requests

#post de um novo usuario
URL = 'https://gen-net.herokuapp.com/api/users/'

userName = input('Informe nome do novo usuário: ')
userEmail = input('Informe o Email do usuário: ')
userPass = input('Inform a senha: ')

jsonNewUser = {
	"email": userEmail,
	"name": userName,
	"password": userPass
}

response = requests.post(URL, jsonNewUser)

if response.status_code == 200:
	print("Usuário Salvo")
	print(response.json())
else:
	print("Erro, usuário não foi salvo")
	print(response.text())