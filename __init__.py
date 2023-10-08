# -*- coding: UTF-8 -*-
from http.server import HTTPServer
from api.index import handler
import logging

logging.basicConfig(
    datefmt = '%d/%b/%Y %H:%M:%S',
    format = '[%(asctime)s] "%(levelname)s: %(message)s" -',
    level=logging.INFO
)

if __name__ == '__main__':
    host = ('0.0.0.0', 80)
    server = HTTPServer(host, handler)
    logging.info("Starting server, listen at http://%s:%s" % host)
    server.serve_forever()
