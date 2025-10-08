# ================================
# Exercise: Using type() to Explore Data Types
# ================================

# Task: Examine the following variables and predict their types BEFORE running the code.
# Then run the code and see if your predictions were correct.

# NOTE: We are expecting knowledge from section "3. Operators" here

# Variable 1
var1 = 10 / 2
# Your prediction: ... float
print(f"var1 ({var1}) is of type: {type(var1)}")

# Variable 2
var2 = 10 // 2
# Your prediction: ... int
print(f"var2 ({var2}) is of type: {type(var2)}")

# Variable 3
var3 = "True"
# Your prediction: ... string
print(f"var3 ({var3}) is of type: {type(var3)}")

# Variable 4
var4 = True
# Your prediction: ... bool
print(f"var4 ({var4}) is of type: {type(var4)}")

# Variable 5
var5 = None
# Your prediction: ... None
print(f"var5 ({var5}) is of type: {type(var5)}")

# Variable 6
var6 = ""
# Your prediction: ... string
print(f"var6 ('{var6}') is of type: {type(var6)}")

# Variable 7
var7 = 0
# Your prediction: ... int
print(f"var7 ({var7}) is of type: {type(var7)}")

# Variable 8
var8 = 5.0
# Your prediction: ... float
print(f"var8 ({var8}) is of type: {type(var8)}")

# Variable 9
var9 = 999999999999999999999999999999
# Your prediction: ... int
print(f"var9 is of type: {type(var9)}")

# Variable 10
var10 = 3 + 4.5
# Your prediction: ... float
print(f"var10 ({var10}) is of type: {type(var10)}")

# Variable 11
var11 = "123"
# Your prediction: ... string
print(f"var11 ({var11}) is of type: {type(var11)}")

# Variable 12
var12 = True + True
# Your prediction: ... int
print(f"var12 ({var12}) is of type: {type(var12)}")

# Variable 13 (Advanced)
var13 = type
# Your prediction: ... type
print(f"var13 is: {type(var13)}")

# After running, answer these questions:
# 1. Which types were different from your predictions?
# 2. Why does 10 / 2 return a float instead of an int?
# 3. What's the difference between "True" and True?
# 4. Why can you add True + True? What does it equal?