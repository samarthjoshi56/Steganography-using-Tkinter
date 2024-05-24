import tkinter as tk
from tkinter import Frame, Button, Text, Entry, filedialog, messagebox
import wave

class Stegno:

    def encode_audio(self, audio_file, key, text):
        # Read the audio file
        with wave.open(audio_file, 'rb') as audio:
            # Get audio parameters
            params = audio.getparams()
            frames = audio.readframes(audio.getnframes())

        # Combine key and text to encode
        combined_text = key + ':' + text
        encoded_text = combined_text.encode('utf-8') + b'\0'  # Null-terminate the encoded text

        # Check if the text can be hidden in the audio file
        if len(encoded_text) > len(frames):
            messagebox.showerror("Error", "Text is too long to hide in this audio file.")
            return

        # Merge audio frames with encoded text
        encoded_frames = bytearray(frames)
        for i, byte in enumerate(encoded_text):
            encoded_frames[i] = byte

        # Prompt user to choose save location
        save_location = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if not save_location:
            messagebox.showinfo("Info", "Encoding canceled.")
            return

        # Write the modified audio to the chosen file
        with wave.open(save_location, 'wb') as audio_out:
            audio_out.setparams(params)
            audio_out.writeframes(encoded_frames)

        messagebox.showinfo("Success", f"Audio encoded successfully. Encoded audio saved as {save_location}.")

    def decode_audio(self, audio_file, input_key):
        # Read the audio file
        with wave.open(audio_file, 'rb') as audio:
            frames = audio.readframes(audio.getnframes())

        # Decode text from audio frames
        decoded_bytes = bytearray()
        for frame in frames:
            if frame != 0:
                decoded_bytes.append(frame)
            else:
                break

        combined_text = decoded_bytes.decode('utf-8')
        # Separate key and message
        try:
            key, message = combined_text.split(':', 1)
        except ValueError:
            messagebox.showerror("Error", "Failed to decode. No valid key found.")
            return

        # Check the input key
        if key != input_key:
            messagebox.showerror("Error", "Incorrect key. Access denied.")
            return

        messagebox.showinfo("Decoded Message", "Decoded Message:\n" + message)

    def frame2_encode(self, f2):
        ep = tk.Frame(root)
        myfile = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            key_label = tk.Label(ep, text="Enter Key:")
            key_label.grid()
            key_entry = Entry(ep, show="*")
            key_entry.grid()
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            encode_button = Button(ep, text="Encode", command=lambda: [self.encode_audio(myfile, key_entry.get(), text_area.get("1.0", "end-1c")), self.home(ep)])
            encode_button.grid(pady=15)
            ep.grid(row=1)
            f2.destroy()

    def frame2_decode(self, f2):
        ep = tk.Frame(root)
        myfile = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            key_label = tk.Label(ep, text="Enter Key:")
            key_label.grid()
            key_entry = Entry(ep, show="*")
            key_entry.grid()
            decode_button = Button(ep, text="Decode", command=lambda: [self.decode_audio(myfile, key_entry.get()), self.home(ep)])
            decode_button.grid(pady=15)
            ep.grid(row=1)
            f2.destroy()

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def main(self, root):
        root.title('Audio Steganography')
        root.geometry('500x600')
        root.state('zoomed')  # Maximize window
        f = Frame(root)

        title = tk.Label(f, text='Audio Steganography')
        title.config(font=('courier', 33))
        title.grid(pady=10)

        b_encode = Button(f, text="Encode", command=lambda: self.frame1_encode(f), padx=14)
        b_encode.config(font=('courier', 14))
        b_decode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_decode(f))
        b_decode.config(font=('courier', 14))
        b_decode.grid(pady=12)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        b_encode.grid(row=2)
        b_decode.grid(row=3)

    def frame1_encode(self, f):
        f.destroy()
        f2 = tk.Frame(root)
        label_art = tk.Label(f2, text='\'\(°Ω°)/\'')
        label_art.config(font=('courier', 70))
        label_art.grid(row=1, pady=50)
        l1 = tk.Label(f2, text='Select the Audio in which \nyou want to hide text:')
        l1.config(font=('courier', 18))
        l1.grid()

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_encode(f2))
        bws_button.config(font=('courier', 18))
        bws_button.grid()
        back_button = Button(f2, text='Cancel', command=lambda: self.home(f2))
        back_button.config(font=('courier', 18))
        back_button.grid(pady=15)
        f2.grid()

    def frame1_decode(self, f):
        f.destroy()
        f2 = tk.Frame(root)
        label_art = tk.Label(f2, text='٩(^‿^)۶')
        label_art.config(font=('courier', 90))
        label_art.grid(row=1, pady=50)
        l1 = tk.Label(f2, text='Select Audio with Hidden text:')
        l1.config(font=('courier', 18))
        l1.grid()
        bws_button = Button(f2, text='Select', command=lambda: self.frame2_decode(f2))
        bws_button.config(font=('courier', 18))
        bws_button.grid()
        back_button = Button(f2, text='Cancel', command=lambda: self.home(f2))
        back_button.config(font=('courier', 18))
        back_button.grid(pady=15)
        f2.grid()

# Usage:
root = tk.Tk()
o = Stegno()
o.main(root)
root.mainloop()
