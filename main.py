import sys
from src.api import get_crypto_data
from src.utils import format_message
import argparse


def parse_arguments():
    """
    Configura y procesa los argumentos de la línea de comandos.
    """
    parser = argparse.ArgumentParser(description="Herramienta CLI para obtener precios de criptomonedas.")

    # Argumento obligatorio, el ID de la moneda.
    parser.add_argument(
        '--coin', '-c',
        type=str,
        required=True,
        help='El ID de la moneda en CoinPaprika (ej: btc-bitcoin, eth-ethereum)'
    )

    # Argumento opcional (Flag): Modo 'Raw' para ver el JSON crudo
    parser.add_argument(
        '--raw', '-r',
        action='store_true',
        help="Muestra la respuesta completa JSON sin formato."
    )

    return parser.parse_args()

def run():
    """
    Función principal que orquesta el flujo del programa.
    """
    args = parse_arguments()
    coin_id = args.coin
    
    print(f"🚀 Consultando datos para: {coin_id}...")
    
    # 1. Extract
    data = get_crypto_data(coin_id)
    
    if not data:
        print("Error: No se encontraron datos para '{coin_id}'. Verifica el ID.")
        sys.exit(1) # Salimos con código de error

    if args.raw:
        print(data)    
    else:
        # 2. Transform / Format
        report = format_message(data)
        
        # 3. Load / Show
        print(report)


if __name__ == "__main__":
    run()