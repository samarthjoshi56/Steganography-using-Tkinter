import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

class SteganographyApp:
    def __init__(self, master):
        self.master = master
        master.title("Multimedia Steganography GUI")
        master.configure(bg='black')  # Set background color to black

        # ASCII art
        self.ascii_label = tk.Label(master, text='''
 
   _____ _______ ______ _____          _   _  ____   _____ _____            _____  _    ___     __ 
  / ____|__   __|  ____/ ____|   /\   | \ | |/ __ \ / ____|  __ \     /\   |  __ \| |  | \ \   / / 
 | (___    | |  | |__ | |  __   /  \  |  \| | |  | | |  __| |__) |   /  \  | |__) | |__| |\ \_/ /  
  \___ \   | |  |  __|| | |_ | / /\ \ | . ` | |  | | | |_ |  _  /   / /\ \ |  ___/|  __  | \   /   
  ____) |  | |  | |___| |__| |/ ____ \| |\  | |__| | |__| | | \ \  / ____ \| |    | |  | |  | |    
 |_____/   |_|  |______\_____/_/    \_\_| \_|\____/ \_____|_|  \_\/_/    \_\_|    |_|  |_|  |_|    
                                                                                                   
                                                                                                   

''', bg='black', fg='white', font=('Courier', 16))
        self.ascii_label.pack()

        # Menus
        self.menu_frame = tk.Frame(master, bg='black')
        self.menu_frame.pack()

        # Steganography Operations button
        self.operations_button = tk.Button(self.menu_frame, text="Steganography Operations", command=self.open_operations,
                                            bg='#4CAF50', fg='black', font=('Arial', 12))
        self.operations_button.pack(side=tk.LEFT, padx=5)

        # Features button
        self.features_button = tk.Button(self.menu_frame, text="Features", command=self.show_features,
                                         bg='#2196F3', fg='black', font=('Arial', 12))
        self.features_button.pack(side=tk.LEFT, padx=5)

        # About button
        self.about_button = tk.Button(self.menu_frame, text="About", command=self.show_about,
                                       bg='#FFC107', fg='black', font=('Arial', 12))
        self.about_button.pack(side=tk.LEFT, padx=5)

        # GitHub button
        self.github_button = tk.Button(self.menu_frame, text="GitHub", command=self.open_github,
                                       bg='#795548', fg='black', font=('Arial', 12))
        self.github_button.pack(side=tk.LEFT, padx=5)

        # Certification info
        self.certification_label = tk.Label(master, text="MAJOR PROJECT 2024", bg='black', fg='white',
                                            font=('Arial', 10))
        self.certification_label.pack(side=tk.BOTTOM)

    def open_operations(self):
        self.operations_window = tk.Toplevel(self.master)
        self.operations_window.title("Steganography Operations")
        self.operations_window.configure(bg='black')

        # Operation buttons
        self.operation_buttons = []
        operations = ["Encryption of Text", "Decryption of Text", "Image Steganography", "Audio Steganography"]
        for operation in operations:
            button = tk.Button(self.operations_window, text=operation, command=lambda op=operation: self.execute_code(op),
                               bg='#FF5722', fg='black', font=('Arial', 12))
            button.pack()

        # ASCII art
        self.ascii_label = tk.Label(self.operations_window, text='''

   ____  _____  ______ _____         _______ _____ ____  _   _  _____ 
  / __ \|  __ \|  ____|  __ \     /\|__   __|_   _/ __ \| \ | |/ ____|
 | |  | | |__) | |__  | |__) |   /  \  | |    | || |  | |  \| | (___  
 | |  | |  ___/|  __| |  _  /   / /\ \ | |    | || |  | | . ` |\___ \ 
 | |__| | |    | |____| | \ \  / ____ \| |   _| || |__| | |\  |____) |
  \____/|_|    |______|_|  \_\/_/    \_\_|  |_____\____/|_| \_|_____/ 
                                                                      
                                                                      

''', bg='black', fg='white', font=('Courier', 14))
        self.ascii_label.pack()

    def show_about(self):
        self.about_window = tk.Toplevel(self.master)
        self.about_window.title("About")
        self.about_window.configure(bg='black')
        
        about_text = """Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video.
It is often used to hide the existence of the communicated data. 
This program offers various steganography techniques like Encryption of Text, Decryption of Text, Image Steganography, and Audio Steganography."""
        
        self.about_label = tk.Label(self.about_window, text=about_text, wraplength=400, justify="left",
                                     bg='black', fg='white', font=('Arial', 12))
        self.about_label.pack()

        # Contact info
        contact_label = tk.Label(self.about_window, text="Contact:", bg='black', fg='white', font=('Arial', 12))
        contact_label.pack()
        contacts = ["Sanjana Oza", "Shivaprasad Patil", "Swati Patil"]
        for contact in contacts:
            contact_label = tk.Label(self.about_window, text=contact, bg='black', fg='white', font=('Arial', 12))
            contact_label.pack()

        # ASCII art
        self.ascii_label = tk.Label(self.about_window, text='''

           ____   ____  _    _ _______ 
     /\   |  _ \ / __ \| |  | |__   __|
    /  \  | |_) | |  | | |  | |  | |   
   / /\ \ |  _ <| |  | | |  | |  | |   
  / ____ \| |_) | |__| | |__| |  | |   
 /_/    \_\____/ \____/ \____/   |_|   
                                       
                                       

''', bg='black', fg='white', font=('Courier', 14))
        self.ascii_label.pack()

    def show_features(self):
        self.features_window = tk.Toplevel(self.master)
        self.features_window.title("Features")
        self.features_window.configure(bg='black')

        features_text = """1. Encryption of Text: Encrypt text messages using a chosen algorithm.
2. Decryption of Text: Decrypt text messages encrypted using this program.
3. Image Steganography: Hide text or another image within an image file.
4. Audio Steganography: Hide text within an audio file."""
        
        self.features_label = tk.Label(self.features_window, text=features_text, wraplength=400, justify="left",
                                       bg='black', fg='white', font=('Arial', 12))
        self.features_label.pack()

        # ASCII art
        self.ascii_label = tk.Label(self.features_window, text='''

   __           _                       
  / _|         | |                      
 | |_ ___  __ _| |_ _   _ _ __ ___  ___ 
 |  _/ _ \/ _` | __| | | | '__/ _ \/ __|
 | ||  __/ (_| | |_| |_| | | |  __/\__ \
 |_| \___|\__,_|\__|\__,_|_|  \___||___/
                                        
                                        

''', bg='black', fg='white', font=('Courier', 14))
        self.ascii_label.pack()

    def open_github(self):
        webbrowser.open_new_tab("https://github.com/your_repository")

    def execute_code(self, operation):
        # Check if user is logged in
        if not self.is_logged_in():
            messagebox.showwarning("Login Required", "Please login to perform this operation.")
            return

        # Execute corresponding operation
        if operation == "Encryption of Text":
            os.system("python Encryption.py")
        elif operation == "Decryption of Text":
            os.system("python Decryption.py")
        elif operation == "Image Steganography":
            os.system("python img.py")
        elif operation == "Audio Steganography":
            os.system("python audio.py")

    def is_logged_in(self):
        # Check if user is logged in
        # Implement your logic here, e.g., check if username and password are in the database
        return True  # For demonstration purposes, always return True

def main():
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
