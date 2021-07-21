import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "4567121"
    MONGO_URI = "mongodb+srv://student:Smile123@clustercube.ebgyq.mongodb.net?retryWrites=true&w=majority"