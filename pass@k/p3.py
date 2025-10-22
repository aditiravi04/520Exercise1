import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem3 import gpt_mean_absolute_deviation_a, claude_mean_absolute_deviation_a, gpt_mean_absolute_deviation_b, claude_mean_absolute_deviation_b
from tests.test_p3 import check

# CoT
try:
    check(gpt_mean_absolute_deviation_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# CoT
try:
    check(claude_mean_absolute_deviation_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")


# Self-debugging
try:
    check(gpt_mean_absolute_deviation_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-debugging
try:
    check(claude_mean_absolute_deviation_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
