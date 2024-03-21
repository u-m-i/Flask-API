import sys
import logging

from flask import Flask


def create_app():

    app = Flask(__name__)

    #configure env variables

    # Configure logging

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(messages)s", stream=sys.stdout)


    return app

