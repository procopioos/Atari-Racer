import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tempfile
import os
from utils.persistence import load_high_score, save_high_score, load_progress, save_progress

def test_high_score_save_load():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        f.write("100")
        f.flush()
        pass
