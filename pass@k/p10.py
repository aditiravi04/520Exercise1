import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem10 import gpt_cycpattern_check_a, claude_cycpattern_check_a, gpt_cycpattern_check_b, claude_cycpattern_check_b, gpt_cycpattern_check_try2, gpt_cycpattern_check_try3, claude_cycpattern_check_try2, claude_cycpattern_check_try3
from tests.test_p10 import check

# CoT
try:
    check(gpt_cycpattern_check_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(claude_cycpattern_check_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
# Self-debugging
try:
    check(gpt_cycpattern_check_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(claude_cycpattern_check_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
# For GPT's responses for part 2 of the exercise (debugging & iterative improvement)
try:
    check(gpt_cycpattern_check_try2)
    print("GPT solution try 2: pass")
except AssertionError:
    print("GPT solution try 2: fail")
    
try:
    check(gpt_cycpattern_check_try3)
    print("GPT solution try 3: pass")
except AssertionError:
    print("GPT solution try 3: fail")
    
# For Claude's responses for part 2 of the exercise (debugging & iterative improvement)
try:
    check(claude_cycpattern_check_try2)
    print("Claude solution try 2: pass")
except AssertionError:
    print("Claude solution try 2: fail")
    
try:
    check(claude_cycpattern_check_try3)
    print("Claude solution try 3: pass")
except AssertionError:
    print("Claude solution try 3: fail")