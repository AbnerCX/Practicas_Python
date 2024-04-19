import logging
import sys
import traceback

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s] [%(funcName)s:%(lineno)d] [%(message)s]",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def test_traceback2():
    test_traceback()


def test_traceback():
    traceback.print_stack()


if __name__ == "__main__":
    try:
        logger.debug(f" Inicio")
        print(f" divide {0 / 0}")
        logger.info(f" Fin.")
    except ZeroDivisionError as error:
        logger.warn(f"{error}")
        logger.exception(error)
        logger.info("-" * 20)
        test_traceback2()

    # sys.exit(0)