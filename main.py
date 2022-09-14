# (c) lava_frai 2022-
# Open GPL

import tkinter as ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import decompressor
import compressor


class App:
    def __init__(self):
        self.root = ttk.Tk()
        self.frm = ttk.Frame(self.root)

        self.runButton = ttk.Button(self.root, text="Decompress", command=self.decompress_file_path)
        self.runButton.pack()
        self.runButton.place(x=180, y=130)

        self.runButton = ttk.Button(self.root, text="Compress", command=self.compress_file_path)
        self.runButton.pack()
        self.runButton.place(x=100, y=130)

    def init_root(self):
        self.root.resizable(False, False)
        self.root.geometry("270x165")

    def init_form(self):
        self.frm.place()
        ttk.Label(self.frm, text="Hello World!").place(x=10, y=10)
        # ttk.Button(self.frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    @staticmethod
    def decompress_file_path() -> None:
        filename: str = fd.askopenfilename()
        if filename is not None:
            print(filename)
            decompressor.unzip(filename, filename[:filename.rindex("/")] + "/uncompress")
            showinfo("Success", "Oke!\nDecompressing successfully finished")

    @staticmethod
    def compress_file_path() -> None:
        filename: str = fd.askopenfilename()
        if filename is not None:
            print(filename)
            compressor.zip(filename, filename + ".zip")
            showinfo("Success", "Oke!\nCompressing successfully finished")

    def run(self):
        self.init_root()
        self.init_form()
        self.root.mainloop()


if __name__ == "__main__":
    App().run()
