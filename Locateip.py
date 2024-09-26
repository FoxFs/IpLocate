import requests
import folium

def localizar_por_ip(ip=None):
    # Se nenhum IP for fornecido, ele usa o IP da máquina local (consulta automática)
    url = f'https://ipinfo.io/{ip}/json' if ip else 'https://ipinfo.io/json'
    
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        localizacao = dados.get('loc', None)
        
        if localizacao:
            lat, lng = localizacao.split(',')
            print(f"Latitude: {lat}, Longitude: {lng}")
            mymap = folium.Map(location=[lat, lng], zoom_start=12)
            folium.Marker([lat, lng], popup=localizacao).add_to(mymap)
            mymap.save("mylocation.html")
            print("mapa feito com sucesso!!")

        else:
            print("Localização não encontrada para o IP informado.")
    else:
        print(f"Erro ao acessar o serviço: {response.status_code}")

# Exemplo de uso
ip_personalizado = input("Digite o IP para localizar (ou deixe vazio para usar seu IP atual): ")
localizar_por_ip(ip_personalizado)