import tkinter as tk
from tkinter import filedialog, Listbox, messagebox
from PyPDF2 import PdfMerger
import os

class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        root.title("PDF Merger App")
        root.geometry("500x550")  # Set the size of the window

        # App name label
        self.app_name_label = tk.Label(root, text="Combine PDFs", font=("Arial", 20))
        self.app_name_label.pack(pady=30)

        # Instructions label title
        self.instructions_label = tk.Label(root, text="Instructions", font=("Arial", 14))
        self.instructions_label.pack(anchor='w', pady=10, padx=30)

        # Instructions label 1
        self.instructions_label1 = tk.Label(root, text="1. Click the 'Select PDFs' button and choose your files.", font=("Arial", 10))
        self.instructions_label1.pack(anchor='w', padx=30)

        # Instructions label 2
        self.instructions_label2 = tk.Label(root, text="2. Re-order the files by clicking and dragging them up and down.", font=("Arial", 10))
        self.instructions_label2.pack(anchor='w', padx=30)

        # Instructions label 3
        self.instructions_label3 = tk.Label(root, text="3. Click the 'Merge PDFs' button and save in your desired location.", font=("Arial", 10))
        self.instructions_label3.pack(anchor='w', padx=30)

        # Listbox to display selected files
        self.file_listbox = Listbox(root, selectmode=tk.SINGLE, width=60, height=10)
        self.file_listbox.pack(pady=20, padx=10)

        # Create GUI elements
        self.select_button = tk.Button(root, padx=20, text="Select PDFs", command=self.select_files)
        self.select_button.pack()

        self.merge_button = tk.Button(root, padx=20, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=20)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

        # Bind events for drag-and-drop in the listbox
        self.file_listbox.bind('<Button-1>', self.on_click)
        self.file_listbox.bind('<B1-Motion>', self.on_drag)

        self.drag_start_index = None

    def select_files(self):
        new_files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if new_files:
            self.file_listbox.insert(tk.END, *new_files)

    def merge_pdfs(self):
        files = self.file_listbox.get(0, tk.END)
        if not files:
            messagebox.showerror("Error", "No files selected!")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not output_path:
            return

        try:
            merger = PdfMerger()
            for pdf in files:
                merger.append(pdf)

            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged into {os.path.basename(output_path)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_click(self, event):
        self.drag_start_index = self.file_listbox.nearest(event.y)

    def on_drag(self, event):
        drag_current_index = self.file_listbox.nearest(event.y)
        if self.drag_start_index is not None and drag_current_index != self.drag_start_index:
            self.file_listbox.insert(drag_current_index, self.file_listbox.get(self.drag_start_index))
            self.file_listbox.delete(self.drag_start_index if drag_current_index > self.drag_start_index else self.drag_start_index + 1)
            self.drag_start_index = drag_current_index

# Create the main window
root = tk.Tk()
app = PdfMergerApp(root)
root.mainloop()
