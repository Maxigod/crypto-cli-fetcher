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