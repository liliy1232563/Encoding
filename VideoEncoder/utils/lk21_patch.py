import urllib.parse
import re

# Patch re.sre_parse for lk21/exrex compatibility on Python 3.12+
if not hasattr(re, "sre_parse"):
    import re._parser
    re.sre_parse = re._parser

# Save original urlparse
_original_urlparse = urllib.parse.urlparse

def safe_urlparse(url, scheme='', allow_fragments=True):
    try:
        return _original_urlparse(url, scheme, allow_fragments)
    except Exception:
        return _original_urlparse("http://invalid", scheme, allow_fragments)

# Apply safe urlparse patch
urllib.parse.urlparse = safe_urlparse

# Import lk21 after monkey patch
import lk21

# Apply pyrogram save_file patch
from . import pyrogram_patch