from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///class_management.db'
engine = create_engine('sqlite:///class_management.db')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
if __name__ ==  "__main__":
    app.run(port=8000,debug=True)