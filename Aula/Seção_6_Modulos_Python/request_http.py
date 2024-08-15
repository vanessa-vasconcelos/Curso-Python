# requests para requisições HTTP
# live - https://www.youtube.com/watch?v=Qd8JT0bnJGs
import requests

# http:// -> 80 = o site já carrega na 80
# https:// -> 443 = o site já carrega na porta 443
url = 'http://localhost:3333/'
response = requests.get(url) # resposta recebe a requisição.leitura da url

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)