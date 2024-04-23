class Television:
    def __init__(self):
        """
        default instnce variables
        """
        self.__min_volume = 0
        self.__max_volume = 2
        self.__min_channel = 0
        self.__max_channel = 3
        self.__status = False
        self.__muted = False
        self.__volume = 0
        self.__channel = 0
        self.__before_muted = 0 # value that allows us to get the volume again after muted

    def power(self):
        """
        it allows us turn on or off
        """
        self.__status = not self.__status

    def mute(self):
        """
        it makes the tv muted
        """
        if self.__status == True:
            self.__muted = not self.__muted
            self.__before_muted = self.__volume
            self.__volume = 0
        
        
        

    def channel_up(self):
        """
        It change the channel up, and when the channel meet to the maximum channel = 3,
        it change the channel to minimum.
        """
        if self.__status == True:
            self.__channel = (self.__channel + 1) % (self.__max_channel + 1)

    def channel_down(self):
        """ 
        It change the channel down, and when the channel meet to the minimum channel = 0,
        it change the channel to minimum.
        """
        if self.__status == True:
            self.__channel = self.__channel -1 
            if self.__channel < 0:
                self.__channel = self.__max_channel    
    
    
    def volume_up(self):
        """
        it makes volume up
        """
        if self.__muted == True:
            self.__muted = False
            self.__volume = self.__before_muted
        if self.__status == True:
            if self.__volume < self.__max_volume:
                self.__volume += 1
                
    def volume_down(self):
        """
        it makes volume down
        """
        if self.__muted == True:
            self.__muted = False
            self.__volume = self.__before_muted
        if self.__status == True:
           if self.__min_volume < self.__volume:
               self.__volume -= 1
               
    def __str__(self):
        return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"