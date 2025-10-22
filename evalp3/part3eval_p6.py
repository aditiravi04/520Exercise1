import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p6 import p3_gpt_count_upper, p3_claude_count_upper
from tests.test_p6 import check

try:
    check(p3_gpt_count_upper)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_count_upper)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    