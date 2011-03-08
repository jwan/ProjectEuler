# By starting at the top of the triangle below and moving to adjacent numbers on the
# row below, the maximum total from top to bottom is 23. (3 -> 7 -> 4 -> 9)
# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in no067.txt, a 15K text file
# containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible
# to try every route to solve this problem, as there are 2**99 altogether! If you
# could check one trillion (10**12) routes every second it would take over twenty
# billion years to check them all. There is an efficient algorithm to solve it. ;o)

def str_to_int_line(list_):
    return [ int(entry) for entry in list_ ]

def max_sum(triangle_mat):
    # We have a maximum at each depth, we initially start at a depth of zero
    # and work up to the top
    max_depth = len(triangle_mat) - 1
    depth = max_depth
    result = {}
    for i, entry in enumerate(triangle_mat[depth]):
        result[(i, max_depth - depth)] = entry

    depth -= 1
    while depth >= 0:
        for i, entry in enumerate(triangle_mat[depth]):
            result[(i, max_depth - depth)] = entry + max(
                result[(i, max_depth - depth - 1)], result[(i + 1, max_depth - depth - 1)] )
        depth -= 1
    return result[(0, max_depth - depth - 1)]

if __name__ == "__main__":
    print "The answer to Euler Project, question 18 is:",
    with open('/Users/dan/Documents/sandbox/euler_project'
              '/problem_data/no067.txt', 'r') as fh:
        triangle = fh.read().strip()
    triangle_mat = [ str_to_int_line(line.split()) for line in triangle.split("\n") ]
    n = 100
    triangle_mat = triangle_mat[:n]
    print max_sum(triangle_mat)

s = """\
def str_to_int_line(list_):
    return [ int(entry) for entry in list_ ]

def max_sum(triangle_mat):
    # We have a maximum at each depth, we initially start at a depth of zero
    # and work up to the top
    max_depth = len(triangle_mat) - 1
    depth = max_depth
    result = {}
    for i, entry in enumerate(triangle_mat[depth]):
        result[(i, max_depth - depth)] = entry

    depth -= 1
    while depth >= 0:
        for i, entry in enumerate(triangle_mat[depth]):
            result[(i, max_depth - depth)] = entry + max(
                result[(i, max_depth - depth - 1)], result[(i + 1, max_depth - depth - 1)] )
        depth -= 1
    return result[(0, max_depth - depth - 1)]

if __name__ == "__main__":
    print "The answer to Euler Project, question 18 is:",
    with open('no067.txt', 'r') as fh:
        triangle = fh.read().strip()
    triangle_mat = [ str_to_int_line(line.split()) for line in triangle.split("\\n") ]
    n = %s
    triangle_mat = triangle_mat[:n]
    print max_sum(triangle_mat)
"""

def avg_run_time(rows):
    import timeit
    t = timeit.Timer(stmt=(s % rows))
    return sum([t.timeit(number=100) for i in range(10000) ])/10000.0

run_times = [ avg_run_time(i) for i in range(1, 101) ]
print run_times
