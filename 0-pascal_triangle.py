# 0-pascal_triangle.py
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Every row starts with 1
        # Add adjacent elements from the previous row
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
