# This filters the numbers in the list to just return those between 10 and 20.
# But uses a list comprehension rather than a filter.
# It effectively looks at every item in the list - so probably not as good as the
# the filter in this scenario - but better if you want to transform every item
# in the list.

sumbers = [13, 65, 878, 98, 53, 19, 37, 388, 38, 38]

def between_10_and_20(sumber):
    if (sumber > 10) and (sumber < 20):
        return sumber

print([between_10_and_20(sumber) for sumber in sumbers])

