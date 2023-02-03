from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from .schema import *
from .chinook import Chinook

''' 
import urllib.request    # needed for download of the example database
import shutil            # needed for unziping of the example database
import os                # for checking existence/removing of a file

urllib.request.urlretrieve(
    "https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip", "chinook.zip")
shutil.unpack_archive("chinook.zip")
os.remove("chinook.zip")
'''
