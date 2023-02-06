class electronic_device:
    power = 2000
class pocket_gadget(electronic_device):
    power = 1000
class mobile(pocket_gadget):
    def mobile_uses(self):
        return f"Mobile is awesome" \
               f"it take power only {self.power}"


nokia =mobile()
print(nokia.mobile_uses())



#
# class Electronic_device():
#     power_source = "Alternating current or Direct Current"
#     use = "Automates works and make the work very faster and efficient"
#     start = "It is a kind of device which uses"
#
#     def printdetails(self):
#         return f"{self.start} {self.power_source} and {self.use}".capitalize()
#
#
# class Pocket_gadget(Electronic_device):
#     power_source = "Direct current"
#     addon_features = "It is portable and looks super awesome"
#
#     def printdetails(self):
#         return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()
#
#
# class Phone(Pocket_gadget):
#     use = "Its main feature is calling other person's phone to talk"
#
#     def printdetails(self):
#         return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()
#
#
# computer = Electronic_device()
# miband = Pocket_gadget()
# redmi = Phone()
#
# print(computer.printdetails())
# print(miband.printdetails())
# print(redmi.printdetails())