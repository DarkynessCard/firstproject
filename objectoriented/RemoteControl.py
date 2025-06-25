class RemoteControl:
    def turn_on(self):
        print("TV is now ON")

    def change_channel(self, channel):
        print(f"Channel changed to {channel}")


remote = RemoteControl()
remote.turn_on()
remote.change_channel(5)