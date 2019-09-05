# function digPow(n, p){
#   var digits = n.toString().split('');
#   var result = 0;
#   for(var i=0; i<digits.length; i++){
#     result = result + Math.pow(digits[i], p);
#     p++;
#   }
#   var data = result/n;
#   if(result % n === 0){
#   return data;
#   }else{
#   return -1;
#   }
# }

# Some numbers have funny properties.
# For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# we want to find a positive integer k, if it exists,
# such as the sum of the digits of n taken to the successive powers of p is equal to k * n.

# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case we will return k, if not return -1.
# Note: n and p will always be given as strictly positive integers.
from asserts.Asserts import assert_true


def dig_pow(n, p):
    digits = list(map(int, str(n)))
    power = 0

    for i in digits:
        power += i ** p
        p += 1

    return power / n if not power % n else -1


assert_true(dig_pow(46288, 3), 51)
