from tkinter import *
import os
from tkinter import ttk

import PIL.Image, PIL.ImageTk

from diagram import *
class Scheme:
    def __init__(self, alphabet:str, states:str, master:Tk, main_frame:Frame):
        """
        STANDARD PARAMETERS
        :param alphabet: must be str
        :param states: must be str
        :param master: must be Tk
        :param main_frame: must be Frame
        """
        self.alphabet = alphabet.replace(" ", "")
        self.alphabet_list = self.alphabet.split(",")
        self.states = states
        self.master = master
        self.frame = main_frame
        self.directory = os.getcwd()
        self.column_amount = len(self.alphabet_list) + 2
        self.row_amount = int(states) + 1
        self.state_list = []
        self.title_list = []
        self.body_list = []
        self.output_list = []
        self._recreate_frame()

    def _clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
    def _recreate_frame(self):
        for _ in range(int(self.states)):
            self.state_list.append(f"q{_}")
        self._clear_frame()
        for i in range(self.row_amount):
            for j in range(self.column_amount):
                if i == 0:
                    if j == 0:
                        new_title = Label(master=self.frame, text="States")
                        new_title.grid(row=i, column=j)
                        self.title_list.append(new_title)
                    elif j == self.column_amount - 1:
                        new_title = Label(master=self.frame, text="Outputs")
                        new_title.grid(row=i, column=j)
                        self.title_list.append(new_title)
                    else:
                        new_title = Label(master=self.frame, text=f"after input {self.alphabet_list[j - 1]}")
                        new_title.grid(row=i, column=j)
                        self.title_list.append(new_title)
                else:
                    if j == 0:
                        new_title = Label(master=self.frame, text=f"q{i - 1}")
                        new_title.grid(row=i, column=j)
                    elif j == self.column_amount - 1:
                        new_value = Entry(master=self.frame, highlightthickness=1)
                        new_value.grid(row=i, column=j)
                        self.output_list.append(new_value)
                    else:
                        new_state = ttk.Combobox(master=self.frame, values=self.state_list)
                        new_state.grid(row=i, column=j)
                        self.body_list.append(new_state)
        table_button = Button(master=self.frame, text="Create Diagram", command=self.create_diagram)
        table_button.grid(column=self.column_amount-1, row=self.row_amount)

    def create_diagram(self):
        image_diagram = ImageDiagram(diagram=self._create_table(), state_number=int(self.states), alphabet=self.alphabet_list)
        image = PIL.Image.open(image_diagram.get_image_path())
        golden_ratio = (1 + pow(5, 1 / 2)) / 2
        height = 400
        width = int(height * golden_ratio)
        new_image = image.resize((width, height))
        diagram_image = PIL.ImageTk.PhotoImage(new_image)
        self._clear_frame()
        label = Label(master=self.frame, image=diagram_image)
        label.pack()

    def _create_table(self) -> dict:
        moore_table = {}
        body_list = []
        output_list = []
        body_index = 0
        for state in self.body_list:
            body_list.append(state.get())
        for output in self.output_list:
            output_list.append(output.get())
        for init in range(int(self.states)):
            moore_table[f'q{init}'] = {}
        for _ in range(int(self.states)):
            for index in range(len(self.alphabet_list)):
                moore_table[f'q{_}'][self.alphabet_list[index]] = body_list[body_index+index]
            body_index += len(self.alphabet_list)
            moore_table[f'q{_}']['output'] = output_list[_]
        return moore_table