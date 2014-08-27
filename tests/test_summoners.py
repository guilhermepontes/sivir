import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from sivir import Sivir

print Sivir.from_region("br").by_user("nulled").get_data()