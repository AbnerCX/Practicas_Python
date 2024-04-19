import logging
import sys
import traceback

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s] [%(funcName)s:%(lineno)d] [%(message)s]",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

print('Hola mundo')

lista = ['hoola', 'amigos', 'como ', 'estan']

logger.info(lista)