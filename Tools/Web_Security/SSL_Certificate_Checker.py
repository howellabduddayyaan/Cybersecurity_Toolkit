# ===============================
# === SSL Certificate Checker ===
# ===============================

# --------------------
# Secure Sockets Layer
# --------------------

import socket
import ssl
from datetime import datetime, UTC

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

