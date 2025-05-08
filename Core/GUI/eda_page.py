import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class EdaPage:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.current_chart_index = 0
        self.chart_frames = []
        self.image_chart_frames = []
        self.grid_image_labels = []
       
        self.image_paths = [
            # r"Core\GUI\EDA_Plots\heatmap.png",
            # r"Core\GUI\EDA_Plots\weightvsbmi_scatter.png"
            # Add more paths here if you have additional images
        ]
         # Hardcoded list of image paths for Full Plot tabs
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
        # Tabs for visual output (full width)
        self.tab_view = ctk.CTkTabview(self.parent)
        self.tab_view.pack(fill="both", expand=True, padx=10, pady=10)

        # Data Profiling tab
        profiling_tab = self.tab_view.add("Data Profiling")
        profiling_frame = ctk.CTkFrame(profiling_tab, fg_color="#f5f5f5")
        profiling_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.chart_frames.append(profiling_frame)

        # Profiling content frame
        profiling_content = ctk.CTkFrame(profiling_frame, fg_color="#ffffff", corner_radius=10)
        profiling_content.pack(fill="both", expand=True, padx=10, pady=10)

        # Correlations Section
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

        # Imbalances Section
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

        # Distributions Section
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

        # # First tab with 6 grid chart slots
        # self.tab1 = self.tab_view.add("Grid Charts")
        # grid_frame = ctk.CTkFrame(self.tab1)
        # grid_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # # Grid for chart slots
        # grid_container = ctk.CTkFrame(grid_frame)
        # grid_container.pack(fill="both", expand=True)

        # for i in range(6):
        #     chart_frame = ctk.CTkFrame(grid_container, fg_color="#e8f0fe", corner_radius=10, width=200, height=200)
        #     row, col = divmod(i, 3)
        #     chart_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        #     self.chart_frames.append(chart_frame)
        #     # Add a label to hold the image with centered alignment
        #     image_label = ctk.CTkLabel(chart_frame, text="", image=None, fg_color="#e8f0fe")
        #     image_label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label
        #     self.grid_image_labels.append(image_label)
        #     # Load and display image if path exists
        #     if i < len(self.image_paths):
        #         try:
        #             image = Image.open(self.image_paths[i])
        #             # Calculate new size to fit within 200x200 while maintaining aspect ratio
        #             image.thumbnail((200, 200), Image.Resampling.LANCZOS)
        #             # Create a new image with the target size and paste the resized image
        #             new_image = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        #             paste_x = (200 - image.width) // 2
        #             paste_y = (200 - image.height) // 2
        #             new_image.paste(image, (paste_x, paste_y))
        #             ctk_image = ctk.CTkImage(light_image=new_image, dark_image=new_image, size=(200, 200))
        #             image_label.configure(image=ctk_image)
        #         except Exception as e:
        #             print(f"Error loading image {self.image_paths[i]}: {e}")

        # grid_container.grid_rowconfigure((0, 1), weight=1)
        # grid_container.grid_columnconfigure((0, 1, 2), weight=1)

       # Full screen plot tabs
        for i in range(12):
            full_tab = self.tab_view.add(f"Full Plot {i + 1}")
            full_frame = ctk.CTkFrame(full_tab, fg_color="#e8f0fe")
            full_frame.pack(fill="both", expand=True, padx=10, pady=10)
            self.chart_frames.append(full_frame)
            # Add a label to hold the image
            image_label = ctk.CTkLabel(full_frame, text="", image=None, fg_color="#e8f0fe")
            image_label.place(relx=0.5, rely=0.5, anchor="center")
            # Load and display image if path exists
            if i < len(self.full_plot_image_paths):
                try:
                    image = Image.open(self.full_plot_image_paths[i])
                    # Resize image to fit within a reasonable size (e.g., 600x400) while maintaining aspect ratio
                    if i==10:
                         image.thumbnail((1000, 650), Image.Resampling.LANCZOS)
                    image.thumbnail((1000, 750), Image.Resampling.LANCZOS)
                    ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(image.width, image.height))
                    image_label.configure(image=ctk_image)
                except Exception as e:
                    print(f"Error loading full plot image {self.full_plot_image_paths[i]}: {e}")


        # Image tab with grid layout and chart dropdown
        generate_plots = self.tab_view.add("Generate Plots")
        image_main_frame = ctk.CTkFrame(generate_plots)
        image_main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Grid for charts on the left
        image_grid_frame = ctk.CTkFrame(image_main_frame)
        image_grid_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        for i in range(6):
            chart_frame = ctk.CTkFrame(image_grid_frame, fg_color="#e8f0fe", corner_radius=10)
            row, col = divmod(i, 3)
            chart_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.image_chart_frames.append(chart_frame)

        image_grid_frame.grid_rowconfigure((0, 1), weight=1)
        image_grid_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Right frame for chart dropdown in Images tab
        image_right_frame = ctk.CTkFrame(image_main_frame, width=250)
        image_right_frame.pack(side="right", fill="y", padx=(10, 0))

        # Chart type dropdown
        self.chart_dropdown_var = ctk.StringVar(value="Histogram")
        self.chart_dropdown = ctk.CTkOptionMenu(image_right_frame, values=["Bar Chart", "Histogram","Line Chart","Pie Chart"], variable=self.chart_dropdown_var, command=self.toggle_column_dropdown)
        self.chart_dropdown.pack(pady=(20, 5))

        # Column dropdown for histogram (visible by default)
        self.hist_column_label = ctk.CTkLabel(image_right_frame, text="Select Column")
        self.hist_column_label.pack(pady=(5, 5))
        column_values = self.data.columns.tolist() if hasattr(self.data, 'columns') and self.data.columns is not None else []
        self.hist_column_menu = ctk.CTkOptionMenu(image_right_frame, values=column_values)
        self.hist_column_menu.pack(pady=(0, 10))

        # Column dropdown for bar chart (hidden by default)
        self.bar_column_label = ctk.CTkLabel(image_right_frame, text="Select Column for Bar Chart")
        self.bar_column_menu = ctk.CTkOptionMenu(image_right_frame, values=column_values)
        # Column dropdown for bar chart (hidden by default)
        self.pie_column_label = ctk.CTkLabel(image_right_frame, text="Select Column for Bar Chart")
        self.pie_column_menu = ctk.CTkOptionMenu(image_right_frame, values=column_values)
        # Column dropdown for bar chart (hidden by default)
        self.line_column_label = ctk.CTkLabel(image_right_frame, text="Select Column for Bar Chart")
        self.line_column_menu = ctk.CTkOptionMenu(image_right_frame, values=column_values)

        # Generate chart button
        self.generate_chart_button = ctk.CTkButton(image_right_frame, text="Generate Chart",fg_color="#00b300", command=self.generate_chart)
        self.generate_chart_button.pack(pady=(10, 20))

        # Reset charts button
        self.reset_plots_button = ctk.CTkButton(image_right_frame, text="Reset Charts",fg_color="Red", command=self.reset_plots)
        self.reset_plots_button.pack(pady=(10, 30))

    def toggle_column_dropdown(self, choice):
    # Hide all dropdowns and labels initially
        self.hist_column_label.pack_forget()
        self.hist_column_menu.pack_forget()
        self.bar_column_label.pack_forget()
        self.bar_column_menu.pack_forget()
        self.line_column_label.pack_forget()
        self.line_column_menu.pack_forget()
        self.pie_column_label.pack_forget()
        self.pie_column_menu.pack_forget()
        # Show/hide the appropriate column dropdown based on chart type
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
# plot_image_line_plot
# plot_image_pie_chart
    def plot_image_histogram(self):
        column = self.hist_column_menu.get()
        if column not in self.data.columns:
            return
        fig, ax = plt.subplots(figsize=(4, 3))  # Smaller figure size
        self.data[column].hist(ax=ax, color='lightgreen', edgecolor='black')
        ax.set_title(f'Histogram of {column}', fontsize=10)
        plt.tight_layout()  # Ensure layout fits within figure
        self.display_image_plot(fig)


    def plot_image_bar_chart(self):
        column = self.bar_column_menu.get()
        if column not in self.data.columns:
            return
        fig, ax = plt.subplots(figsize=(4, 3))  # Smaller figure size
        self.data[column].value_counts().plot(kind='bar', ax=ax, color='orange', edgecolor='black')
        ax.set_title(f'Bar Chart of {column}', fontsize=10)
        plt.tight_layout()  # Ensure layout fits within figure
        self.display_image_plot(fig)

    def plot_image_line_plot(self):
        column = self.line_column_menu.get()
        if column not in self.data.columns:
            return
        fig, ax = plt.subplots(figsize=(4, 3))  # Smaller figure size
        ax.plot(self.data.index, self.data[column], color='purple', marker='o')
        ax.set_title(f'Line Plot of {column}', fontsize=10)
        ax.set_xlabel('Index', fontsize=8)
        ax.set_ylabel(column, fontsize=8)
        plt.tight_layout()  # Ensure layout fits within figure
        self.display_image_plot(fig)

    def plot_image_pie_chart(self):
        column = self.pie_column_menu.get()
        if column not in self.data.columns:
            return
        fig, ax = plt.subplots(figsize=(4, 3))  # Smaller figure size
        self.data[column].value_counts().plot(kind='pie', ax=ax, colors=['lightcoral', 'lightblue', 'lightgreen', 'orange'], autopct='%1.1f%%', startangle=90)
        ax.set_title(f'Pie Chart of {column}', fontsize=10)
        plt.tight_layout()  # Ensure layout fits within figure
        self.display_image_plot(fig)

    def display_plot(self, fig):
        if self.current_chart_index >= len(self.chart_frames):
            # Add a new tab dynamically
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
            return  # No more space in the Images tab grid

        chart_frame = self.image_chart_frames[self.image_chart_index]

        for widget in chart_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=False, padx=5, pady=5)  # Adjusted packing to prevent overlap
        self.image_chart_index += 1

    def reset_plots(self):
        # Reset indices
        self.current_chart_index = 0
        self.image_chart_index = 0

        # Clear widgets from chart frames
        for frame in self.chart_frames:
            for widget in frame.winfo_children():
                widget.destroy()

        # Clear widgets from image chart frames
        for frame in self.image_chart_frames:
            for widget in frame.winfo_children():
                widget.destroy()