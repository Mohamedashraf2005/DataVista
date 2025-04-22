import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
from dataset_page import DatasetPage
from eda_page import EdaPage

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class mainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DataAnalysis Interface")
        self.root.geometry("1200x640+250+100")
        self.root.resizable(False, False)

        self.df = None
        self.current_page = None

        self.create_top_frame()
        self.create_main_frame()
        self.show_dataset_page()

    def create_top_frame(self):
        self.top_frame = ctk.CTkFrame(self.root, fg_color="#f0f4f8")
        self.top_frame.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=5)

        self.btn_dataset = ctk.CTkButton(self.top_frame, text="DataSet", fg_color="#1a73e8", text_color="white", font=("Arial", 15, "bold"), corner_radius=10, command=self.show_dataset_page)
        self.btn_dataset.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.X)

        self.btn_eda = ctk.CTkButton(self.top_frame, text="EDA", fg_color="#e8f0fe", text_color="#1a73e8", font=("Arial", 15), corner_radius=10, command=self.show_eda_page)
        self.btn_eda.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.X)

        self.btn_ml = ctk.CTkButton(self.top_frame, text="ML Model", fg_color="#e8f0fe", text_color="#1a73e8", font=("Arial", 15), corner_radius=10)
        self.btn_ml.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.X)

        self.btn_about = ctk.CTkButton(self.top_frame, text="About Project (optional)", fg_color="#e8f0fe", text_color="#1a73e8", font=("Arial", 15), corner_radius=10)
        self.btn_about.pack(side=ctk.LEFT, padx=10, expand=True, fill=ctk.X)

    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#f0f4f8")
        self.main_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
        self.main_frame.pack_propagate(False)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_dataset_page(self):
        self.clear_main_frame()
        self.current_page = DatasetPage(self.main_frame, self)
        self.current_page.create_ui()

    def show_eda_page(self):
        if self.df is None:
            messagebox.showwarning("Warning", "Please load a dataset first.")
            return
        self.clear_main_frame()
        self.current_page = EdaPage(self.main_frame, self)
        self.current_page.create_ui()

    def upload_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                if self.current_page and isinstance(self.current_page, DatasetPage):
                    self.current_page.update_ui(self.df, file_path.split("/")[-1])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")
        else:
            messagebox.showwarning("Warning", "No file selected")

if __name__ == "__main__":
    root = ctk.CTk()
    app = mainApp(root)
    root.mainloop()