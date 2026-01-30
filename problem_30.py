def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

r = "5"
print(f"Area: {area_of_circle(float(r))}")  # Convert string to float
