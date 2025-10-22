import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p1 import p3_gpt_truncate_number, p3_claude_truncate_number
from tests.test_p1 import check

try:
    check(p3_gpt_truncate_number)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_truncate_number)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")