# testTV
# import class
from TV import TV

# create objects (tv1 and tv2)
tv1 = TV()
tv2 = TV()

# call methods
tv1.turn_on()
tv2.turn_on()

tv1.set_channel(29)
tv2.set_channel(4)

tv1.set_volume(4)
tv2.set_volume(1)

tv1.channel_up()
tv2.channel_down()

tv1.volume_down()
tv2.volume_up()

tv1.turn_off
tv2.turn_off

get_channel_tv1 = tv1.get_channel()
get_channel_tv2  = tv2.get_channel()

get_volume_tv1 = tv1.get_volume()
get_volume_tv2 = tv2.get_volume()


# print result
print("TV1's channel is", get_channel_tv1, "and volume level is", get_volume_tv1)
print("TV2's channel is", get_channel_tv2, "and volume level is", get_volume_tv2)