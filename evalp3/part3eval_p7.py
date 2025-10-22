import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p7 import p3_gpt_is_bored, p3_claude_is_bored
from tests.test_p7 import check

try:
    check(p3_gpt_is_bored)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_is_bored)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    