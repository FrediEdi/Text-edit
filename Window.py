import tkinter as tk



class AppWindow:
    def __init__(self, root, process_function):

        def file_save():
            user_text = self.text.get("1.0", "end-1c")
            process_function["set"](user_text)
        
        def file_fetch():
            user_text = self.entry.get()
            content = process_function["get"](user_text)
            
            if content is not None:
                self.text.delete("1.0", tk.END);
                self.text.insert("1.0", content)
        


        self.root = root;
        root.title("Text edit");
        root.geometry("400x300");

        self.root.rowconfigure(0, weight=1);
        self.root.rowconfigure(1, weight=9);
        self.root.columnconfigure(0, weight=3);
        self.root.minsize(400, 300);

        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=0)

        self.text = tk.Text(
            root,
        )
        self.text.grid(row=1, column=0, sticky="w");

        self.open = tk.Button(
            root,
            text="Open",
            command=file_fetch
        )
        self.open.grid(row=0, column=0, sticky="w", padx=30);

        self.save = tk.Button(
            root,
            text="Save",
            command=file_save
        )
        self.save.grid(row=0, column=0, sticky="w");
