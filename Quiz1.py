def math_prog(x):
    result =  -5 * x**5 + 69 * x**2 - 47
    return result

print math_prog(0)
print math_prog(1)
print math_prog(2)
print math_prog(3)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    FV = present_value * (1 + rate_per_period)**periods
    return(FV)

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print future_value(500, .04, 10, 10)

import math

def area_reg_polygon(n, s):
    area = (0.25) * n * s**2 / math.tan(math.pi/n)
    return(area)

print area_reg_polygon(7,3)

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)
