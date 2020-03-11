from os import environ
import os

PORT = environ.get('SERVER_PORT', 8080)
PORT_HTTP2 = environ.get('SERVER_HTTP2_PORT', 9090)

try:
    PORT = int(PORT)
except:
    raise Exception(f'Invalid port: {PORT}')


IP_ADDR_REGEX = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
DOMAIN_REGEX = r'^([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'

GLOBAL_ORDER_API_PREFIX = '/api'
GLOBAL_USER_API_PREFIX = '/api'

""" certificates """
keyfile = os.path.join(os.path.dirname(__file__), 'key.pem')
certfile = os.path.join(os.path.dirname(__file__), 'certificate.pem')
