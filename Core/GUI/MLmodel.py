import customtkinter as ctk
from tkinter import messagebox

class MLModelPage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
      
    def create_ui(self):
        self.ml_frame = ctk.CTkFrame(self.parent, fg_color="#f0f4f8")
        self.ml_frame.pack(fill=ctk.BOTH, expand=True)

        
        self.upper_frame = ctk.CTkFrame(self.ml_frame, fg_color="#f0f4f8")
        self.upper_frame.pack(fill=ctk.BOTH, expand=True, padx=5, pady=(0, 5))

        # Left Column: Model Overview
        self.left_frame = ctk.CTkFrame(self.upper_frame, fg_color="#ffffff", corner_radius=10)
        self.left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=(0, 5))

        model_title = ctk.CTkLabel(self.left_frame, text="MODEL OVERVIEW", 
                                   font=("Arial", 16, "bold"), text_color="#1a73e8")
        model_title.pack(anchor='w', padx=10, pady=(10, 0))

        summary_label = ctk.CTkLabel(self.left_frame, text="SUMMARY: Comprehensive model architecture and parameters", 
                                     font=("Arial", 12), wraplength=500, justify="left")
        summary_label.pack(anchor='w', padx=10, pady=(5, 0))

        name_label = ctk.CTkLabel(self.left_frame, text="MODEL NAME: Gradient Boosting Classifier", 
                                  font=("Arial", 12), wraplength=500, justify="left")
        name_label.pack(anchor='w', padx=10, pady=(5, 0))

        rationale_label = ctk.CTkLabel(self.left_frame, text="SELECTION RATIONALE: High accuracy", 
                                       font=("Arial", 12), wraplength=500, justify="left")
        rationale_label.pack(anchor='w', padx=10, pady=(5, 10))

        # Right Column: Interactive Prediction Interface (Placeholder)
        self.right_frame = ctk.CTkFrame(self.upper_frame, fg_color="#e8f0fe", corner_radius=10)
        self.right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)

        prediction_title = ctk.CTkLabel(self.right_frame, text="Interactive Prediction Interface", 
                                        font=("Arial", 16, "bold"), text_color="#1a73e8")
        prediction_title.pack(anchor='center', pady=(10, 10))

        # Two-column layout for Confusion Matrix and Key Features
        self.lower_frame = ctk.CTkFrame(self.ml_frame, fg_color="#f0f4f8")
        self.lower_frame.pack(fill=ctk.BOTH, expand=True, padx=5, pady=(5, 0))

        # Left Column: Confusion Matrix Visualization (Placeholder)
        self.confusion_frame = ctk.CTkFrame(self.lower_frame, fg_color="#e8f0fe", corner_radius=10)
        self.confusion_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=(0, 5))

        confusion_title = ctk.CTkLabel(self.confusion_frame, text="CONFUSION MATRIX VISUALIZATION", 
                                       font=("Arial", 16, "bold"), text_color="#1a73e8")
        confusion_title.pack(anchor='center', pady=(10, 10))

        # Right Column: Key Features Extracted
        self.features_frame = ctk.CTkFrame(self.lower_frame, fg_color="#e8f0fe", corner_radius=10)
        self.features_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)

        features_title = ctk.CTkLabel(self.features_frame, text="Key Features Extracted from Training Data", 
                                      font=("Arial", 16, "bold"), text_color="#1a73e8")
        features_title.pack(anchor='center', pady=(10, 10))
       