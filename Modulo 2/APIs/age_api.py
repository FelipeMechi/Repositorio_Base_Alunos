import requests

nome = input("Digite o nome da pessoa: ").strip()

url = f'https://api.agify.io/?name={nome}'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f'Nome: {dados['name']}')
    print(f'Idade estimada: {dados['age']} anos')
    print(f'Número de registros analisados: {dados['count']}')
else:
    print(f'Erro ao acessar a API: {response.status_code}')