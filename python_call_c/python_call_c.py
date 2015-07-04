import ctypes

math = ctypes.CDLL("./math_func.so")

print "100 - 10 = %d" % math.sub_func(100,10)

print "100 + 10 = %d" % math.add_func(100,10)

