import tkinter as tk
from tkinter import filedialog, messagebox
import os

root = tk.Tk()
root.title("File Opener")
apps = []

selected_app = None

def addApp():
    """Add a new application to the list and display it in the frame."""
    global selected_app
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select File', 
                                          filetypes=(("all files", "*.*"),))
    if filename:  
        apps.append(filename)
        print(filename)
    for app in apps:
        label = tk.Label(frame, text=os.path.basename(app), bg='white', fg='black', pady=5, padx=10, relief=tk.RAISED, bd=1)
        label.pack(pady=5)
        label.bind("<Button-1>", lambda e, app=app: selectApp(e, app))

def selectApp(event, app):
    """Highlight the selected application."""
    global selected_app
    selected_app = app
    for widget in frame.winfo_children():
        widget.config(bg='white')
    event.widget.config(bg='lightblue')
    print(f'Selected {app}')

def runApps():
    """Run the selected application."""
    if selected_app:
        os.system(f'open "{selected_app}"')
    else:
        print("No app selected")

def clearApps():
    """Clear all applications from the list and frame."""
    global selected_app
    selected_app = None
    apps.clear()
    for widget in frame.winfo_children():
        widget.destroy()
    print("Cleared all apps")

def showHelp():
    help_text = """How to use File Opener:
1. Click 'Open File' to select a file.
2. The selected files will appear in the white area.
3. Click on a file to select it.
4. Click 'Run App' to open the selected file.
5. Click 'Clear' to remove all files from the white area.
"""
    messagebox.showinfo("Help", help_text)

canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

# Buttons
openFileButton = tk.Button(root, text="Open File", padx=10, pady=5, 
                           fg="black", bg="grey", command=addApp)
openFileButton.pack(side=tk.LEFT, padx=10, pady=20)

runAppsButton = tk.Button(root, text="Run App", padx=10, pady=5, fg="black", bg="grey", command=runApps)
runAppsButton.pack(side=tk.RIGHT, padx=10, pady=20)

clearButton = tk.Button(root, text="Clear", padx=10, pady=5, fg="black", bg="grey", command=clearApps)
clearButton.pack(side=tk.BOTTOM, pady=20)

helpButton = tk.Button(root, text="Help", padx=10, pady=5, fg="black", bg="grey", command=showHelp)
helpButton.pack(side=tk.BOTTOM, pady=20)

root.mainloop()
