import math

with open("can_size.txt") as size_file:
    for line in size_file:
        parts = line.split(",")

        can_name = parts[0].strip()
        radius = float(parts[1])
        height = float(parts[2])
    size_file.close    

def main(size_file):
    print(can_name, radius, height)

#def cylinder_volume(radius, height):
#    volume = math.pi * radius**2 * height
#    return volume

#def cylinder_surface_area(radius, height):
#    surface_area = 2 * math.pi * radius * (radius + height)

#    return surface_area