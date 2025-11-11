from importlib import import_module
import pkgutil
from typing import Iterable, Optional
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine import Engine

base = declarative_base()
metadata = base.metadata