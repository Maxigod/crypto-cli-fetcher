import requests


def obtener_precio_bitcoin_hoy():
	url = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"
	try:
		response = requests.get(url)
		if response.status_code == 200:
			data = response.json()
			print("El precio del Bitcoin es: $", data["quotes"]["USD"]["price"])
		else:
			print("Sin éxito al conectar con la API. Código de estatus:", response.status_code)
	except Exception as e:
		print("Hubo un error al tratar de llamar a la API")


if __name__ == "__main__":
	obtener_precio_bitcoin_hoy()