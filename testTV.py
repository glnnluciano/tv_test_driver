# testTV
# import class
from TV import TV

# create objects (tv1 and tv2)
tv1 = TV()
tv2 = TV()

# call methods
tv1.set_channel(2)
tv2.set_channel(5)

get_channel1 = tv1.get_channel()
get_channel2  = tv2.get_channel()

# print result
print(get_channel1)
print(get_channel2)