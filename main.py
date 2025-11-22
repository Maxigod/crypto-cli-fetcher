import sys
from src.api import get_crypto_data
from src.utils import format_message
import argparse
import logging


# Los logs se guardarán en un archivo y también se mostrarán en consola
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("execution.log"), # guardar en archivo
        logging.StreamHandler(sys.stdout) # mostrar en consola
    ]
)

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

    parser.add_argument(
        '--save', '-s',
        type=str,
        help='Nombre del archivo JSON para guardar el resultado (ej: data.json)'
    )

    return parser.parse_args()


def run():
    """
    Función principal que orquesta el flujo del programa.
    """
    args = parse_arguments()
    coin_id = args.coin
    
    logging.info(f"Consultando datos para: {coin_id}")
    
    # 1. Extract
    data = get_crypto_data(coin_id)
    
    if not data:
        logging.error(f"Error: No se encontraron datos para '{coin_id}'. Verifica el ID.")
        sys.exit(1) # Salimos con código de error

    if args.save:
        # Pasamos el nombre del archivo que el usuario escribió
        from src.utils import save_to_json
        save_to_json(data, args.save)

    if args.raw:
        print(data)    
    else:
        # 2. Transform / Format
        report = format_message(data)
        
        # 3. Load / Show
        print(report)


if __name__ == "__main__":
    run()