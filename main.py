import io
import webview
import cairosvg as cairosvg
from scheme import *

golden_ratio = (1 + pow(5,1/2)) / 2
height = 600
width = height * golden_ratio
window = Tk()
window.title("Moore Machine")
window.geometry(f"{int(width)}x{height}")
window.config(pady=15, padx=15,background="#7F7FFF")

# Main Frame

frame = Frame(master=window, highlightthickness=2, highlightbackground="#6666CD")
frame.grid(padx=15, pady=15, row=0, column=0, columnspan=10)

alphabet_label = Label(master=frame, text="Type your alphabet: ")
alphabet_label.grid(row=0, column=0, padx=15, pady=15, sticky=W)

alphabet_entry = Entry(master=frame, highlightthickness=2, highlightbackground="#45458B")
alphabet_entry.grid(row=0, column=1, padx=15, pady=15)

state_label = Label(master=frame, text="Type your state number: ")
state_label.grid(row=1, column=0, padx=15, pady=15, sticky=W)

state_entry = Entry(master=frame, highlightthickness=2, highlightbackground="#45458B")
state_entry.grid(row=1, column=1)

def create_scheme(alphabet, state, master, main_frame):
    Scheme(alphabet=alphabet,states= state,master=master,main_frame= main_frame)

scheme_button = Button(master=frame, text="Create Scheme",
                       command=lambda: create_scheme(alphabet_entry.get(), state_entry.get(), window, frame))
scheme_button.grid(row=2, column=1, padx=15, pady=15, sticky=E)

# Links
image_data = cairosvg.svg2png(url="assets/buttons/linkedin.svg")
image = PIL.Image.open(io.BytesIO(image_data))
new_image = image.resize((25, 25))
linkedin_image = PIL.ImageTk.PhotoImage(new_image)
linkedin_button = Button(master=window,
                       image=linkedin_image,
                       command=lambda: open_web('https://www.linkedin.com/in/murabit-akdogan'))
linkedin_button.grid(padx=10, pady=10, row=1,column=0)

linkedin_label = Label(master=window, text="Murabıt Akdoğan", background="#7F7FFF", foreground="white")
linkedin_label.grid(row=1, column=1, padx=15, pady=15, sticky=W)

image = PIL.Image.open("assets/images/website_icon.png")
new_image = image.resize((25, 25))
website_image = PIL.ImageTk.PhotoImage(new_image)
website_button = Button(master=window,
                       image=website_image,
                       command=lambda: open_web('https://murabit-akdogan.me'))
website_button.grid(padx=10, pady=10,row=2,column=0)

website_label = Label(master=window, text="murabit-akdogan.me", background="#7F7FFF",foreground="white")
website_label.grid(row=2, column=1, padx=15, pady=15, sticky=W)
def open_web(url):
    webview.create_window('Murabıt Akdoğan', url)
    webview.start()

window.mainloop()