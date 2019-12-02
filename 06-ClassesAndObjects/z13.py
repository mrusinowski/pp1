class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print(f'Telewizor jest załączony, kanał {self.channel_no}')
        else: print('Telewizor jest wyłączony')
    def set_channel_no(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(channels_list):
        self.channels = channels_list
    def show_channels():
        print('LISTA KANAŁÓW TV'\n)
        for x in range(len(self.channels)):
            print('{x+1}. {self.channels[x]}')