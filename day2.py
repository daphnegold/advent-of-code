total_paper = 0
with open('day2.txt') as present_file:
    presents = present_file.readlines()
    for present in presents:
        dimensions = present.strip().split('x')
        dimensions_int = []
        for dimension in dimensions:
            dimensions_int.append(int(dimension))
        side1 = 2 * dimensions_int[0] * dimensions_int[1]
        side2 = 2 * dimensions_int[0] * dimensions_int[2]
        side3 = 2 * dimensions_int[1] * dimensions_int[2]
        smallest_side = min(side1,side2,side3)
        total_paper = total_paper + side1 + side2 + side3 + (0.5 * smallest_side)

print total_paper
