import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem2 import gpt_below_zero_a, claude_below_zero_a, gpt_below_zero_b, claude_below_zero_b
from tests.test_p2 import check


# CoT
try:
    check(gpt_below_zero_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# CoT
try:
    check(claude_below_zero_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")

# Self-debugging
try:
    check(gpt_below_zero_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-debugging
try:
    check(claude_below_zero_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")