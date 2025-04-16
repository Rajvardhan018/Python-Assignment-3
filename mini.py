import PyPDF2
import pyttsx3
import pandas as pd
import os  # to check file existence

# Take user inputs
file_path = input("Enter the path to the PDF file: ").strip()

# Fix Windows path issue (if user enters without raw string)
file_path = file_path.replace("\\", "/")

# Check if file exists
if not os.path.exists(file_path):
    print("File not found. Please check the path and try again.")
    exit()

rate = int(input("Enter the speaking rate (e.g., 150 for slow, 200 normal, 300 fast): "))

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', rate)

# Optional: Choose voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female

# Prepare a list to store data for pandas
page_data = []

# Read the PDF and extract text
with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    full_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            word_count = len(text.split())
            page_data.append({"Page": i + 1, "Words": word_count})
            full_text += text

# Display report using pandas
df = pd.DataFrame(page_data)
print("\n PDF Summary Report:")
print(df)

# Read aloud
engine.say(full_text)
engine.runAndWait()
