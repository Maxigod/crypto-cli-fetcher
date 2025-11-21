from typing import Dict, Any


def format_message(data: Dict[str, Any]) -> str:
	"""
	Extrae los datos relevantes y formatea el mensaje final.
	"""
	name = data.get('name', 'Desconocido')
	symbol = data.get('symbol', '???')
	price = data['quotes']['USD']['price']

	return f"{name} ({symbol}): ${price:,.2f} USD"