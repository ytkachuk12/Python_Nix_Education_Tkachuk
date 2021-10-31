"""closures func"""


def outside_multiplier(num1: int):
    """take 1st number"""
    def inside_multiplier(num2: int):
        """take 2nd number"""
        return num1*num2
    return inside_multiplier


mul_by5 = outside_multiplier(5)
mul_by6 = outside_multiplier(6)
print(mul_by5(7), mul_by6(7))
