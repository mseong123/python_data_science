from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

"""
height = [2.71, 1.15]
weight = [165.3, 38.4]
print("output is suppose to be correct")
print("height = ", height)
print("weight = ", weight)
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

height = [2.3, 2.1, 1.5, 1.9, 2]
weight = [100, 20, 120, 51, 110]
print("output is suppose to be correct")
print("height = ", height)
print("weight = ", weight)
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 25))
print()

height = None
weight = [165.3, 38.4]
print("output is suppose to be wrong")
print("height = ", height)
print("weight = ", weight)
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

height = [2.71, 1.15]
weight = None
print("output is suppose to be wrong")
print("height = ", height)
print("weight = ", weight)
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

height = None
weight = None
print("output is suppose to be wrong")
print("height = ", height)
print("weight = ", weight)
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

height = [2.3, 2.1, 1.5, 1.9, 2]
weight = [100, True, 120, 51, "Hello"]
print("output is suppose to be wrong")
print("height = ", height)
print("weight = ", weight)
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

height = [2.3, 2.1, "hello", 1.9, 2]
weight = [100, True, 120, 51, "Hello"]
print("output is suppose to be wrong")
print("height = ", height)
print("weight = ", weight)
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()
"""