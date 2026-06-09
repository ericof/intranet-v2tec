from pathlib import Path
from v2tec.intranet import PACKAGE_NAME

import logging
import os


def get_logger() -> logging.Logger:
    """Retorna um logger configurado para o pacote."""
    cwd = Path.cwd()
    log_file = cwd / "debug.log"
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger(f"{PACKAGE_NAME}.debugger")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


logger = get_logger()


def log_event(event: object):
    """Escreve no log todos os eventos disparados pelo processo do backend.

    Apenas funciona se a variável de ambiente DEBUG estiver definida.
    exemplo: DEBUG=1 make backend-start
    """
    if not os.environ.get("DEBUG"):
        return

    # Caminho do módulo que disparou o evento
    module_name = event.__class__.__module__

    # Classe que disparou o evento
    class_name = event.__class__.__name__

    # Caminho completo da classe que disparou o evento
    dotted_name = f"{module_name}.{class_name}"

    # Escreve no log o evento disparado
    # Utilizamos `info` para garantir que sempre será exibido,
    # sem necessidade de alterar o nível do log da aplicação.
    logger.info(f"Evento: {dotted_name} ({event})")
