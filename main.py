from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import my_calender

cal_list = my_calender.get_cal_list()
converter = {0: "Saturday", 1: "Friday", 2: "Thursday", 3: "Wednesday", 4: "Tuesday", 5: "Monday", 6: "Sunday"}


class Grid_LayoutApp(App):

    def build(self):
        layout = GridLayout(cols=7)

        for weekday in sorted(list(converter.keys())):
            layout.add_widget(Label(text=converter[weekday]))

        for week in cal_list:
            for i in range(7)[::-1]:
                if converter[i] in week.keys():
                    layout.add_widget(Label(text=week[converter[i]]))
                else:
                    layout.add_widget(Label(text=""))
        return layout


root = Grid_LayoutApp()
# run the App
root.run()
