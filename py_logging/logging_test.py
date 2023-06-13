import logging
import os

x = 3
y = 0

x_vals = [2, 3, 6, 4, 10]
y_vals = [5, 7, 12, 0, 1]

if __name__ == '__main__':
    # level - с какого уровня необходимо передавать информацию в файл
    logging.basicConfig(level=logging.DEBUG, filename="py_log.log", filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")

    logging.info(f"The values of x and y are {x} and {y}.")
    try:
        result = x / y
        logging.info(f"x/y successful with result: {x / y}.")
    except ZeroDivisionError:
        logging.error('ZeroDivisionError', exc_info=True)

    # for x_val, y_val in zip(x_vals, y_vals):
    #     x, y = x_val, y_val
    #     logging.info(f"The values of x and y are {x} and {y}.")
    #     try:
    #         result = x / y
    #         logging.info(f"x/y successful with result: {x / y}.")
    #     except ZeroDivisionError:
    #         logging.exception("ZeroDivisionError")
