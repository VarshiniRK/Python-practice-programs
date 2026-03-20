import math
a=20
b=28
def gcd(a,b):
    if a==0 or b==0:
        return max(a,b)
    #you only need to find the factor of a minimum number, which itself will be the factor of the larger number between two
    z=min(a,b)
    #check if the minimum number is dividing both a and b, if not reduce it by one and check, continue it until you find the first number which is dividing both a and b which will be the largest factor among both
    while z>0:
        if a%z==0 and b%z==0:
            return z
        z=z-1
print(gcd(a,b))

#Using recursion -> using mathematical proof of gcd(minimum_number, max_number-min_number)
    #│  GCD(a, b) = GCD(b, a - b)    where a > b                   │
        # │                                                              │
        # │  "The GCD of two numbers doesn't change                      │
        # │   if you SUBTRACT the smaller from the larger!"              │
        # │                                                              │
        # │  WHY? If a number d divides both a and b,                    │
        # │  then d also divides (a - b)!                                │
        # │                                                              │
        # │  Example: GCD(12, 8)                                         │
        # │  = GCD(8, 12-8) = GCD(8, 4)                                 │
        # │  = GCD(4, 8-4) = GCD(4, 4)                                  │
        # │  = GCD(4, 4-4) = GCD(4, 0)                                  │
        # │  = 4 ✅    
    #         RULE: Keep subtracting the SMALLER from the LARGER          │
    # │        until both numbers become EQUAL                       │
    # │        That equal number IS the GCD!  

def gcd_a_b(a,b):
    if a==0 or b==0:
        return max(a,b)
    if a==b:
        return a  
    if a>b:
        return gcd_a_b(b,a-b)
    if b>a:
        return gcd_a_b(a,b-a)
print(gcd_a_b(20,28))

#Using recursion but don't wait till both numbers become EQUAL, check if one number divides the other number evenly without any remainder
#if yes then that number is the GCD, this will help you to converge fastly to the correct GCD
# gcd(100, 10)

# APPROACH 2 (pure subtraction):
# gcd(100,10) → gcd(90,10) → gcd(80,10) → gcd(70,10) → 
# gcd(60,10) → gcd(50,10) → gcd(40,10) → gcd(30,10) → 
# gcd(20,10) → gcd(10,10) → 10
# 10 CALLS! 😰

# APPROACH 3 (with divisibility check):
# gcd(100,10) → 100 % 10 = 0 → return 10 IMMEDIATELY!
# 1 CALL! 🚀

# Saved 9 calls!
def gcd_a_b_sub_Divisibility(a,b):
    if a==0 or b==0:
        return max(a,b)
    if a==b:
        return a
    if a%b==0:
        return b
    if b%a==0:
        return b
    if a>b:
        return gcd_a_b_sub_Divisibility(b,a-b)
    if b>a:
        return gcd_a_b_sub_Divisibility(a, b-a)
    
print(gcd_a_b_sub_Divisibility(a,b))

#Using recursion but instead of subtraction of larger with smaller we do the remainder check
#  Instead of subtracting ONCE:                                │
# │    GCD(a, b) = GCD(a - b, b)                                 │
# │                                                              │
# │  Subtract AS MANY TIMES AS POSSIBLE at once:                 │
# │    GCD(a, b) = GCD(b, a % b)                                 │
# │                     ↑                                        │
# │              a % b = remainder after dividing a by b         │
# │              = result of subtracting b from a REPEATEDLY     │
# │                until you can't anymore!                      │
# │                                                              │
# │  EXAMPLE: a=48, b=18                                         │
# │                                                              │
# │  Subtraction approach:                                       │
# │    48 - 18 = 30    (subtract once)                           │
# │    30 - 18 = 12    (subtract again)                          │
# │    12 < 18, can't subtract anymore!                          │
# │    Remainder = 12                                            │
# │                                                              │
# │  Modulo approach:                                            │
# │    48 % 18 = 12    (does ALL subtractions at once!)          │
# │                                                              │
# │  SAME RESULT, but modulo does it in ONE step! 🚀             │
# │                                                              │
# 48 % 18 = ?

# 48 ÷ 18 = 2 remainder 12

# This means: 18 fits into 48 exactly 2 times
#             48 = 18 × 2 + 12
            
# Which is the SAME as:
#             48 - 18 = 30    (first subtraction)
#             30 - 18 = 12    (second subtraction)
#             12 < 18, STOP!  (can't subtract anymore)
#             Remainder = 12

# MODULO does 2 subtractions in ONE operation!

# For gcd(1000000, 3):
#   Subtraction: 333,333 steps! 🐌
#   Modulo: 1000000 % 3 = 1 → ONE step! 🚀

#why are we not checking a==0 and what happens if a>b why aren't we checking those two conditions?
# │  We DON'T need to check a == 0 because:                      │
# │                                                              │
# │  1. In the recursive call: gcd(b, a % b)                     │
# │     → 'b' becomes the NEW 'a'                                │
# │     → 'a % b' becomes the NEW 'b'                            │
# │                                                              │
# │  2. The only value that can become 0 through a % b           │
# │     is the SECOND argument (new b)                           │
# │                                                              │
# │  3. If a == 0 initially (first call), we can handle it       │
# │     BUT within the recursion, a is NEVER 0                   │
# │     because a was the previous b, and b was > 0!             │
#│  → gcd(0,5) takes 2 calls: gcd(0,5)→gcd(5,0)→return 5      │

# │                                                              │
# │  gcd(18, 48)                                                 │
# │                                                              │
# │  Step 1: b = 48, b == 0? NO                                  │
# │          return gcd(48, 18 % 48)                             │
# │                                                              │
# │  18 % 48 = ???                                               │
# │                                                              │
# │  18 ÷ 48 = 0 remainder 18                                    │
# │  (48 goes into 18 ZERO times!)                               │
# │                                                              │
# │  18 % 48 = 18                                                │
# │                                                              │
# │  So: gcd(18, 48) → gcd(48, 18)                               │
# │                                                              │
# │  IT JUST SWAPPED THEM! 🔄                                    │
# │                                                              │
# │  The first step AUTOMATICALLY puts the                       │
# │  LARGER number first!                                        │
# │                         

def gcd_a_b_sub_remainder(a,b):
    if b==0:
        return a
    else:
        return gcd_a_b_sub_remainder(b, a%b)
    
print(gcd_a_b_sub_remainder(a,b))

# Using mathematical function
print(math.gcd(a,b))


