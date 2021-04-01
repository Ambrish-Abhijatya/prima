from classes import chef

myChef = chef()
myChef.make_special_dish()

class ChineseChef(chef):

    def make_special_dish(self):  #This overrides the make_special_dish function inherited from the chef class.
        print("The chef makes orange chicken.")

    def make_fried_rice(self):
        print("The chef makes fried rice.")


myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_salad()