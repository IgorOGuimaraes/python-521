
import requests

URL = 'https://gen-net.herokuapp.com/api/users/{}'

#put API
user_id = input('Inserir id usuário: ')

url_formatada = URL.format(user_id)

user_name = input('Informe nome do novo usuário: ')
user_email = input('Informe o Email do usuário: ')
user_pass = input('Inform a senha: ')

update_user = {
	"email": user_email,
	"name": user_name,
	"password": user_pass
}

response = requests.put(url_formatada, update_user)

if response.status_code == 200:
	print("Usuário atualizado com sucesso")
	print(response.json())
else:
	print("Erro ao atualizar o usuário")
	print(response.text())