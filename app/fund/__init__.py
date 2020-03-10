from flask import Blueprint
# from . import views Can't import this before Bluepriint

fund = Blueprint('fund',__name__)
from . import views # must import this line