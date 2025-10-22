import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p2 import p3_claude_below_zero, p3_gpt_below_zero
from tests.test_p2 import check

try:
    check(p3_gpt_below_zero)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_below_zero)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    