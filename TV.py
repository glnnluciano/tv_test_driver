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
    def turn_off(self):
        self.power = False

    # get_channel()
    def get_channel(self):
        return self.channel

    # set_channel()
    def set_channel(self, set_channel):
        if self.power == False:
            print("TV is off")
            return          
        if 1 <= set_channel <= 120:
            self.channel = set_channel
        else:
            print("Set channel is out of range")      
        
    # get_volume()
    def get_volume(self):
        return self.volume_level

    # set volume()
    def set_volume(self, set_volume):
        if self.power == False:
            print("TV is off")
            return
        if 1 <= set_volume <= 7:
            self.volume_level = set_volume
        else:
            print("Set volume is out of range") 

    # channel_up()
    def channel_up(self):
        if self.power == False:
            print("TV is off. Can't modify channel.")
            return
        if self.channel == 120:
            print("Max channel reached")
        else:
            self.channel = self.channel + 1

    # channel_down()
    def channel_down(self):
        if self.power == False:
            print("TV is off. Can't modify channel.")
            return
        if self.channel == 1:
            print("Min channel reached")
            return
        else:
            self.channel = self.channel - 1

    # volume_up()
    def volume_up(self):
        if self.power == False:
            print("TV is off. Can't modify volume.")
            return
        if self.volume_level == 7:
            print("Max volume reached")
            return
        else:
            self.volume_level = self.volume_level + 1

    # volume_down()
    def volume_down(self):
        if self.power == False:
            print("TV is off. Can't modify volume.")
            return
        if self.volume_level == 1:
            print("Min volume reached")
            return
        else:
            self.volume_level = self.volume_level - 1

# END OF PROGRAM