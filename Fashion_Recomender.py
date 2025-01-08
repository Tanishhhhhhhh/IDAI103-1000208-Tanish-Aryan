import tkinter as tk
from tkinter import messagebox
import google.generativeai as genai

# Configure Gemini with your API key
genai.configure(api_key="AIzaSyCT3GU_8SBkIzYyySdly2vXGFCMHGJ7_ss")  # Replace with your actual Gemini API key

# Function to handle the submit button click
def generate_recommendation():
    user_prompt = prompt_entry.get("1.0", tk.END).strip()
    
    if not user_prompt:
        messagebox.showerror("Error", "Please provide a prompt.")
        return

    try:
        # Generate recommendation using Gemini API
        recommendation_text = generate_gemini_recommendation(user_prompt)
        display_text_recommendation(recommendation_text)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to generate recommendation using Gemini API
def generate_gemini_recommendation(prompt):
    # Use the Gemini model to generate content
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    # Extract and return the text from the response
    return response.text

# Function to display the recommendation text
def display_text_recommendation(text):
    recommendation_text.delete("1.0", tk.END)
    recommendation_text.insert(tk.END, text)

# Create the main application window
root = tk.Tk()
root.title("Gemini Recommender Chat")
root.state('zoomed')  # Maximize the window

# Title Label
title_label = tk.Label(root, text="Gemini Recommender Chat", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Prompt Input Box
prompt_label = tk.Label(root, text="Enter Your Prompt:", font=("Arial", 12))
prompt_label.pack(anchor="w", padx=20)
prompt_entry = tk.Text(root, font=("Arial", 12), height=5, wrap="word")
prompt_entry.pack(fill="x", padx=20, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Generate Recommendation", command=generate_recommendation, font=("Arial", 12), bg="blue", fg="white")
submit_button.pack(pady=10)

# Recommendation Output Section
recommendation_label = tk.Label(root, text="Recommendations:", font=("Arial", 12))
recommendation_label.pack(anchor="w", padx=20)

# Text area to display the recommendation text
recommendation_text = tk.Text(root, font=("Arial", 12), height=10, wrap="word")
recommendation_text.pack(fill="x", padx=20, pady=5)

# Run the application
root.mainloop()


