# TV class
class TV:
# define __init__ attributes and default values of attributes
    def __init__(self):
        # set 1 as default channel
        self.channel = 1
        # set 1 as default volume_level
        self.volume_level = 1
        # set false (off) as default
        self.power = False
        
# define methods
    def turn_on(self):
        self.power = True

    # turn_off()
    def turn_on(self):
        self.power = False

    # get_channel()
    def get_channel(self):
        return self.channel

    # set_channel()
    def set_channel(self, set_channel):
        self.channel = set_channel
        
    # get_volume()
    def get_volume(self):
        return self.volume_level

    # set volume()
    def set_volume(self, set_volume):
        self.volume_level = set_volume

    # channel_up()
    def channel_up(self):
        self.channel = self.channel + 1

    # channel_down()
    def channel_down(self):
        self.channel = self.channel - 1

    # volume_up()
    def volume_up(self):
        self.volume_level = self.volume_level + 1

    # volume_down()
    def volume_down(self):
        self.volume_level = self.volume_level - 1


