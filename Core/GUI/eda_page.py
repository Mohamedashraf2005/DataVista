import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ydata_profiling import ProfileReport
import seaborn as sns
from tkinter import messagebox

class EdaPage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.df = app.df
        self.chart_frames = []
        self.chart_canvases = []

    def create_ui(self):
        self.eda_frame = ctk.CTkFrame(self.parent, fg_color="#f0f4f8")
        self.eda_frame.pack(fill=ctk.BOTH, expand=True)

        methods_label = ctk.CTkLabel(self.eda_frame, text="Methods used to handle data: Simple Imputer, KNN, Normalize Data, Encoding methods", font=("Arial", 12))
        methods_label.pack(anchor="w", padx=300, pady=5)

        self.eda_left_frame = ctk.CTkFrame(self.eda_frame, fg_color="#ffffff", corner_radius=10, width=int(1200 * 0.65))
        self.eda_left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=False, padx=5, pady=5)
        self.eda_left_frame.pack_propagate(False)

        self.eda_right_frame = ctk.CTkFrame(self.eda_frame, fg_color="#ffffff", corner_radius=10, width=int(1200 * 0.35))
        self.eda_right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=False, padx=5, pady=5)
        self.eda_right_frame.pack_propagate(False)

        self.create_left_frame()
        self.create_right_frame()
        self.generate_default_charts()
        self.generate_insights()

    def create_left_frame(self):
        charts_label = ctk.CTkLabel(self.eda_left_frame, text="Important Charts: Histogram, Heatmap, Pair plot, else", font=("Arial", 15, "bold"))
        charts_label.pack(anchor="w", padx=10, pady=5)

        self.chart_grid_frame = ctk.CTkFrame(self.eda_left_frame, fg_color="#ffffff")
        self.chart_grid_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        for i in range(5):
            chart_frame = ctk.CTkFrame(self.chart_grid_frame, fg_color="#e8f0fe", corner_radius=10)
            row = i // 3
            col = i % 3
            chart_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.chart_frames.append(chart_frame)

        self.chart_grid_frame.grid_rowconfigure(0, weight=1)
        self.chart_grid_frame.grid_rowconfigure(1, weight=1)
        self.chart_grid_frame.grid_columnconfigure(0, weight=1)
        self.chart_grid_frame.grid_columnconfigure(1, weight=1)
        self.chart_grid_frame.grid_columnconfigure(2, weight=1)

    def create_right_frame(self):
        insights_label = ctk.CTkLabel(self.eda_right_frame, text="Insights text\n(correlations ... alert from ydata Profiling)", font=("Arial", 15, "bold"))
        insights_label.pack(anchor="w", padx=30, pady=5)

        self.insights_text = ctk.CTkTextbox(self.eda_right_frame, height=300, wrap="word")
        self.insights_text.pack(fill="x", padx=10, pady=5)
        self.insights_text.insert("end", "Insights will be displayed here after generating the profile report.")

        self.chart_dropdown_var = ctk.StringVar()
        self.chart_dropdown = ctk.CTkComboBox(self.eda_right_frame, values=["Make bar chart relation between two columns", "Make histogram for one column"], variable=self.chart_dropdown_var, state="readonly", corner_radius=10)
        self.chart_dropdown.pack(anchor="w", padx=10, pady=5)

        self.generate_chart_button = ctk.CTkButton(self.eda_right_frame, text="Generate Chart", command=self.generate_chart)
        self.generate_chart_button.pack(anchor="w", padx=10, pady=5)

    # def generate_insights(self):
        # if self.df is not None:
            # profile = ProfileReport(self.df, explorative=True, minimal=True)
            # insights = profile.get_description()
            # self.insights_text.delete("1.0", "end")
            # self.insights_text.insert("end", str(insights))

    def generate_default_charts(self):
        for canvas in self.chart_canvases:
            canvas.get_tk_widget().destroy()
        self.chart_canvases = []

        if self.df is not None:
            num_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
            if len(num_cols) > 0:
                fig, ax = plt.subplots(figsize=(3, 2))
                self.df[num_cols[0]].hist(ax=ax)
                ax.set_title(f"Histogram of {num_cols[0]}")
                canvas = FigureCanvasTkAgg(fig, master=self.chart_frames[0])
                canvas.draw()
                canvas.get_tk_widget().pack(fill="both", expand=True)
                self.chart_canvases.append(canvas)

            # if len(num_cols) > 1:
            #     fig, ax = plt.subplots(figsize=(3, 2))
            #     sns.heatmap(self.df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            #     ax.set_title("Correlation Heatmap")
            #     canvas = FigureCanvasTkAgg(fig, master=self.chart_frames[1])
            #     canvas.draw()
            #     canvas.get_tk_widget().pack(fill="both", expand=True)
            #     self.chart_canvases.append(canvas)

            if len(num_cols) >= 2:
                fig, ax = plt.subplots(figsize=(3, 2))
                ax.scatter(self.df[num_cols[0]], self.df[num_cols[1]])
                ax.set_xlabel(num_cols[0])
                ax.set_ylabel(num_cols[1])
                ax.set_title("Pair Plot")
                canvas = FigureCanvasTkAgg(fig, master=self.chart_frames[2])
                canvas.draw()
                canvas.get_tk_widget().pack(fill="both", expand=True)
                self.chart_canvases.append(canvas)

    def generate_chart(self):
        if self.df is None:
            messagebox.showwarning("Warning", "Please load a dataset first.")
            return

        chart_type = self.chart_dropdown_var.get()
        if chart_type == "Make bar chart relation between two columns":
            columns = list(self.df.columns)
            if len(columns) < 2:
                messagebox.showerror("Error", "Dataset must have at least two columns.")
                return

            col1, col2 = columns[0], columns[1]
            fig, ax = plt.subplots(figsize=(3, 2))
            self.df.groupby(col1)[col2].mean().plot(kind="bar", ax=ax)
            ax.set_title(f"Bar Chart: {col1} vs {col2}")
            canvas = FigureCanvasTkAgg(fig, master=self.chart_frames[3])
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)
            self.chart_canvases.append(canvas)

        elif chart_type == "Make histogram for one column":
            columns = list(self.df.columns)
            if len(columns) < 1:
                messagebox.showerror("Error", "Dataset must have at least one column.")
                return

            num_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
            if len(num_cols) < 1:
                messagebox.showerror("Error", "No numerical columns available for histogram.")
                return

            col = num_cols[0]
            fig, ax = plt.subplots(figsize=(3, 2))
            self.df[col].hist(ax=ax)
            ax.set_title(f"Histogram of {col}")
            canvas = FigureCanvasTkAgg(fig, master=self.chart_frames[4])
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)
            self.chart_canvases.append(canvas)