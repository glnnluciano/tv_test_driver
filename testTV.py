# testTV
# import class
from TV import TV

# create objects (tv1 and tv2)
tv1 = TV()
tv2 = TV()

# call methods
tv1.set_channel(2)
tv2.set_channel(5)

tv1.set_volume(3)
tv2.set_volume(6)

get_channel1 = tv1.get_channel()
get_channel2  = tv2.get_channel()

get_volume1 = tv1.get_volume()
get_volume2 = tv2.get_volume()

# print result
print("TV1 channel:", get_channel1, "volume:", get_volume1 )
print("TV2 channel:", get_channel2, "volume:", get_volume2)
