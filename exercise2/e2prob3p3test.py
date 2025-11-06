
from exercise2.e2prob3p3 import gpt_mean_absolute_deviation
from tests.test_p3 import check

try:
    check(gpt_mean_absolute_deviation)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")