import os
from tkinter import *
from tkinter import ttk

# Bu mevcut dizindir.
directory = os.getcwd()

# Kullanıcıdan input değerlerini alabileceğimiz bir pencere oluşturalım
window = Tk()

# Pencere başlığı
window.title("Moore Machine")

# Pencere boyutu
window.geometry("1280x720")
window.config(pady=15, padx=15)

frame1 = Frame(master=window, highlightthickness=2, highlightbackground="blue")
frame1.pack(anchor=NW)
# Frame 1 içeriği:
alphabet_label = Label(master=frame1, text="Alfabe giriniz: ")
alphabet_label.grid(row=0, column=0, padx=15, pady=15, sticky=W)

alphabet_entry = Entry(master=frame1, highlightthickness=2, highlightbackground="blue")
alphabet_entry.grid(row=0, column=1, padx=15, pady=15)

state_label = Label(master=frame1, text="Durum sayısını giriniz: ")
state_label.grid(row=1, column=0, padx=15, pady=15, sticky=W)

state_entry = Entry(master=frame1, highlightthickness=2, highlightbackground="blue")
state_entry.grid(row=1, column=1)


def create_scheme(alphabet, states):
    alphabet = alphabet.replace(" ", "")
    alphabet_list = alphabet.split(",")
    column_amount = len(alphabet_list) + 2
    row_amount = int(states) + 1
    state_list = []
    for _ in range(int(states)):
        state_list.append(f"q{_}")
    frame2 = Frame(master=window, highlightthickness=2, highlightbackground="blue")
    frame2.pack()
    title_list = []
    body_list = []
    output_list = []
    for i in range(row_amount):
        for j in range(column_amount):
            if i == 0:
                if j == 0:
                    new_title = Label(master=frame2, text="Durumlar")
                    new_title.grid(row=i, column=j)
                    title_list.append(new_title)
                elif j == column_amount - 1:
                    new_title = Label(master=frame2, text="Çıktılar")
                    new_title.grid(row=i, column=j)
                    title_list.append(new_title)
                else:
                    new_title = Label(master=frame2, text=f"after input {alphabet_list[j - 1]}")
                    new_title.grid(row=i, column=j)
                    title_list.append(new_title)
            else:
                if j == 0:
                    new_title = Label(master=frame2, text=f"q{i - 1}")
                    new_title.grid(row=i, column=j)
                elif j == column_amount - 1:
                    new_value = Entry(master=frame2, highlightthickness=1)
                    new_value.grid(row=i, column=j)
                    output_list.append(new_value)
                else:
                    new_state = ttk.Combobox(master=frame2, values=state_list)
                    new_state.grid(row=i, column=j)
                    body_list.append(new_state)

    def create_table():
        print("Create Table")
        k = 0
        m = 0
        with open(directory + "\\table.txt", "a") as file:
            for n in range(row_amount):
                for o in range(column_amount):
                    if n == 0:
                        if o == 0:
                            with open(directory + "\\output.txt", "a") as output_file:
                                output_file.write("durum\toutput\n")
                            file.write("durum\t")
                        elif o == column_amount - 1:
                            file.write("\n")
                        else:
                            file.write(f"{alphabet_list[o - 1]}\t")
                    else:
                        if o == 0:
                            with open(directory + "\\output.txt", "a") as output_file:
                                output_file.write(f"q{n - 1}\t")
                            file.write(f"q{n - 1}\t")
                        elif o == column_amount - 1:
                            with open(directory + "\\output.txt", "a") as output_file:
                                output_file.write(f"{output_list[m].get()}\n")
                                m = m + 1
                            file.write("\n")
                        else:
                            file.write(f"{body_list[k].get()}\t")
                            k = k + 1

        def convert():
            transition_table = {}
            output_table = {}

            # ilk giriş state'ini bu değişkende tutalım
            first_input = ''

            # Geçiş tablosunun okunup, oluşturulması
            with open(directory + "\\table.txt", "r") as f:
                ingredients = f.readlines()

                title = ingredients[0]
                inputs = title.strip().split(sep='\t')[1:]

                input_amount = len(inputs)

                say = 0
                for line in ingredients[1:]:
                    row = line.strip().split(sep='\t')
                    d = {inputs[p]: row[p + 1] for p in range(input_amount)}
                    transition_table[row[0]] = d
                    if say == 0:
                        first_input = row[0]
                    say = say + 1

            # Output tablosunun okunup, oluşturulması
            with open(directory + "\\output.txt") as f:
                ingredients = f.readlines()

                for line in ingredients[1:]:
                    row = line.strip().split(sep='\t')
                    output_table[row[0]] = row[1]
                    print(output_table)

            # Kullanıcıdan giriş stringinin istenmesi

            entry = input_string.get()

            print('\n' * 2)
            print('Adım Adım Gösterim')
            print('==================')
            states1 = []
            outputs = []
            states1.append(first_input)
            outputs.append(output_table[first_input])

            state = first_input

            for g in entry:
                state = transition_table[state][g]
                output = output_table[state]
                print('Girdi:', g, 'State:', state, 'Çıktı:', output)
                states1.append(state)
                outputs.append(output)

            output_label.config(text=''.join(outputs))
            states_label.config(text=''.join(states1))

        # Açılır pencere
        new_window = Toplevel(window)
        new_window.config(height=200, width=400)

        input_string = Entry(master=new_window)
        input_string.pack()

        convert_button = Button(master=new_window, text="Göster", command=convert)
        convert_button.pack()

        output_label = Label(master=new_window, text="")
        output_label.pack()

        states_label = Label(master=new_window, text="")
        states_label.pack()

        image_frame = Frame(master=new_window, highlightthickness=1, highlightbackground="blue", height=200, width=400)
        image_frame.pack()

    table_button = Button(master=frame2, text="Tabloyu oluştur", command=create_table)
    table_button.grid(column=column_amount, row=row_amount)


scheme_button = Button(master=frame1, text="Şema oluştur",
                       command=lambda: create_scheme(alphabet_entry.get(), state_entry.get()))
scheme_button.grid(row=2, column=1, padx=15, pady=15, sticky=E)

# Bu penceremizin açık kalmasını sağlar
window.mainloop()
