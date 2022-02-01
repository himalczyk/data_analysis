from pathlib import Path
from tokenize import String
from dotenv import load_dotenv
import os

load_dotenv()
PATH_TO_FILE = os.getenv('PATH_TO_FILE')

filename=Path(str(PATH_TO_FILE)).stem