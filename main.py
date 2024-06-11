from tkinter import *
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os

class ConvertApp:

    def __init__(self, root):
        self.root = root
        self.file_path = StringVar()

        head_label = Label(root, text="PDF to Text Converter",
                           padx=15,
                           pady=15,
                           font="Helvetica 16 bold",
                           fg="blue",
                           bg="white")
        head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

        file_label = Label(root, text="PDF File Path:", font="Helvetica 12", bg="white")
        file_label.grid(row=2, column=1, pady=10, padx=5)

        self.file_entry = Entry(root, width=40, textvariable=self.file_path, font="Helvetica 12")
        self.file_entry.grid(row=2, column=2, pady=10, padx=5)

        browse_button = Button(root, text="Browse", font="Helvetica 12 bold", bg="blue", fg="white", command=self.browse)
        browse_button.grid(row=2, column=3, pady=10, padx=5)

        convert_button = Button(root, text="Convert", font="Helvetica 12 bold", bg="green", fg="white", command=self.convert_button_clicked)
        convert_button.grid(row=4, column=1, pady=20, padx=5, columnspan=3)

    def browse(self):
        file_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.file_path.set(file_path)

    def convert_button_clicked(self):
        pdf_file_path = self.file_path.get()
        if pdf_file_path:
            try:
                word_file_path = os.path.splitext(pdf_file_path)[0] + ".docx"
                cv = Converter(pdf_file_path)
                cv.convert(word_file_path)
                cv.close()
                messagebox.showinfo("Conversion Complete", "PDF content extracted successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("File Not Selected", "Please select a PDF file.")

def main():
    root = Tk()
    root.geometry("600x300")
    root.resizable(False, False)
    root.title("PDF to Text Converter")
    root.config(background="white")
    app = ConvertApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
