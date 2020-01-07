"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import G.player_views
import G.admin_views
