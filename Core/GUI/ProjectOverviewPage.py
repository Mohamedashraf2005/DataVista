import customtkinter as ctk
import webbrowser

class ProjectOverviewPage:
    """A class to create the Project Overview page UI for the Plot Twist project."""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.theme = {
            "primary": "#1a73e8",
            "secondary": "#ffffff",
            "background": "#f5f7fa",
            "text": "#333333",
            "hover": "#e8f0fe"
        }

    def create_ui(self):
        """Create the main UI for the Project Overview page."""
        # Main scrollable frame
        self.main_frame = ctk.CTkScrollableFrame(self.parent, fg_color=self.theme["background"])
        self.main_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Create sections
        self._create_project_overview()
        self._create_columns_layout()

    def _create_project_overview(self):
        """Create the Project Overview section."""
        overview_frame = ctk.CTkFrame(self.main_frame, fg_color=self.theme["secondary"], corner_radius=12)
        overview_frame.pack(fill="x", padx=10, pady=10)

        project_title = ctk.CTkLabel(
            overview_frame,
            text="Plot Twist-Project Overview",
            font=("Roboto", 20, "bold"),
            text_color=self.theme["primary"]
        )
        project_title.pack(anchor="w", padx=20, pady=(15, 5))

        project_desc = ctk.CTkLabel(
            overview_frame,
            text=(
                "Affiliated with the Data Analysis course at the Faculty of Artificial Intelligence, Menoufia University.\n"
                "This project analyzes a patient dataset through Exploratory Data Analysis (EDA), interactive visualizations, "
                "and machine learning (ML) classification.\n\n"
                "• Goals: Uncover insights, visualize trends, and predict Diabetes-related health outcomes using an interactive GUI.\n"
                "• Dataset: Kaggle patient data with features like Sex, Age, BMI, and health conditions.\n"
                "• Tools: Python, Pandas (data analysis), Scikit-learn (ML), CustomTkinter (GUI)."
            ),
            font=("Roboto", 14),
            text_color=self.theme["text"],
            wraplength=1100,
            justify="left"
        )
        project_desc.pack(anchor="w", padx=20, pady=(5, 15))

    def _create_columns_layout(self):
        """Create the two-column layout for Contributors, Key Learnings, and Contact."""
        columns_frame = ctk.CTkFrame(self.main_frame, fg_color=self.theme["background"])
        columns_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Left Column: Project Contributors
        self._create_contributors(columns_frame)

        # Right Column: Key Learnings and Contact & Support
        self._create_right_column(columns_frame)

    def _create_contributors(self, parent):
        """Create the Project Contributors section."""
        left_frame = ctk.CTkFrame(parent, fg_color=self.theme["secondary"], corner_radius=12)
        left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=(0, 5))

        contributors_title = ctk.CTkLabel(
            left_frame,
            text="Project Contributors",
            font=("Roboto", 18, "bold"),
            text_color=self.theme["primary"]
        )
        contributors_title.pack(anchor="w", padx=20, pady=(15, 5))

        contributors = [
            ("Mohamed Ashraf", "EDA, ML modeling"),
            ("Eman Hekal", "GUI design, Visualizations"),
            ("Ali Fathy", "GUI, Data preprocessing"),
            ("Mariam Ahmed", "ML modeling, Visualizations"),
            ("Mohammed Ahmed", "EDA, ML evaluation"),
            ("Youssef Ahmed", "EDA"),
            ("Kareem Mousa", "Data preprocessing")
        ]

        for name, role in contributors:
            contributor_label = ctk.CTkLabel(
                left_frame,
                text=f"• {name}: {role}",
                font=("Roboto", 14),
                text_color=self.theme["text"],
                wraplength=500,
                justify="left"
            )
            contributor_label.pack(anchor="w", padx=20, pady=2)
            contributor_label.bind("<Enter>", lambda e, l=contributor_label: l.configure(text_color=self.theme["hover"]))
            contributor_label.bind("<Leave>", lambda e, l=contributor_label: l.configure(text_color=self.theme["text"]))

        thanks_label = ctk.CTkLabel(
            left_frame,
            text="• Thanks: ENG/Rokia for guidance, Kaggle for dataset.",
            font=("Roboto", 14),
            text_color=self.theme["text"],
            wraplength=500,
            justify="left"
        )
        thanks_label.pack(anchor="w", padx=20, pady=(5, 15))

    def _create_right_column(self, parent):
        """Create the Key Learnings and Contact & Support sections."""
        right_frame = ctk.CTkFrame(parent, fg_color=self.theme["secondary"], corner_radius=12)
        right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=(5, 0))

        # Key Learnings
        learnings_title = ctk.CTkLabel(
            right_frame,
            text="Key Learnings",
            font=("Roboto", 18, "bold"),
            text_color=self.theme["primary"]
        )
        learnings_title.pack(anchor="w", padx=20, pady=(15, 5))

        learnings = [
            "Data Analysis: Applied EDA to uncover patterns and correlations.",
            "Interactive Visuals: Built dynamic GUI charts (histograms, bar, line, pie).",
            "ML Classification: Trained and evaluated models for Diabetes prediction.",
            "GUI Design: Created user-friendly interfaces with responsive layouts and modern styling.",
            "Tools Proficiency: Gained expertise in Python, Pandas, Scikit-learn, and CustomTkinter."
        ]

        for learning in learnings:
            learning_label = ctk.CTkLabel(
                right_frame,
                text=f"• {learning}",
                font=("Roboto", 14),
                text_color=self.theme["text"],
                wraplength=500,
                justify="left"
            )
            learning_label.pack(anchor="w", padx=20, pady=2)

        # Contact & Support
        contact_title = ctk.CTkLabel(
            right_frame,
            text="Contact & Support",
            font=("Roboto", 18, "bold"),
            text_color=self.theme["primary"]
        )
        contact_title.pack(anchor="w", padx=20, pady=(20, 5))

        contacts = [
            "mohamedachrvf@gmail.com",
            "emanhekal159@gmail.com",
            "ali.fathy.ali20@gmail.com",
            "mariamsalama369@gmail.com",
            "mohmedahmedali159@gmail.com",
            "Youssef112005@gmail.com",
            "x5247701478x@gmail.com"
        ]

        for email in contacts:
            email_label = ctk.CTkLabel(
                right_frame,
                text=f"• {email}",
                font=("Roboto", 14),
                text_color=self.theme["primary"],
                wraplength=500,
                justify="left",
                cursor="hand2"
            )
            email_label.pack(anchor="w", padx=20, pady=2)
            email_label.bind("<Button-1>", lambda e, em=email: webbrowser.open(f"mailto:{em}"))
            email_label.bind("<Enter>", lambda e, l=email_label: l.configure(text_color=self.theme["hover"]))
            email_label.bind("<Leave>", lambda e, l=email_label: l.configure(text_color=self.theme["primary"]))

        # contact_desc = ctk.CTkLabel(
        #     right_frame,
        #     text="For further information or collaboration opportunities, please reach out to us via email.",
        #     font=("Roboto", 14),
        #     text_color=self.theme["text"],
        #     wraplength=500,
        #     justify="left"
        # )
        # contact_desc.pack(anchor="w", padx=20, pady=(5, 15))