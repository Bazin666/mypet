from flask import Blueprint, Flask

index = Blueprint('index', __name__)
question = Blueprint('question', __name__)
comment = Blueprint('comment', __name__)
from .index import *
from .question import *
from .comment import *
