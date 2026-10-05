import logging

# Configuração global do logging
logging.basicConfig(
    level=logging.INFO,  # Nível mínimo exibido (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato da mensagem
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato da data e hora
)
logger = logging.getLogger(__name__)
