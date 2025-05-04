import customtkinter as ctk
from tkinter import ttk
import pandas as pd
from PIL import Image

class DatasetPage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.df = None
        self.summary_labels = {}

    def create_ui(self):
        self.dataset_frame = ctk.CTkFrame(self.parent, fg_color="#f0f4f8")
        self.dataset_frame.pack(fill=ctk.BOTH, expand=True)

        # Get screen width to set fixed ratios
        screen_width = self.parent.winfo_screenwidth()
        left_width = int(screen_width * 0.6)  # Max 60% for left frame
        right_width = int(screen_width * 0.4)  # Max 40% for right frame

        self.create_left_frame(left_width)
        self.create_right_frame(right_width)

    def create_left_frame(self, max_width):
        self.left_frame = ctk.CTkFrame(self.dataset_frame, fg_color="#ffffff", corner_radius=10)
        self.left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=False, padx=5, pady=5)
        self.left_frame.configure(width=max_width)  # Fixed max width at 60%
        self.left_frame.pack_propagate(False)

        # Header frame for upload button, dataset name, and image
        self.header_frame = ctk.CTkFrame(self.left_frame, fg_color="#ffffff")
        self.header_frame.pack(fill="x", padx=10, pady=5)

        self.load_button = ctk.CTkButton(self.header_frame, text="Upload CSV", command=self.app.upload_csv)
        self.load_button.pack(side=ctk.RIGHT, padx=(0, 10))

        # Create a subframe to hold the label and image for better alignment
        self.label_image_frame = ctk.CTkFrame(self.header_frame, fg_color="#ffffff")
        self.label_image_frame.pack(side=ctk.LEFT, expand=True, padx=(250, 40))

        # Load and add the image
        image_path = "Core/GUI/dataset_icon.png"  # Use forward slashes for cross-platform compatibility
        try:
            dataset_image = ctk.CTkImage(light_image=Image.open(image_path), size=(80, 80))  # Adjust size as needed
            self.image_label = ctk.CTkLabel(self.label_image_frame, image=dataset_image, text="")
            self.image_label.pack(side=ctk.RIGHT, padx=(0, 5))  # Small padding between image and text
        except Exception as e:
            print(f"Error loading image: {e}")

        # Dataset name label
        self.label_dataset_name = ctk.CTkLabel(
            self.label_image_frame,
            text="PlotTwist",
            fg_color="#ffffff",
            font=("comic sans ms", 18, "bold")
        )
        self.label_dataset_name.pack(side=ctk.RIGHT)

        # Data table frame (fixed height to fit 25 rows)
        self.data_table_frame = ctk.CTkFrame(self.left_frame, fg_color="#ffffff", height=200)
        self.data_table_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
        self.data_table_frame.pack_propagate(False)  # Prevent resizing based on content

        self.data_table = ttk.Treeview(self.data_table_frame, show="headings")
        self.scroll_x = ttk.Scrollbar(self.data_table_frame, orient="horizontal", command=self.data_table.xview)
        self.data_table.configure(xscrollcommand=self.scroll_x.set)

        self.data_table.grid(row=0, column=0, sticky="nsew")
        self.scroll_x.grid(row=1, column=0, sticky="ew")

        self.data_table_frame.grid_rowconfigure(0, weight=1)
        self.data_table_frame.grid_columnconfigure(0, weight=1)

        # Filter section at the bottom
        self.filter_section_frame = ctk.CTkFrame(self.left_frame, fg_color="#ffffff")
        self.filter_section_frame.pack(fill="x", padx=10, pady=(10, 5), side=ctk.BOTTOM)

        self.filter_label = ctk.CTkLabel(self.filter_section_frame, text="Choose and apply filter to columns", fg_color="#ffffff", font=("Arial", 15, "bold"))
        self.filter_label.pack(anchor="w", padx=10, pady=(5, 0))

        self.filter_var = ctk.StringVar()
        self.filter_menu = ctk.CTkComboBox(self.filter_section_frame, values=["Filter Options"], variable=self.filter_var, state="readonly", corner_radius=10)
        self.filter_menu.set("Filter Options")
        self.filter_menu.pack(anchor="w", padx=10, pady=(0, 5))

        self.filter_input_frame = ctk.CTkFrame(self.filter_section_frame, fg_color="#ffffff")
        self.filter_input_frame.pack(anchor="w", pady=5)

        self.filter_entry = ctk.CTkEntry(self.filter_input_frame, placeholder_text="Enter filter value")
        self.filter_entry.pack(side=ctk.LEFT, padx=(0, 5), pady=5)

        self.apply_filter_button = ctk.CTkButton(self.filter_input_frame, text="Apply Filter", command=self.apply_filter)
        self.apply_filter_button.pack(side=ctk.LEFT, pady=5)

    def create_right_frame(self, max_width):
        self.right_frame = ctk.CTkFrame(self.dataset_frame, fg_color="#ffffff", corner_radius=10)
        self.right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=False, padx=5, pady=5)
        self.right_frame.configure(width=max_width)  # Fixed max width at 40%
        self.right_frame.pack_propagate(False)

        self.canvas = ctk.CTkCanvas(self.right_frame, bg="#ffffff")
        self.scrollbar = ttk.Scrollbar(self.right_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color="#ffffff")

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Bind configure event to update scrollregion
        def update_scrollregion(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.scrollable_frame.bind("<Configure>", update_scrollregion)

        self.canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        self.scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        summary_title = ctk.CTkLabel(self.scrollable_frame, text="Dataset Summary", fg_color="#ffffff", font=("Arial", 18, "bold"))
        summary_title.pack(anchor="w", padx=10, pady=5)

        sections = [
            "Overview", "Shape", "Missing Values", "Duplicates", 
            "Data Types", "Unique Values", "Critical Columns"
        ]

        for title in sections:
            section_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="#f9f9f9", corner_radius=10)
            section_frame.pack(fill='x', pady=5, padx=10)

            label_title = ctk.CTkLabel(section_frame, text=title, font=("Arial", 14, "bold"), text_color="#1a73e8")
            label_title.pack(anchor='w', padx=10, pady=(5, 0))

            label_data = ctk.CTkLabel(section_frame, text="", font=("Arial", 12), wraplength=300, justify="left")
            label_data.pack(anchor='w', padx=10, pady=(0, 5))

            self.summary_labels[title] = label_data

    def apply_filter(self):
        if self.df is None:
            return
        column = self.filter_var.get()
        filter_value = self.filter_entry.get()
        if column and filter_value and column != "Filter Options":
            try:
                filtered_df = self.df[self.df[column].astype(str).str.contains(filter_value, case=False, na=False)]
                self.display_data_table(filtered_df)
            except Exception as e:
                print(f"Filter error: {e}")

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

    def display_data_table(self, df=None):
        self.data_table.delete(*self.data_table.get_children())
        display_df = df if df is not None else self.df
        if display_df is None:
            return
        display_df = display_df.head(34)  # Display exactly 25 rows
        self.data_table["columns"] = list(display_df.columns)
        self.data_table["show"] = "headings"

        # Get the available width of the data_table_frame
        frame_width = self.data_table_frame.winfo_width()
        if frame_width <= 1:  # If not yet rendered, estimate based on left_frame
            frame_width = int(self.left_frame.winfo_width() * 0.9)  # 90% of left_frame

        num_columns = len(display_df.columns)
        if num_columns == 0:
            return

        # Calculate dynamic column width
        min_col_width = 80  # Minimum column width
        max_col_width = 200  # Maximum column width
        col_width = min(max_col_width, max(min_col_width, frame_width // num_columns))

        # Set column headings and widths
        for col in display_df.columns:
            self.data_table.heading(col, text=col)
            max_content_length = max(len(str(col)), max([len(str(x)) for x in display_df[col].head(25)], default=0))
            content_width = max_content_length * 8
            final_width = min(max_col_width, max(min_col_width, content_width))
            final_width = min(final_width, col_width)
            self.data_table.column(col, width=final_width, anchor="center", stretch=False)

        # Insert data rows
        for _, row in display_df.iterrows():
            self.data_table.insert("", "end", values=list(row))

        # Ensure horizontal scrolling is enabled
        self.data_table.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_x.grid(row=1, column=0, sticky="ew")

    def update_summary(self):
        if self.df is None:
            return
        self.summary_labels["Overview"].configure(text="Dataset loaded successfully.")
        self.summary_labels["Shape"].configure(text=str(self.df.shape))
        self.summary_labels["Missing Values"].configure(text=str(self.df.isnull().sum()))
        self.summary_labels["Duplicates"].configure(text=str(self.df.duplicated().sum()))
        self.summary_labels["Data Types"].configure(text=str(self.df.dtypes))
        self.summary_labels["Unique Values"].configure(text=str(self.df.nunique()))
        critical_cols = self.df.columns[self.df.isnull().mean() > 0.5].tolist()
        self.summary_labels["Critical Columns"].configure(text=str(critical_cols) if critical_cols else "No critical columns")