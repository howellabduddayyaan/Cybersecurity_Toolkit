# ========================
# === Password Manager ===
# ========================

import hashlib
import os
import string
import secrets

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

VAULT_FILE = "vault.txt"

MASTER_PASSWORD = "Doodle"


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


MASTER_HASH = hash_password(MASTER_PASSWORD)


# _________________________________________________________________________________________________
