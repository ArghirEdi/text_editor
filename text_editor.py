import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def open_file():
    """Open a file and display its content in the text widget."""
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    # Clear the existing content in the text widget
    text.delete(1.0, tk.END)

    try:
        # Read and insert the content of the selected file into the text widget
        with open(filepath, "r") as f:
            content = f.read()
            text.insert(tk.END, content)

        # Update the window title and status bar
        window.title(f"Text Editor - {filepath}")
        update_status_bar(f"File opened: {filepath}")

    except Exception as e:
        # Display an error message and update the status bar
        messagebox.showerror("Error", f"Unable to open file: {e}")
        update_status_bar("File open failed.")

def save_file():
    """Save the content of the text widget to a file."""
    filepath = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    try:
        # Write the content of the text widget to the selected file
        with open(filepath, "w") as f:
            content = text.get(1.0, tk.END)
            f.write(content)

        # Update the window title and status bar
        window.title(f"Text Editor - {filepath}")
        update_status_bar(f"File saved: {filepath}")

    except Exception as e:
        # Display an error message and update the status bar
        messagebox.showerror("Error", f"Unable to save file: {e}")
        update_status_bar("File save failed.")

def update_status_bar(message):
    """Update the status bar with the provided message."""
    statusbar.config(text=message)

def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        window.destroy()

def about():
    messagebox.showinfo("About", "Simple Text Editor\nVersion 2.0\n(C) 2024 Arghir Eduard")

def toggle_theme():
    current_background = text.cget("background")
    colors = ["white", "black", "#B1DDC6", "#e0f0e0", "#e0e0e0", "#e0e0f0", "#f0e0e0", "#d0c7d0", "#c0d5e0", "#c6d7d0"]

    # Find the index of the current background color in the list
    current_index = colors.index(current_background)

    # Calculate the next index using modulo to wrap around
    next_index = (current_index + 1) % len(colors)

    # Set the next background color
    if colors[next_index] == "black":
        text.config(bg=colors[next_index], fg="white")
    else:
        text.config(bg=colors[next_index], fg="black")
    
    

def main():
    """Create and run the main application."""
    global window, text, statusbar

    window = tk.Tk()
    window.title("Text Editor")
    window.iconbitmap("favicon.ico")

    # Create Menu Bar
    menubar = tk.Menu(window)

    # File Menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
    file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
    file_menu.add_command(label="Save As", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_app)
    menubar.add_cascade(label="File", menu=file_menu)

    # Edit Menu (You can add more options)
    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"), accelerator="Ctrl+X")
    edit_menu.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"), accelerator="Ctrl+C")
    edit_menu.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"), accelerator="Ctrl+V")
    edit_menu.add_separator()
    edit_menu.add_command(label="Toggle Theme", command=toggle_theme, accelerator="CTRL+T")
    menubar.add_cascade(label="Edit", menu=edit_menu)

    # Help Menu
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=help_menu)

    window.config(menu=menubar)

    # Create Text Widget with Scrollbar
    text = scrolledtext.ScrolledText(window, wrap=tk.WORD, font="Helvetica 12")
    text.pack(expand=True, fill=tk.BOTH)

    # Status Bar
    statusbar = tk.Label(window, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, padx=8, pady=5)
    statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    # Bind keyboard shortcuts
    window.bind("<Control-o>", lambda x: open_file())
    window.bind("<Control-s>", lambda x: save_file())
    window.bind("<Control-t>", lambda x: toggle_theme())

    window.mainloop()

if __name__ == "__main__":
    main()
