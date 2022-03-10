"""
try: # Try to do this code
except: # Do this if there was an exception
else: # Do this if there were no exceptions
finally: # Do this no matter what happens
"""

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height** 2

print(bmi)