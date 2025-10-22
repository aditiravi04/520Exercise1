import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem1 import gpt_truncate_number_a, claude_truncate_number_a, gpt_truncate_number_b, claude_truncate_number_b
from tests.test_p1 import check

# CoT
try:
    check(gpt_truncate_number_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# CoT
try:
    check(claude_truncate_number_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
# Self-debugging
try:
    check(gpt_truncate_number_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-debugging
try:
    check(claude_truncate_number_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")