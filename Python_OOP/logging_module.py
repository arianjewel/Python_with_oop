import logging

logging.basicConfig(filename="test.log", filemode='w', level=logging.WARNING, format='%(message)s   (%(asctime)s)', datefmt='%d/%m/%y %I:%M:%S %p')

logging.debug('This is debug log')
logging.info('This is info log')
logging.warning('This is warning log')
logging.error('This is error log')
logging.critical('This is critical log')
