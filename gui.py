import tkinter as tk
from tkinter import filedialog, messagebox
from main import generate_invoices

class InvoiceGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice PDF Generator")

        tk.Label(root, text="Select Invoice Folder:").grid(row=0, column=0, sticky="w")
        self.folder_entry = tk.Entry(root, width=50)
        self.folder_entry.grid(row=0, column=1)
        tk.Button(root, text="Browse", command=self.browse_folder).grid(row=0, column=2)

        tk.Label(root, text="Select Logo Image:").grid(row=1, column=0, sticky="w")
        self.logo_entry = tk.Entry(root, width=50)
        self.logo_entry.grid(row=1, column=1)
        tk.Button(root, text="Browse", command=self.browse_logo).grid(row=1, column=2)

        tk.Button(root, text="Generate PDFs", command=self.generate, bg="green", fg="white").grid(row=2, column=1, pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0, folder_selected)

    def browse_logo(self):
        logo_selected = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.logo_entry.delete(0, tk.END)
        self.logo_entry.insert(0, logo_selected)

    def generate(self):
        folder = self.folder_entry.get()
        logo = self.logo_entry.get()

        if not folder or not logo:
            messagebox.showerror("Error", "Please select both invoice folder and logo image.")
            return

        try:
            count = generate_invoices(folder, logo)
            messagebox.showinfo("Success", f"Generated {count} PDFs successfully!")
        except Exception as e:
            messagebox.showerror("Failed", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InvoiceGeneratorApp(root)
    root.mainloop()
