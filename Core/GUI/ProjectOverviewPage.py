import customtkinter as ctk

class ProjectOverviewPage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app

    def create_ui(self):
        self.overview_frame = ctk.CTkFrame(self.parent, fg_color="#f0f4f8")
        self.overview_frame.pack(fill=ctk.BOTH, expand=True)

       

        # Project Overview Section
        self.project_overview_frame = ctk.CTkFrame(self.overview_frame, fg_color="#ffffff", corner_radius=10)
        self.project_overview_frame.pack(fill='x', padx=5, pady=5)

        project_title = ctk.CTkLabel(self.project_overview_frame, text="PROJECT OVERVIEW", 
                                     font=("Arial", 18, "bold"), text_color="#1a73e8")
        project_title.pack(anchor='w', padx=10, pady=(10, 0))

        project_desc = ctk.CTkLabel(self.project_overview_frame, 
                                    text="This project encompasses a comprehensive analysis and implementation of a machine learning pipeline. It includes detailed descriptions of the project objectives, course affiliation, timeline, and the datasets utilized along with their sources. The project is currently in the ML phase, focusing on model development and evaluation.",
                                    font=("Arial", 12), wraplength=1100, justify="left")
        project_desc.pack(anchor='w', padx=10, pady=(5, 10))

        # Two-column layout for Contributors, Key Learnings, and Contact & Support
        self.columns_frame = ctk.CTkFrame(self.overview_frame, fg_color="#f0f4f8")
        self.columns_frame.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

        # Left Column: Project Contributors
        self.left_frame = ctk.CTkFrame(self.columns_frame, fg_color="#ffffff", corner_radius=10)
        self.left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=(0, 5))

        contributors_title = ctk.CTkLabel(self.left_frame, text="Project Contributors", 
                                          font=("Arial", 16, "bold"), text_color="#1a73e8")
        contributors_title.pack(anchor='w', padx=10, pady=(10, 0))

        contributors_desc = ctk.CTkLabel(self.left_frame, 
                                         text="Our dedicated team of data scientists, analysts, and developers collaborated closely to ensure the success of this project. Their expertise spans data preprocessing, exploratory data analysis, and advanced machine learning techniques.",
                                         font=("Arial", 12), wraplength=500, justify="left")
        contributors_desc.pack(anchor='w', padx=10, pady=(5, 10))

        # Right Column: Key Learnings and Contact & Support
        self.right_frame = ctk.CTkFrame(self.columns_frame, fg_color="#ffffff", corner_radius=10)
        self.right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)

        # Key Learnings
        learnings_title = ctk.CTkLabel(self.right_frame, text="Key Learnings", 
                                       font=("Arial", 16, "bold"), text_color="#1a73e8")
        learnings_title.pack(anchor='w', padx=10, pady=(10, 0))

        learnings_desc = ctk.CTkLabel(self.right_frame, 
                                      text="Through this project, we have gained valuable insights into data handling, feature engineering, and model optimization. The iterative process has enhanced our understanding of predictive analytics and real-world application challenges.",
                                      font=("Arial", 12), wraplength=500, justify="left")
        learnings_desc.pack(anchor='w', padx=10, pady=(5, 10))

        # Contact & Support
        contact_title = ctk.CTkLabel(self.right_frame, text="Contact & Support", 
                                     font=("Arial", 16, "bold"), text_color="#1a73e8")
        contact_title.pack(anchor='w', padx=10, pady=(20, 0))

        contact_desc = ctk.CTkLabel(self.right_frame, 
                                    text="For further information or collaboration opportunities, please reach out to us via email at mohamedachrvf@gmail.com mohamedachrvf@gmail.com mohamedachrvf@gmail.com mohamedachrvf@gmail.com .",
                                    font=("Arial", 12), wraplength=500, justify="left")
        contact_desc.pack(anchor='w', padx=10, pady=(5, 10))