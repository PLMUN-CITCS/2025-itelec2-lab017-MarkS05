# Import the math module
import math

# Define the function to calculate the area of a circle
def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    # Calculate the area using the formula: area = π * radius^2
    area = math.pi * (radius ** 2)
    # Return the calculated area
    return area

# Call the function and display the result
radius_value = 5  # Assign a specific radius
area_result = circle_area(radius_value)  # Call the function with the radius value

# Print the result with formatted output to 2 decimal places
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")