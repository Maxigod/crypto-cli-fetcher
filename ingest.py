import requests
from typing import Dict, Any, Optional


def get_crypto_data(coin_id: str) -> Optional[Dict[str, Any]]:
	"""
	Consulta la API de CoinPaprika para obtener datos de una moneda.
	"""
	base_url = "https://api.coinpaprika.com/v1/tickers"
	url = f"{base_url}/{coin_id}"

	try:
		response = requests.get(url)
		response.raise_for_status() # Lanza error si no es 200 OK
		return response.json()
	except requests.exceptions.RequestException as e:
		print(f"Error de red: {e}")
		return None

def format_message(data: Dict[str, Any]) -> str:
	"""
	Extrae los datos relevantes y formatea el mensaje final.
	"""
	name = data.get('name', 'Desconocido')
	symbol = data.get('symbol', '???')
	price = data['quotes']['USD']['price']

	return f"{name} ({symbol}): ${price:,.2f} USD"


if __name__ == "__main__":
	coin_id = 'eth-ethereum'
	
	raw_data = get_crypto_data(coin_id)

	if raw_data:
		mensaje = format_message(raw_data)
		print("--------------------")
		print(mensaje)
		print("--------------------")