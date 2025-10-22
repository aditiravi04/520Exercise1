import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem5 import gpt_multiply_a, claude_multiply_a, gpt_multiply_b, claude_multiply_b
from tests.test_p5 import check


# CoT
try:
    check(gpt_multiply_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# CoT
try:
    check(claude_multiply_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")

# Self-repair
try:
    check(gpt_multiply_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-repair
try:
    check(claude_multiply_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")