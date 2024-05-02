import tkinter as tk
from tkinter import Frame, Button, Text, filedialog, messagebox
import wave

class Stegno:

    def encode_audio(self, audio_file, text):
        # Read the audio file
        with wave.open(audio_file, 'rb') as audio:
            # Get audio parameters
            params = audio.getparams()
            frames = audio.readframes(audio.getnframes())

        # Convert text to bytes
        encoded_text = text.encode('utf-8')
        encoded_text += b'\0' * (len(frames) - len(encoded_text))  # Pad with zeros to match frame length

        # Merge audio frames with encoded text
        encoded_frames = bytearray()
        for i, frame in enumerate(frames):
            if i < len(encoded_text):
                byte = encoded_text[i]
            else:
                byte = frame
            encoded_frames.append(byte)

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

    def decode_audio(self, audio_file):
        # Read the audio file
        with wave.open(audio_file, 'rb') as audio:
            frames = audio.readframes(audio.getnframes())

        # Decode text from audio frames
        decoded_text = ""
        for frame in frames:
            if frame != 0:
                decoded_text += chr(frame)

        messagebox.showinfo("Decoded Message", "Decoded Message:\n" + decoded_text)

    def frame2_encode(self, f2):
        ep = tk.Frame(root)
        myfile = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            encode_button = Button(ep, text="Encode", command=lambda: [self.encode_audio(myfile, text_area.get("1.0", "end-1c")), self.home(ep)])
            encode_button.grid(pady=15)
            ep.grid(row=1)
            f2.destroy()

    def frame2_decode(self, f2):
        ep = tk.Frame(root)
        myfile = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            decode_button = Button(ep, text="Decode", command=lambda: [self.decode_audio(myfile), self.home(ep)])
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
        l1 = tk.Label(f2, text='Select the Audio in which \nyou want to hide text :')
        l1.config(font=('courier', 18))
        l1.grid()

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_encode(f2))
        bws_button.config(font=('courier', 18))
        bws_button.grid()
        back_button = Button(f2, text='Cancel', command=lambda: self.home(f2))
        back_button.config(font=('courier', 18))
        back_button.grid(pady=15)
        back_button.grid()
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
        back_button.grid()
        f2.grid()


# Usage:
root = tk.Tk()
o = Stegno()
o.main(root)
root.mainloop()
