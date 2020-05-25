from flask import Blueprint, Flask

index = Blueprint('index', __name__)
question = Blueprint('question', __name__)

from .index import *
from .question import *
