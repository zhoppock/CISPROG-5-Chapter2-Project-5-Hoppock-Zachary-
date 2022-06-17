# We are going to calculate an object’s momentum based on its mass and velocity:

# Input the mass (in kilograms) and velocity (in meters per second)
massString = input("What is an object's mass in kilograms? ")
velocityString = input("What is an object's velocity in meters per second? ")

mass = int(massString)
velocity = int(velocityString)

# Compute the object’s momentum using the formula:
# Momentum = mass * velocity
momentum = mass * velocity

# Print the momentum
print("The object's momentum is " + str(momentum) + ".")