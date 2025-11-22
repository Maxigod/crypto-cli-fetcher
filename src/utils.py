import json
from typing import Dict, Any
import logging


def format_message(data: Dict[str, Any]) -> str:
	"""
	Extrae los datos relevantes y formatea el mensaje final.
	"""
	name = data.get('name', 'Desconocido')
	symbol = data.get('symbol', '???')
	price = data['quotes']['USD']['price']

	return f"{name} ({symbol}): ${price:,.2f} USD"


def save_to_json(data: Dict[str, Any], filename: str):
	"""
	Guarda los datos en un archivo JSON local.
	"""
	try:
		with open(filename, 'w', encoding='utf-8') as f:
			json.dump(data, f, indent=4)
			logging.info(f"Datos guardados exitosamente en {filename}")
	except IOError as e:
		logging.error(f"Error al escribir el archivo: {e}")