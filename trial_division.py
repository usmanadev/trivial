import math

def trial_division(num: int) -> bool:
    """Checks if given input is prime.
    """
    for i in range(2, math.sqrt(num)):
        if num / i == 0:
            return False
    return True
