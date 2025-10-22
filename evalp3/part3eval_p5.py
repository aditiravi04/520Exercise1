import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p5 import p3_gpt_multiply, p3_claude_multiply
from tests.test_p5 import check

try:
    check(p3_gpt_multiply)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_multiply)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    