import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem7 import gpt_is_bored_a, claude_is_bored_a, gpt_is_bored_b, claude_is_bored_b, gpt_is_bored_try2, gpt_is_bored_try3, gpt_is_bored_try4, claude_is_bored_try2, claude_is_bored_try3
from tests.test_p7 import check

# Self-repair
try:
    check(gpt_is_bored_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-repair
try:
    check(claude_is_bored_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
# CoT
try:
    check(gpt_is_bored_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# CoT
try:
    check(claude_is_bored_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    

    
# For GPT's responses for part 2 of the exercise (debugging & iterative improvement)
try:
    check(gpt_is_bored_try2)
    print("GPT solution try 2: pass")
except AssertionError:
    print("GPT solution try 2: fail")

try:
    check(gpt_is_bored_try3)
    print("GPT solution try 3: pass")
except AssertionError:
    print("GPT solution try 3: fail")
    
try:
    check(gpt_is_bored_try4)
    print("GPT solution try 4: pass")
except AssertionError:
    print("GPT solution try 4: fail")

# For Claude's responses for part 2 of the exercise (debugging & iterative improvement)

try:
    check(claude_is_bored_try2)
    print("Claude solution try 2: pass")
except AssertionError:
    print("Claude solution try 2: fail")
    
try:
    check(claude_is_bored_try3)
    print("Claude solution try 3: pass")
except AssertionError:
    print("Claude solution try 3: fail")