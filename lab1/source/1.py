list = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark', ('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
d = {} # empty dict
for key, value in list:
    d.setdefault(key, []).append(value)    # appending tuples to dict d
print("Dictionary:", d)
s = sorted(d.items(), key=lambda x: x[0])   # key value pairs are sorted using lambda and sorted functions
print("Sorted:", s)                      # desired dict with sorted tuples