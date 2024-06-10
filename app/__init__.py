import sys
import logging

from flask import Flask
from dotenv import  load_dotenv



def create_app():

    app = Flask(__name__)

    # Configure env variables
    load_dotenv()

    app.config["BASIC_ROUTE"] = os.getenv("BASIC_ROUTE")

    # Configure logging

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(messages)s", stream=sys.stdout)

    return app

