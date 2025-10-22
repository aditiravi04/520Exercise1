import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem4 import gpt_any_int_a, claude_any_int_a, gpt_any_int_b, claude_any_int_b
from tests.test_p4 import check

# CoT
try:
    check(gpt_any_int_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# CoT
try:
    check(claude_any_int_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")

# Self-debugging
try:
    check(gpt_any_int_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-debugging
try:
    check(claude_any_int_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")