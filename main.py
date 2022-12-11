from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import my_calender

cal_list = my_calender.get_cal_list()
converter = {0: "Saturday", 1: "Friday", 2: "Thursday", 3: "Wednesday", 4: "Tuesday", 5: "Monday", 6: "Sunday"}

child_grids = {}
day_btn_representations = []


class Grid_LayoutApp(App):

    def build(self):
        layout = GridLayout(cols=7)

        for weekday in sorted(list(converter.keys())):
            layout.add_widget(Label(text=converter[weekday]))

        for week in cal_list:
            for i in range(7)[::-1]:
                if converter[i] in week.keys():
                    child_grid = GridLayout(cols=1)

                    day_btn_representation = Button(text=week[converter[i]])
                    day_btn_representations.append(day_btn_representation)
                    child_grids[week[converter[i]]] = child_grid

                    day_btn_representation.bind(
                        on_press=lambda x=day_btn_representation: child_grids[str(
                            day_btn_representations.index(x)+1)].add_widget(Label(text="hello")))

                    child_grid.add_widget(day_btn_representation)
                    layout.add_widget(child_grid)
                else:
                    layout.add_widget(Label(text=""))
        print(child_grids)
        return layout


root = Grid_LayoutApp()
# run the App
root.run()
