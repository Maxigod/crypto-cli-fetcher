# 📈 Crypto CLI Fetcher

Una herramienta de línea de comandos (CLI) construida en Python para extraer precios de criptomonedas en tiempo real usando la API de CoinPaprika. Diseñada con principios de Ingeniería de Datos: modularidad, manejo de errores y logging.

## 🚀 Funcionalidades
- **Extracción en tiempo real:** Consulta precios de cualquier criptomoneda (Bitcoin, Ethereum, Polkadot, etc.).
- **Modo Raw:** Opción para inspeccionar la respuesta JSON cruda de la API.
- **Exportación de Datos:** Capacidad de guardar los resultados en archivos JSON locales.
- **Robustez:** Sistema de logging integrado para monitoreo y depuración.

## 🛠️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Maxigod/crypto-cli-fetcher.git](https://github.com/Maxigod/crypto-cli-fetcher.git)
   cd crypto-cli-fetcher

2. **Crear y activar el entorno virtual**
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate

3. **Instalar dependencias**
    ```bash
    pip install -r requirements.txt

## Uso
**Consultar precio del bitcoin**
    ```bash
    python main.py --coin btc-bitcoin

**Guardar el resultado en un archivo JSON**
    ```bash
    python main.py -c eth-ethereum --save resultado.json

**Ver la ayuda completa**
    ```bash
    python main.py --help

## Estructura del proyecto
* src/: Código fuente modular (API client y utilidades).
* main.py: Punto de entrada de la aplicación (CLI).
* execution.log: Registro de actividad y errores (se genera al ejecutar).