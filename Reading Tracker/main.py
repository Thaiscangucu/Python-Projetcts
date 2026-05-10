import requests 
from datetime import datetime

USERNAME = "thaiscangucu"
TOKEN = "jbfjjtmds124"
GRAPH_ID = "graph2"
GRAPH_URL = "https://pixe.la/v1/users/thaiscangucu/graphs/graph2.html"

# Pixaela
pixaela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixaela_endpoint, json=user_params)
# print(response.text)

# Graph
graph_endpoint = f"{pixaela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "id": "graph2",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
}
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# choice = input("1. \n2.Update a pixel\n3. Delete a pixel.")

def calc_paginas():
    last_page = int(input("Última página lida: "))
    if last_page <= 0:
        return
    first_page = int(input("Primeira página lida: "))
    total_pages = last_page - first_page
    print(f"Total de páginas lidas: {total_pages}")

def adicionar_pixel():
    today = datetime.now()
    pixel_endpoint = f"{pixaela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("Quantas páginas você leu hoje? "),
    }
    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
    print(response.text)

def editar_pixel():
    data = input("Digite a data do pixel que deseja editar (formato YYYYMMDD): ")
    nova_qtd = input("Nova quantidade de páginas: ")
    update_endpoint = f"{pixaela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{data}"
    new_pixel_data = {
        "quantity": nova_qtd
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)

def deletar_pixel():
    data = input("Digite a data do pixel que deseja deletar (formato YYYYMMDD): ")
    delete_endpoint = f"{pixaela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{data}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar pixel")
        print("2 - Editar pixel")
        print("3 - Deletar pixel")
        print("4 - Calcular páginas")
        print("5 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_pixel()
        elif opcao == "2":
            editar_pixel()
        elif opcao == "3":
            deletar_pixel()
        elif opcao == "4":
            calc_paginas()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# calc_paginas()
menu()