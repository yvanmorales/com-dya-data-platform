import logging
import requests
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger(__name__)

class RestAPIConnector:
    """Conector robusto para ingesta de fuentes externas hacia la Capa Bronze."""
    
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        self.headers = headers or {"Content-Type": "application/json"}

    def fetch_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        try:
            logger.info(f"Iniciando solicitud GET a: {url}")
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            response.raise_for_status()
            logger.info("Datos obtenidos exitosamente de la fuente.")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error crítico al conectar con la API externa: {e}")
            raise