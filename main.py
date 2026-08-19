from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from Window import AppWindow



Datamodel = Path(__file__).parent;
Saves = Datamodel/"saves";

def Get_files(arg : str):

    file_path = filedialog.askopenfilename(
        initialdir=Saves,
        title="Select a File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read();
    return None;


def Set_files(arg : str):

    file_path = filedialog.asksaveasfile(
        initialdir=Saves,
        title="Select a File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        defaultextension=".txt",
        mode='w'
    )

    if file_path:
        file_path.write(arg);
        file_path.close();

def Save_file():
     print("save");

def Create_file():
     print("create");

funclib = {
     "get": Get_files,
     "set": Set_files
}



def main():

    root = tk.Tk();
    AppWindow(root, process_function=funclib);

    root.mainloop();

if __name__ == "__main__":
    main();
