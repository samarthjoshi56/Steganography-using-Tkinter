import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

class VideoFrameEmbedder:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Frame Embedder")
        self.video_path = ""
        self.image_path = ""
        self.cap = None
        self.frame_count = 0
        self.frame_width = 0
        self.frame_height = 0
        self.fps = 0
        self.embedded_video_path = ""
        self.embedded_frame_number = 0

        # Create UI elements
        self.video_label = tk.Label(self.master, text="Select video file:")
        self.video_label.pack()
        self.video_button = tk.Button(self.master, text="Open Video", command=self.open_video)
        self.video_button.pack()

        self.image_label = tk.Label(self.master, text="Select image to embed:")
        self.image_label.pack()
        self.image_button = tk.Button(self.master, text="Open Image", command=self.open_image)
        self.image_button.pack()

        self.frame_number_label = tk.Label(self.master, text="Enter frame number to embed image:")
        self.frame_number_label.pack()
        self.frame_number_entry = tk.Entry(self.master)
        self.frame_number_entry.pack()

        self.embed_button = tk.Button(self.master, text="Embed Image into Video", command=self.embed_image, state=tk.DISABLED)
        self.embed_button.pack()

        self.save_button = tk.Button(self.master, text="Save Embedded Video", command=self.save_embedded_video, state=tk.DISABLED)
        self.save_button.pack()

    def open_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))

    def open_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            self.embed_button.config(state=tk.NORMAL)

    def embed_image(self):
        try:
            frame_number = int(self.frame_number_entry.get())
            if frame_number < 0 or frame_number >= self.frame_count:
                messagebox.showerror("Error", "Invalid frame number.")
                return

            image = cv2.imread(self.image_path)
            if image is None:
                messagebox.showerror("Error", "Failed to load the image.")
                return

            # Resize image to match video frame size
            image = cv2.resize(image, (self.frame_width, self.frame_height))

            # Read video and embed image at the specified frame number
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            success, frame = self.cap.read()
            if success:
                # Blend image with video frame
                alpha = 0.5  # Opacity of the image
                blended_frame = cv2.addWeighted(frame, 1 - alpha, image, alpha, 0)

                # Save the embedded frame number for later use
                self.embedded_frame_number = frame_number

                # Display the embedded frame
                cv2.imshow("Embedded Frame", blended_frame)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                # Write the embedded video to a temporary file
                self.embedded_video_path = f"embedded_video_{frame_number}.mp4"
                out = cv2.VideoWriter(self.embedded_video_path, cv2.VideoWriter_fourcc(*"mp4v"), self.fps, (self.frame_width, self.frame_height))
                for i in range(self.frame_count):
                    if i == frame_number:
                        out.write(blended_frame)
                    else:
                        self.cap.set(cv2.CAP_PROP_POS_FRAMES, i)
                        success, frame = self.cap.read()
                        if success:
                            out.write(frame)
                out.release()

                self.save_button.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", "Failed to read video frame.")
        except ValueError:
            messagebox.showerror("Error", "Invalid frame number.")

    def save_embedded_video(self):
        if not self.embedded_video_path:
            messagebox.showerror("Error", "No embedded video found.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if save_path:
            import shutil
            shutil.move(self.embedded_video_path, save_path)
            messagebox.showinfo("Success", "Embedded video saved successfully.")
            self.embedded_video_path = ""

def main():
    root = tk.Tk()
    app = VideoFrameEmbedder(root)
    root.mainloop()

if __name__ == "__main__":
    main()
