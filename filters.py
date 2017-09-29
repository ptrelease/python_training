# This filters the numbers in the list to just return those between 10 and 20.

sumbers = [13, 65, 878, 98, 53, 19, 37, 388, 38, 38]


def find_numbers_between(val_min, val_max):

    def between_min_and_max(item):
        return (item > val_min) and (item < val_max)
    return between_min_and_max

print(filter(find_numbers_between(10, 20), sumbers))
