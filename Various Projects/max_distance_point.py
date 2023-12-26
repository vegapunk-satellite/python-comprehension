from math import sqrt

# (x1, y1) -- (x2, y2) = sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

def distance(point1, point2):
    return sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))

def find_max_distance_point(start_point, end_points):
    max_point = None
    max_distance = None
    for point in end_points:
        current_distance = distance(start_point, point)
        if max_distance is None or distance(start_point, point) > max_distance:
            max_point = point
            max_distance = current_distance
    return max_point



start_point = (3, 4)
end_points = [(1, 10), (-3, 2), (0, 6), (3, 0), (-1, -3)]
max_distance_point = find_max_distance_point(start_point, end_points)
print("Max distance point: " + str(max_distance_point))
print("Max distance: " + str(distance(start_point, max_distance_point)))