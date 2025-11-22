import requests
from typing import Dict, Any, Optional
import logging


def get_crypto_data(coin_id: str) -> Optional[Dict[str, Any]]:
	"""
	Consulta la API de CoinPaprika para obtener datos de una moneda.
	"""
	base_url = "https://api.coinpaprika.com/v1/tickers"
	url = f"{base_url}/{coin_id}"

	try:
		logging.debug(f"Consultando URL: {url}")
		response = requests.get(url)
		response.raise_for_status() # Lanza error si no es 200 OK
		logging.info("Datos descargados correctamente de la API.")
		return response.json()
	except requests.exceptions.HTTPError as e:
		# Si es un error 404, es un error del cliente (la moneda no existe)
		if response.status_code == 404:
			logging.warning(f"Moneda {coin_id} no encontrada en CoinPaprika.")
		else:
			logging.error(f"Error HTTP: {e}")
		return None
	except requests.exceptions.RequestException as e:
		logging.critical(f"Error CRITICO de conexion: {e}")
		return None