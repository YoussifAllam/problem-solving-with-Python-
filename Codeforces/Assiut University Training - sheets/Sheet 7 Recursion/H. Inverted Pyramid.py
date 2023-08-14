n=int(input())
def print_inverted_pyramid_row(row_num, total_height):
    if row_num > total_height:
        return

    num_spaces = row_num - 1
    num_stars = 2 * (total_height - row_num) + 1

    print(" " * num_spaces + "*" * num_stars)

    print_inverted_pyramid_row(row_num + 1, total_height)

def print_inverted_pyramid(N):
    print_inverted_pyramid_row(1, N)


print_inverted_pyramid(n)
