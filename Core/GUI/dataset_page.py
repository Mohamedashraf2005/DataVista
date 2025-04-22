import customtkinter as ctk
from tkinter import ttk
import pandas as pd

class DatasetPage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.df = None
        self.summary_labels = {}

    def create_ui(self):
        self.dataset_frame = ctk.CTkFrame(self.parent, fg_color="#f0f4f8")
        self.dataset_frame.pack(fill=ctk.BOTH, expand=True)

        self.create_left_frame()
        self.create_right_frame()

    def create_left_frame(self):
        self.left_frame = ctk.CTkFrame(self.dataset_frame, fg_color="#ffffff", corner_radius=10, width=int(1024 * 0.75))
        self.left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=False, padx=5, pady=5)
        self.left_frame.pack_propagate(False)

        self.label_dataset_name = ctk.CTkLabel(self.left_frame, text="Name of the DataSet", fg_color="#ffffff", font=("Arial", 15, "bold"))
        self.label_dataset_name.pack(anchor="w", padx=10, pady=5)

        self.load_button = ctk.CTkButton(self.left_frame, text="Upload CSV", command=self.app.upload_csv)
        self.load_button.pack(anchor="w", padx=10, pady=5)

        self.filter_label = ctk.CTkLabel(self.left_frame, text="Choose and apply filter to columns", fg_color="#ffffff", font=("Arial", 15, "bold"))
        self.filter_label.pack(anchor="w", padx=10, pady=5)

        self.filter_var = ctk.StringVar()
        self.filter_menu = ctk.CTkComboBox(self.left_frame, values=["Filter Options"], variable=self.filter_var, state="readonly", corner_radius=10)
        self.filter_menu.set("Filter Options")
        self.filter_menu.pack(anchor="w", padx=10, pady=5)

        self.data_table_frame = ctk.CTkFrame(self.left_frame, fg_color="#ffffff", height=400)
        self.data_table_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        self.data_table = ttk.Treeview(self.data_table_frame)
        self.scroll_x = ttk.Scrollbar(self.data_table_frame, orient="horizontal", command=self.data_table.xview)
        self.scroll_y = ttk.Scrollbar(self.data_table_frame, orient="vertical", command=self.data_table.yview)
        self.data_table.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.data_table.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.scroll_x.grid(row=1, column=0, sticky="ew")

        self.data_table_frame.grid_rowconfigure(0, weight=1)
        self.data_table_frame.grid_columnconfigure(0, weight=1)

    def create_right_frame(self):
        self.right_frame = ctk.CTkFrame(self.dataset_frame, fg_color="#ffffff", corner_radius=10, width=int(1200 * 0.45))
        self.right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=False, padx=5, pady=5)
        self.right_frame.pack_propagate(False)

        summary_title = ctk.CTkLabel(self.right_frame, text="Dataset Summary", fg_color="#ffffff", font=("Arial", 18, "bold"))
        summary_title.pack(anchor="w", padx=10, pady=5)

        sections = [
            "Overview", "Shape", "Missing Values", "Duplicates", 
            "Data Types", "Stats", "Unique Values", "Critical Columns"
        ]

        for title in sections:
            section_frame = ctk.CTkFrame(self.right_frame, fg_color="#f9f9f9", corner_radius=10)
            section_frame.pack(fill='x', pady=5, padx=10)

            label_title = ctk.CTkLabel(section_frame, text=title, font=("Arial", 14, "bold"), text_color="#1a73e8")
            label_title.pack(anchor='w', padx=10, pady=(5, 0))

            label_data = ctk.CTkLabel(section_frame, text="", font=("Arial", 12), wraplength=350, justify="left")
            label_data.pack(anchor='w', padx=10, pady=(0, 5))

            self.summary_labels[title] = label_data

    def update_ui(self, df, dataset_name):
        self.df = df
        self.label_dataset_name.configure(text=dataset_name)
        self.update_filter_options()
        self.display_data_table()
        self.update_summary()

    def update_filter_options(self):
        columns = list(self.df.columns)
        self.filter_menu.configure(values=columns)
        if columns:
            self.filter_menu.set(columns[0])

    def display_data_table(self):
        self.data_table.delete(*self.data_table.get_children())
        self.data_table["columns"] = list(self.df.columns)
        self.data_table["show"] = "headings"

        for col in self.df.columns:
            self.data_table.heading(col, text=col)
            self.data_table.column(col, width=100, anchor="center")

        for _, row in self.df.iterrows():
            self.data_table.insert("", "end", values=list(row))

    def update_summary(self):
        if self.df is not None:
            self.summary_labels["Overview"].configure(text="Dataset loaded successfully.")
            self.summary_labels["Shape"].configure(text=str(self.df.shape))
            self.summary_labels["Missing Values"].configure(text=str(self.df.isnull().sum()))
            self.summary_labels["Duplicates"].configure(text=str(self.df.duplicated().sum()))
            self.summary_labels["Data Types"].configure(text=str(self.df.dtypes))
            self.summary_labels["Stats"].configure(text=str(self.df.describe(include='all')))
            self.summary_labels["Unique Values"].configure(text=str(self.df.nunique()))
            critical_cols = self.df.columns[self.df.isnull().mean() > 0.5].tolist()
            self.summary_labels["Critical Columns"].configure(text=str(critical_cols) if critical_cols else "No critical columns")