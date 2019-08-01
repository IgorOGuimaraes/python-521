
import requests

URL = 'https://gen-net.herokuapp.com/api/users/{}'

#get sem filtro
response = requests.get(URL.format(''))
print(response.json())



#get com filtro
userId = input('Inserir id usuário: ')

URL_FORMATADA = URL.format(userId)
response = requests.get(URL_FORMATADA)

if response.status_code == 200:
	print("Usuário localizado")
	print(response.json())
else:
	print("Erro, usuário não existe")
	print(response.text())