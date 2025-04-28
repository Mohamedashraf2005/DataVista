import customtkinter as ctk
from tkinter import messagebox
import uuid

class MLModelPage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
      
    def create_ui(self):
        self.ml_frame = ctk.CTkFrame(self.parent, fg_color="#f0f4f8")
        self.ml_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Upper Frame: Model Overview and Prediction Interface
        self.upper_frame = ctk.CTkFrame(self.ml_frame, fg_color="#f0f4f8")
        self.upper_frame.pack(fill=ctk.BOTH, expand=True, padx=5, pady=(0, 10))

        # Left Column: Model Overview
        self.left_frame = ctk.CTkFrame(self.upper_frame, fg_color="#ffffff", corner_radius=12, border_width=1, border_color="#e0e0e0")
        self.left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=(0, 10))

        model_title = ctk.CTkLabel(self.left_frame, text="MODEL OVERVIEW", 
                                   font=("Arial", 18, "bold"), text_color="#1a73e8")
        model_title.pack(anchor='w', padx=15, pady=(15, 5))

        summary_label = ctk.CTkLabel(self.left_frame, text="SUMMARY: Comprehensive model architecture and parameters", 
                                     font=("Arial", 13), wraplength=500, justify="left", text_color="#333333")
        summary_label.pack(anchor='w', padx=15, pady=(5, 5))

        name_label = ctk.CTkLabel(self.left_frame, text="MODEL NAME: Gradient Boosting Classifier", 
                                  font=("Arial", 13), wraplength=500, justify="left", text_color="#333333")
        name_label.pack(anchor='w', padx=15, pady=(5, 5))

        rationale_label = ctk.CTkLabel(self.left_frame, text="SELECTION RATIONALE: High accuracy and robustness", 
                                       font=("Arial", 13), wraplength=500, justify="left", text_color="#333333")
        rationale_label.pack(anchor='w', padx=15, pady=(5, 15))

        # Right Column: Interactive Prediction Interface (Placeholder)
        self.right_frame = ctk.CTkFrame(self.upper_frame, fg_color="#e8f0fe", corner_radius=12, border_width=1, border_color="#e0e0e0")
        self.right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)

        prediction_title = ctk.CTkLabel(self.right_frame, text="Interactive Prediction Interface", 
                                        font=("Arial", 18, "bold"), text_color="#1a73e8")
        prediction_title.pack(anchor='center', pady=(15, 15))

        # Lower Frame: Tabbed Interface for Visualizations and Comparisons
        self.lower_frame = ctk.CTkFrame(self.ml_frame, fg_color="#f0f4f8")
        self.lower_frame.pack(fill=ctk.BOTH, expand=True, padx=5, pady=(10, 0))

        # TabView for Confusion Matrix, Key Features, and Comparison
        self.tab_view = ctk.CTkTabview(self.lower_frame, fg_color="#ffffff", segmented_button_selected_color="#1a73e8", 
                                       segmented_button_selected_hover_color="#1565c0", corner_radius=12)
        self.tab_view.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

        # Tab 1: Confusion Matrix
        self.confusion_tab = self.tab_view.add("Confusion Matrix")
        confusion_title = ctk.CTkLabel(self.confusion_tab, text="CONFUSION MATRIX VISUALIZATION", 
                                       font=("Arial", 16, "bold"), text_color="#1a73e8")
        confusion_title.pack(anchor='center', pady=(10, 10))
        confusion_placeholder = ctk.CTkLabel(self.confusion_tab, text="Placeholder for Confusion Matrix Plot", 
                                             font=("Arial", 12), text_color="#333333")
        confusion_placeholder.pack(anchor='center', pady=10)

        # Tab 2: Key Features
        self.features_tab = self.tab_view.add("Key Features")
        features_title = ctk.CTkLabel(self.features_tab, text="Key Features Extracted from Training Data", 
                                      font=("Arial", 16, "bold"), text_color="#1a73e8")
        features_title.pack(anchor='center', pady=(10, 10))
        features_placeholder = ctk.CTkLabel(self.features_tab, text="Placeholder for Feature Importance Chart", 
                                            font=("Arial", 12), text_color="#333333")
        features_placeholder.pack(anchor='center', pady=10)

        # Tab 3: Train-Test Split vs K-Folds Comparison
        self.comparison_tab = self.tab_view.add("Model Evaluation Comparison")
        comparison_title = ctk.CTkLabel(self.comparison_tab, text="Train-Test Split vs K-Folds Comparison", 
                                        font=("Arial", 16, "bold"), text_color="#1a73e8")
        comparison_title.pack(anchor='center', pady=(10, 10))

        # Comparison Frame with Two Columns
        comparison_frame = ctk.CTkFrame(self.comparison_tab, fg_color="#e8f0fe", corner_radius=10)
        comparison_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Train-Test Split Section
        train_test_frame = ctk.CTkFrame(comparison_frame, fg_color="#ffffff", corner_radius=8)
        train_test_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=(0, 5))

        train_test_title = ctk.CTkLabel(train_test_frame, text="Train-Test Split", 
                                        font=("Arial", 14, "bold"), text_color="#1a73e8")
        train_test_title.pack(anchor='w', padx=10, pady=(10, 5))

        train_test_desc = ctk.CTkLabel(train_test_frame, 
                                       text="DESCRIPTION:",
                                       font=("Arial", 12), wraplength=300, justify="left", text_color="#333333")
        train_test_desc.pack(anchor='w', padx=10, pady=5)

        train_test_pros = ctk.CTkLabel(train_test_frame, 
                                       text="PROS:",
                                       font=("Arial", 12), wraplength=300, justify="left", text_color="#333333")
        train_test_pros.pack(anchor='w', padx=10, pady=5)

        train_test_cons = ctk.CTkLabel(train_test_frame, 
                                       text="CONS:",
                                       font=("Arial", 12), wraplength=300, justify="left", text_color="#333333")
        train_test_cons.pack(anchor='w', padx=10, pady=5)

        # K-Folds Section
        k_folds_frame = ctk.CTkFrame(comparison_frame, fg_color="#ffffff", corner_radius=8)
        k_folds_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=(5, 0))

        k_folds_title = ctk.CTkLabel(k_folds_frame, text="K-Folds Cross-Validation", 
                                     font=("Arial", 14, "bold"), text_color="#1a73e8")
        k_folds_title.pack(anchor='w', padx=10, pady=(10, 5))

        k_folds_desc = ctk.CTkLabel(k_folds_frame, 
                                    text="DESCRIPTION:",
                                    font=("Arial", 12), wraplength=300, justify="left", text_color="#333333")
        k_folds_desc.pack(anchor='w', padx=10, pady=5)

        k_folds_pros = ctk.CTkLabel(k_folds_frame, 
                                    text="PROS:",
                                    font=("Arial", 12), wraplength=300, justify="left", text_color="#333333")
        k_folds_pros.pack(anchor='w', padx=10, pady=5)

        k_folds_cons = ctk.CTkLabel(k_folds_frame, 
                                    text="CONS:",
                                    font=("Arial", 12), wraplength=300, justify="left", text_color="#333333")
        k_folds_cons.pack(anchor='w', padx=10, pady=5)