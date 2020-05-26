## IMPORT MODULES
from flask import Flask, request
import logging, os

## DEFINE LOGGING STANDARDS
logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()

## DEFINE FLASK APPLICATION
def create_app():
    ## LOG APPLICATION START UP
    logger.info('Starting Application ...')
    
    ## DEFINE APPLICATION
    app = Flask(__name__)

    ## DEFAULT INDEX ROUTE
    @app.route("/")
    def index():
        return "HELLO WORLD!"

    ## RETURN APPLICATION
    return app