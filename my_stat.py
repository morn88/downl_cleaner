import statistics

example_list = [4, 6, 2, 6, 7, 8, 2, 5, 6, 4, 6, 7, 2, 2]
example_list2 = [1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
example_list3 = [1, 100, 101, 2]
x = statistics.mean(example_list)
y = statistics.median(example_list)
z = statistics.stdev(example_list)
a = statistics.median_low(example_list)
b = statistics.median_high(example_list)
c = statistics.variance(example_list)
print(x, y, z, a, b)
print(c)
d = statistics.variance(example_list2)
e = statistics.variance(example_list3)
print(d)
print(e)
