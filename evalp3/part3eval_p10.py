import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p10 import p3_gpt_cycpattern_check, p3_claude_cycpattern_check
from tests.test_p10 import check

try:
    check(p3_gpt_cycpattern_check)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_cycpattern_check)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    