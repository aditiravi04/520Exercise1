import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p4 import p3_gpt_any_int, p3_claude_any_int
from tests.test_p4 import check

try:
    check(p3_gpt_any_int)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_any_int)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    