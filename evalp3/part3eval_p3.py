import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p3 import p3_gpt_mean_absolute_deviation, p3_claude_mean_absolute_deviation
from tests.test_p3 import check

try:
    check(p3_gpt_mean_absolute_deviation)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_mean_absolute_deviation)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    