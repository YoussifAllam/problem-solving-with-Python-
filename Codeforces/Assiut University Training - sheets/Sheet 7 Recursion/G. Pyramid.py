n=int(input())
def print_pyramid_row(row_num, total_height):
    if row_num > total_height:
        return

    num_spaces = total_height - row_num
    num_stars = 2 * row_num - 1

    print(" " * num_spaces + "*" * num_stars)

    print_pyramid_row(row_num + 1, total_height)

def print_pyramid(N):
    print_pyramid_row(1, N)

print_pyramid(n)
