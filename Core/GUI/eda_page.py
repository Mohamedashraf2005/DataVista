import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
from tkinter import messagebox
import uuid

class EdaPage:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.current_chart_index = 0
        self.chart_frames = []
        self.image_chart_frames = []
        self.grid_image_labels = []
       
        self.image_paths = []
        self.full_plot_titles = [
            "First Count Plot",
            "Second Count Plot",
            "Columns Distribution",
            "Pair Plot",
            "Smoker Status Bar Chart",
            "Weight vs BMI Scatter",
            "IQR Outlier",
            "Std Dev Outlier",
            "Z-Score Outlier",
            "DBSCAN",
            "Box Plots",
            "Adv Box Plots",
        ]
        self.full_plot_image_paths = [
            r"Core\EDA,ML\EDA_Plots\firstcountplot.png",
            r"Core\EDA,ML\EDA_Plots\secondcountplot.png",
            r"Core\EDA,ML\EDA_Plots\Distofcolumns.png",
            r"Core\EDA,ML\EDA_Plots\Pairplot.png",
            r"Core\EDA,ML\EDA_Plots\BARsmokerstatus.png",
            r"Core\EDA,ML\EDA_Plots\weightvsbmi_scatterplot.png",
            r"Core\EDA,ML\EDA_Plots\IQR_drop.png",
            r"Core\EDA,ML\EDA_Plots\StandardDev_drop.png",
            r"Core\EDA,ML\EDA_Plots\zscore_drop.png",
            r"Core\EDA,ML\EDA_Plots\DBsacn2d.png",
            r"Core\EDA,ML\EDA_Plots\boxplots.png",
            r"Core\EDA,ML\EDA_Plots\Adv._boxplots.png",
        ]
        self.setup_ui()

    def setup_ui(self):
        self.tab_view = ctk.CTkTabview(self.parent)
        self.tab_view.pack(fill="both", expand=True, padx=10, pady=10)

        # Data Profiling Tab
        profiling_tab = self.tab_view.add("Data Profiling")
        profiling_frame = ctk.CTkFrame(profiling_tab, fg_color="#f5f5f5")
        profiling_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.chart_frames.append(profiling_frame)

        profiling_content = ctk.CTkFrame(profiling_frame, fg_color="#ffffff", corner_radius=10)
        profiling_content.pack(fill="both", expand=True, padx=10, pady=10)

        correlation_label = ctk.CTkLabel(profiling_content, text="Correlations", font=("Arial", 16, "bold"), text_color="#333333")
        correlation_label.pack(anchor="w", padx=10, pady=(10, 5))

        correlations = [
            ("BMI is highly overall correlated with WeightInKilograms", "High correlation"),
            ("HeightInMeters is highly overall correlated with Sex and WeightInKilograms", "High correlation"),
            ("Sex is highly overall correlated with HeightInMeters", "High correlation"),
        ]

        for i, (text, status) in enumerate(correlations):
            entry_frame = ctk.CTkFrame(profiling_content, fg_color="#ff4d4d", corner_radius=8)
            entry_frame.pack(fill="x", padx=15, pady=3)
            ctk.CTkLabel(entry_frame, text=text, text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
            ctk.CTkLabel(entry_frame, text=status, text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        imbalance_label = ctk.CTkLabel(profiling_content, text="Imbalances", font=("Arial", 16, "bold"), text_color="#333333")
        imbalance_label.pack(anchor="w", padx=10, pady=(20, 5))

        imbalances = [
            ("HadHeartAttack is highly imbalanced (78.8%)", "Imbalance"),
            ("HadStroke is highly imbalanced (71.8%)", "Imbalance"),
            ("HadSkinCancer is highly imbalanced (60.4%)", "Imbalance"),
            ("HadKidneyDisease is highly imbalanced (74.5%)", "Imbalance"),
            ("HighRiskLastYear is highly imbalanced (75.3%)", "Imbalance"),
            ("BlindOrVisionDifficulty is highly imbalanced (70.6%)", "Imbalance"),
        ]

        for i, (text, status) in enumerate(imbalances):
            entry_frame = ctk.CTkFrame(profiling_content, fg_color="#ff9900", corner_radius=8)
            entry_frame.pack(fill="x", padx=15, pady=3)
            ctk.CTkLabel(entry_frame, text=text, text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
            ctk.CTkLabel(entry_frame, text=status, text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        distribution_label = ctk.CTkLabel(profiling_content, text="Distributions", font=("Arial", 16, "bold"), text_color="#0c9430")
        distribution_label.pack(anchor="w", padx=10, pady=(20, 5))

        distributions = [
            ("GeneralHealth has 754 (15.1%) zeros", "Zeros"),
            ("AgeCategory has 238 (4.8%) zeros", "Zeros"),
        ]

        for i, (text, status) in enumerate(distributions):
            entry_frame = ctk.CTkFrame(profiling_content, fg_color="#b3ffb3", corner_radius=8)
            entry_frame.pack(fill="x", padx=15, pady=3)
            ctk.CTkLabel(entry_frame, text=text, text_color="#333333", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
            ctk.CTkLabel(entry_frame, text=status, text_color="#333333", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # Processing Tab
        processing_tab = self.tab_view.add("Processing")
        processing_frame = ctk.CTkFrame(processing_tab, fg_color="#f5f5f5")
        processing_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.chart_frames.append(processing_frame)

        processing_content = ctk.CTkScrollableFrame(processing_frame, fg_color="#ffffff", corner_radius=10)
        processing_content.pack(fill="both", expand=True, padx=10, pady=10)

        # Handling Missing Values
        missing_values_label = ctk.CTkLabel(processing_content, text="Handling Missing Values", font=("Arial", 16, "bold"), text_color="#333333")
        missing_values_label.pack(anchor="w", padx=10, pady=(10, 5))
        missing_entry = ctk.CTkFrame(processing_content, fg_color="#4da8ff", corner_radius=8)
        missing_entry.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(missing_entry, text="Used SimpleImputer with mean strategy to fill missing values", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(missing_entry, text="Method", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # Duplicate Rows
        duplicates_label = ctk.CTkLabel(processing_content, text="Duplicate Rows", font=("Arial", 16, "bold"), text_color="#333333")
        duplicates_label.pack(anchor="w", padx=10, pady=(20, 5))
        duplicates_entry = ctk.CTkFrame(processing_content, fg_color="#4da8ff", corner_radius=8)
        duplicates_entry.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(duplicates_entry, text="No duplicate rows in the dataset", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(duplicates_entry, text="Status", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # Feature Categorization
        feature_cat_label = ctk.CTkLabel(processing_content, text="Feature Categorization", font=("Arial", 16, "bold"), text_color="#333333")
        feature_cat_label.pack(anchor="w", padx=10, pady=(20, 5))
        
        categorical_entry = ctk.CTkFrame(processing_content, fg_color="#ff9900", corner_radius=8)
        categorical_entry.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(categorical_entry, text="Categorical: ['State', 'Sex', 'GeneralHealth', 'AgeCategory', 'HadDiabetes', 'SmokerStatus', 'ECigaretteUsage', 'RaceEthnicityCategory', 'TetanusLast10Tdap']", 
                    text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(categorical_entry, text="Features", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        numerical_entry = ctk.CTkFrame(processing_content, fg_color="#ff9900", corner_radius=8)
        numerical_entry.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(numerical_entry, text="Critical Numerical: ['HeightInMeters', 'WeightInKilograms', 'BMI', 'HadHeartAttack', 'HadAngina', 'HadStroke', 'HadAsthma', 'HadSkinCancer', 'HadCOPD', 'HadDepressiveDisorder', 'HadKidneyDisease', 'HadArthritis', 'PneumoVaxEver', 'HighRiskLastYear', 'CovidPos']", 
                    text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(numerical_entry, text="Features", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # Feature Scaling
        scaling_label = ctk.CTkLabel(processing_content, text="Feature Scaling", font=("Arial", 16, "bold"), text_color="#333333")
        scaling_label.pack(anchor="w", padx=10, pady=(20, 5))
        scaling_entry = ctk.CTkFrame(processing_content, fg_color="#4da8ff", corner_radius=8)
        scaling_entry.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(scaling_entry, text="Applied StandardScaler to scale numerical features", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(scaling_entry, text="Method", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # Target Variable
        target_label = ctk.CTkLabel(processing_content, text="Target Variable", font=("Arial", 16, "bold"), text_color="#333333")
        target_label.pack(anchor="w", padx=10, pady=(20, 5))
        target_entry = ctk.CTkFrame(processing_content, fg_color="#4da8ff", corner_radius=8)
        target_entry.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(target_entry, text="Target column: 'HadDiabetes'", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(target_entry, text="Target", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # Outlier Detection
        outlier_label = ctk.CTkLabel(processing_content, text="Outlier Detection", font=("Arial", 16, "bold"), text_color="#333333")
        outlier_label.pack(anchor="w", padx=10, pady=(20, 5))
        
        outlier_iqr = ctk.CTkFrame(processing_content, fg_color="#ff4d4d", corner_radius=8)
        outlier_iqr.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(outlier_iqr, text="IQR method: 249 rows", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(outlier_iqr, text="Outliers", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        outlier_std = ctk.CTkFrame(processing_content, fg_color="#ff4d4d", corner_radius=8)
        outlier_std.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(outlier_std, text="Standard Deviation method: 192 rows", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(outlier_std, text="Outliers", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        outlier_zscore = ctk.CTkFrame(processing_content, fg_color="#ff4d4d", corner_radius=8)
        outlier_zscore.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(outlier_zscore, text="Z-score method: 192 rows", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(outlier_zscore, text="Outliers", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # DBSCAN Clustering
        dbscan_label = ctk.CTkLabel(processing_content, text="DBSCAN Clustering (Varying Epsilon)", font=("Arial", 16, "bold"), text_color="#333333")
        dbscan_label.pack(anchor="w", padx=10, pady=(20, 5))
        
        dbscan_05 = ctk.CTkFrame(processing_content, fg_color="#0c9430", corner_radius=8)
        dbscan_05.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(dbscan_05, text="Epsilon = 0.5 → Number of clusters: 3", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(dbscan_05, text="Clustering", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        dbscan_10 = ctk.CTkFrame(processing_content, fg_color="#0c9430", corner_radius=8)
        dbscan_10.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(dbscan_10, text="Epsilon = 1.0 → Number of clusters: 1", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(dbscan_10, text="Clustering", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        dbscan_15 = ctk.CTkFrame(processing_content, fg_color="#0c9430", corner_radius=8)
        dbscan_15.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(dbscan_15, text="Epsilon = 1.5 → Number of clusters: 1", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(dbscan_15, text="Clustering", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # Encoding
        encoding_label = ctk.CTkLabel(processing_content, text="Encoding", font=("Arial", 16, "bold"), text_color="#333333")
        encoding_label.pack(anchor="w", padx=10, pady=(20, 5))
        
        encoding_label_enc = ctk.CTkFrame(processing_content, fg_color="#4da8ff", corner_radius=8)
        encoding_label_enc.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(encoding_label_enc, text="Used Label Encoding for general categorical columns", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(encoding_label_enc, text="Encoding", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        encoding_onehot = ctk.CTkFrame(processing_content, fg_color="#4da8ff", corner_radius=8)
        encoding_onehot.pack(fill="x", padx=15, pady=3)
        ctk.CTkLabel(encoding_onehot, text="Used One-Hot Encoding specifically for the Sex column", text_color="#ffffff", font=("Arial", 12), wraplength=600).pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(encoding_onehot, text="Encoding", text_color="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10, pady=5)

        # Rest of the tabs (unchanged)
        for i in range(12):
            tab_name = self.full_plot_titles[i] if i < len(self.full_plot_titles) else f"Plot {i + 1}"
            full_tab = self.tab_view.add(tab_name)
            full_frame = ctk.CTkFrame(full_tab, fg_color="#e8f0fe")
            full_frame.pack(fill="both", expand=True, padx=10, pady=10)
            self.chart_frames.append(full_frame)
            image_label = ctk.CTkLabel(full_frame, text="", image=None, fg_color="#e8f0fe")
            image_label.place(relx=0.5, rely=0.5, anchor="center")
            if i < len(self.full_plot_image_paths):
                try:
                    image = Image.open(self.full_plot_image_paths[i])
                    if i == 10:
                        image.thumbnail((1000, 650), Image.Resampling.LANCZOS)
                    else:
                        image.thumbnail((1000, 750), Image.Resampling.LANCZOS)
                    ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(image.width, image.height))
                    image_label.configure(image=ctk_image)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to load image: {self.full_plot_image_paths[i]}")
                    image_label.configure(text="Image not available", font=("Arial", 12), text_color="#ff0000")
            else:
                image_label.configure(text="No image available", font=("Arial", 12), text_color="#888888")

        generate_plots = self.tab_view.add("Generate Plots")
        image_main_frame = ctk.CTkFrame(generate_plots)
        image_main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        image_grid_frame = ctk.CTkFrame(image_main_frame)
        image_grid_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        for i in range(6):
            chart_frame = ctk.CTkFrame(image_grid_frame, fg_color="#e8f0fe", corner_radius=10)
            row, col = divmod(i, 3)
            chart_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.image_chart_frames.append(chart_frame)

        image_grid_frame.grid_rowconfigure((0, 1), weight=1)
        image_grid_frame.grid_columnconfigure((0, 1, 2), weight=1)

        image_right_frame = ctk.CTkFrame(image_main_frame, width=250)
        image_right_frame.pack(side="right", fill="y", padx=(10, 0))

        self.chart_dropdown_var = ctk.StringVar(value="Histogram")
        self.chart_dropdown = ctk.CTkOptionMenu(image_right_frame, values=["Bar Chart", "Histogram", "Line Chart", "Pie Chart"], variable=self.chart_dropdown_var, command=self.toggle_column_dropdown)
        self.chart_dropdown.pack(pady=(20, 5))

        self.hist_column_label = ctk.CTkLabel(image_right_frame, text="Select Column")
        self.hist_column_label.pack(pady=(5, 5))
        column_values = self.data.columns.tolist() if hasattr(self.data, 'columns') and self.data.columns is not None else []
        self.hist_column_menu = ctk.CTkOptionMenu(image_right_frame, values=column_values)
        self.hist_column_menu.pack(pady=(0, 10))

        self.bar_column_label = ctk.CTkLabel(image_right_frame, text="Select Column for Bar Chart")
        self.bar_column_menu = ctk.CTkOptionMenu(image_right_frame, values=column_values)
        self.pie_column_label = ctk.CTkLabel(image_right_frame, text="Select Column for Pie Chart")
        self.pie_column_menu = ctk.CTkOptionMenu(image_right_frame, values=column_values)
        self.line_column_label = ctk.CTkLabel(image_right_frame, text="Select Column for Line Chart")
        self.line_column_menu = ctk.CTkOptionMenu(image_right_frame, values=column_values)

        self.generate_chart_button = ctk.CTkButton(image_right_frame, text="Generate Chart", fg_color="#00b300", command=self.generate_chart)
        self.generate_chart_button.pack(pady=(10, 20))

        self.reset_plots_button = ctk.CTkButton(image_right_frame, text="Reset Charts", fg_color="Red", command=self.reset_plots)
        self.reset_plots_button.pack(pady=(10, 30))

    def toggle_column_dropdown(self, choice):
        self.hist_column_label.pack_forget()
        self.hist_column_menu.pack_forget()
        self.bar_column_label.pack_forget()
        self.bar_column_menu.pack_forget()
        self.line_column_label.pack_forget()
        self.line_column_menu.pack_forget()
        self.pie_column_label.pack_forget()
        self.pie_column_menu.pack_forget()
        if choice == "Histogram":
            self.hist_column_label.pack(pady=(5, 5))
            self.hist_column_menu.pack(pady=(0, 10))
        elif choice == "Bar Chart":
            self.bar_column_label.pack(pady=(5, 5))
            self.bar_column_menu.pack(pady=(0, 10))
        elif choice == "Line Chart":
            self.line_column_label.pack(pady=(5, 5))
            self.line_column_menu.pack(pady=(0, 10))
        elif choice == "Pie Chart":
            self.pie_column_label.pack(pady=(5, 5))
            self.pie_column_menu.pack(pady=(0, 10))

    def generate_chart(self):
        chart_type = self.chart_dropdown_var.get()
        if chart_type == "Histogram":
            self.plot_image_histogram()
        elif chart_type == "Bar Chart":
            self.plot_image_bar_chart()
        elif chart_type == "Line Chart":
            self.plot_image_line_plot()
        elif chart_type == "Pie Chart":
            self.plot_image_pie_chart()

    def plot_image_histogram(self):
        column = self.hist_column_menu.get()
        if column not in self.data.columns:
            return
        fig, ax = plt.subplots(figsize=(4, 3))
        self.data[column].hist(ax=ax, color='lightgreen', edgecolor='black')
        ax.set_title(f'Histogram of {column}', fontsize=10)
        plt.tight_layout()
        self.display_image_plot(fig)

    def plot_image_bar_chart(self):
        column = self.bar_column_menu.get()
        if column not in self.data.columns:
            return
        fig, ax = plt.subplots(figsize=(4, 3))
        self.data[column].value_counts().plot(kind='bar', ax=ax, color='orange', edgecolor='black')
        ax.set_title(f'Bar Chart of {column}', fontsize=10)
        plt.tight_layout()
        self.display_image_plot(fig)

    def plot_image_line_plot(self):
        column = self.line_column_menu.get()
        if column not in self.data.columns:
            return
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.plot(self.data.index, self.data[column], color='purple', marker='o')
        ax.set_title(f'Line Plot of {column}', fontsize=10)
        ax.set_xlabel('Index', fontsize=8)
        ax.set_ylabel(column, fontsize=8)
        plt.tight_layout()
        self.display_image_plot(fig)

    def plot_image_pie_chart(self):
        column = self.pie_column_menu.get()
        if column not in self.data.columns:
            return
        fig, ax = plt.subplots(figsize=(4, 3))
        self.data[column].value_counts().plot(kind='pie', ax=ax, colors=['lightcoral', 'lightblue', 'lightgreen', 'orange'], autopct='%1.1f%%', startangle=90)
        ax.set_title(f'Pie Chart of {column}', fontsize=10)
        plt.tight_layout()
        self.display_image_plot(fig)

    def display_plot(self, fig):
        if self.current_chart_index >= len(self.chart_frames):
            new_tab = self.tab_view.add(f"Plot {self.current_chart_index + 1}")
            new_frame = ctk.CTkFrame(new_tab, fg_color="#e8f0fe")
            new_frame.pack(fill="both", expand=False, padx=0, pady=0)
            self.chart_frames.append(new_frame)

        chart_frame = self.chart_frames[self.current_chart_index]

        for widget in chart_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        self.current_chart_index += 1

    def display_image_plot(self, fig):
        if not hasattr(self, 'image_chart_index'):
            self.image_chart_index = 0

        if self.image_chart_index >= len(self.image_chart_frames):
            return

        chart_frame = self.image_chart_frames[self.image_chart_index]

        for widget in chart_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=False, padx=5, pady=5)
        self.image_chart_index += 1

    def reset_plots(self):
        self.current_chart_index = 0
        self.image_chart_index = 0

        for frame in self.chart_frames:
            for widget in frame.winfo_children():
                widget.destroy()

        for frame in self.image_chart_frames:
            for widget in frame.winfo_children():
                widget.destroy()