import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
from steganography import *

class SteganographyApp:
    def __init__(self, master):
        self.master = master
        master.title("Steganography App")

        self.label = tk.Label(master, text=PROMPT)
        self.label.pack()

        self.choice_frame = tk.Frame(master)
        self.choice_frame.pack()

        self.choice = tk.StringVar()
        self.choice.set("1")

        self.encode_radio = tk.Radiobutton(self.choice_frame, text="Encode", variable=self.choice, value="1")
        self.encode_radio.pack(side="left")

        self.decode_radio = tk.Radiobutton(self.choice_frame, text="Decode", variable=self.choice, value="2")
        self.decode_radio.pack(side="left")

        self.execute_button = tk.Button(master, text="Execute", command=self.execute)
        self.execute_button.pack()

    def execute(self):
        choice = self.choice.get()

        if choice == "1":
            self.encode_message()
        elif choice == "2":
            self.decode_message()

    def encode_message(self):
        in_image = filedialog.askopenfilename(initialdir="./", title="Select Image File",
                                              filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
        if not in_image:
            messagebox.showerror("Error", "Please select an image file.")
            return

        in_message = tk.simpledialog.askstring("Input", "Enter the message to encode:")
        if not in_message:
            messagebox.showerror("Error", "Please enter a message.")
            return

        key_str = tk.simpledialog.askstring("Input", "Enter the encryption key:")
        if not key_str:
            messagebox.showerror("Error", "Please enter an encryption key.")
            return

        try:
            key = int(key_str)
        except ValueError:
            messagebox.showerror("Error", "Encryption key must be an integer.")
            return

        out_image = in_image + "-enc.png"

        pixels = get_pixels_from_image(in_image)
        bytestring = encode_message_as_bytestring(in_message, key)
        epixels = encode_pixels_with_message(pixels, bytestring)
        write_pixels_to_image(epixels, out_image)

        messagebox.showinfo("Success", "Message encoded successfully. Output image saved as " + out_image)

    def decode_message(self):
        in_image = filedialog.askopenfilename(initialdir="./", title="Select Image File",
                                              filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
        if not in_image:
            messagebox.showerror("Error", "Please select an image file.")
            return

        key_str = tk.simpledialog.askstring("Input", "Enter the decryption key:")
        if not key_str:
            messagebox.showerror("Error", "Please enter a decryption key.")
            return

        try:
            key = int(key_str)
        except ValueError:
            messagebox.showerror("Error", "Decryption key must be an integer.")
            return

        pixels = get_pixels_from_image(in_image)
        decoded_message = decode_pixels(pixels, key)

        messagebox.showinfo("Decoded Message", "The decoded message is:\n" + decoded_message)


root = tk.Tk()
app = SteganographyApp(root)
root.mainloop()
