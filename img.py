from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk, Image
from io import BytesIO
import os

class Stegno:

    art = '''¯\(ツ)/¯'''
    art2 = '''
@(\/)
(\/)-{}-)@
@(={}=)/\)(\/)
(\/(/\)@| (-{}-)
(={}=)@(\/)@(/\)@
(/\)\(={}=)/(\/)
@(\/)\(/\)/(={}=)
(-{}-)""""@/(/\)
|:   |
/::'   \\
/:::     \\
|::'       |
|::        |
\::.       /
':.'
""""""'''

    output_image_size = 0

    def main(self, root):
        root.title('ImageSteganography')
        root.geometry('500x600')
        root.resizable(width=False, height=False)
        f = Frame(root)

        title = Label(f, text='Image Steganography')
        title.config(font=('courier', 33))
        title.grid(pady=10)

        b_encode = Button(f, text="Encode", command=lambda: self.frame1_encode(f), padx=14)
        b_encode.config(font=('courier', 14))
        b_decode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_decode(f))
        b_decode.config(font=('courier', 14))
        b_decode.grid(pady=12)

        ascii_art = Label(f, text=self.art)
        ascii_art.config(font=('courier', 60))

        ascii_art2 = Label(f, text=self.art2)
        ascii_art2.config(font=('courier', 12, 'bold'))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        b_encode.grid(row=2)
        b_decode.grid(row=3)
        ascii_art.grid(row=4, pady=10)
        ascii_art2.grid(row=5, pady=5)

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def frame1_decode(self, f):
        f.destroy()
        d_f2 = Frame(root)
        label_art = Label(d_f2, text='٩(^‿^)۶')
        label_art.config(font=('courier', 90))
        label_art.grid(row=1, pady=50)
        l1 = Label(d_f2, text='Select Image with Hidden text:')
        l1.config(font=('courier', 18))
        l1.grid()
        bws_button = Button(d_f2, text='Select', command=lambda: self.frame2_decode(d_f2))
        bws_button.config(font=('courier', 18))
        bws_button.grid()
        back_button = Button(d_f2, text='Cancel', command=lambda: Stegno.home(self, d_f2))
        back_button.config(font=('courier', 18))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()

    def frame2_decode(self, d_f2):
        d_f3 = Frame(root)
        myfile = filedialog.askopenfilename(filetypes=[('png', '.png'), ('jpeg', '.jpeg'), ('jpg', '.jpg'), ('All Files', '.*')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4 = Label(d_f3, text='Selected Image:')
            l4.config(font=('courier', 18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()

            key_label = Label(d_f3, text='Enter the secret key:')
            key_label.config(font=('courier', 18))
            key_label.grid(pady=10)
            key_entry = Entry(d_f3, show="*")
            key_entry.config(font=('courier', 18))
            key_entry.grid()

            decode_button = Button(d_f3, text='Decode', command=lambda: self.verify_key_and_decode(myimg, key_entry.get(), d_f3))
            decode_button.config(font=('courier', 11))
            decode_button.grid(pady=15)
            back_button = Button(d_f3, text='Cancel', command=lambda: self.page3(d_f3))
            back_button.config(font=('courier', 11))
            back_button.grid(pady=15)
            show_info = Button(d_f3, text='More Info', command=self.info)
            show_info.config(font=('courier', 11))
            show_info.grid()
            d_f3.grid(row=1)
            d_f2.destroy()

    def verify_key_and_decode(self, myimg, key, frame):
        hidden_data = self.decode(myimg)
        if hidden_data.startswith(key):
            data = hidden_data[len(key):]
            l2 = Label(frame, text='Hidden data is:')
            l2.config(font=('courier', 18))
            l2.grid(pady=10)
            text_area = Text(frame, width=50, height=10)
            text_area.insert(INSERT, data)
            text_area.configure(state='disabled')
            text_area.grid()
        else:
            messagebox.showerror("Error", "Incorrect key! The program will close.")
            root.destroy()

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while True:
            pixels = [value for value in next(imgdata)[:3] +
                      next(imgdata)[:3] +
                      next(imgdata)[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame1_encode(self, f):
        f.destroy()
        f2 = Frame(root)
        label_art = Label(f2, text='\'\(°Ω°)/\'')
        label_art.config(font=('courier', 70))
        label_art.grid(row=1, pady=50)
        l1 = Label(f2, text='Select the Image in which \nyou want to hide text:')
        l1.config(font=('courier', 18))
        l1.grid()

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_encode(f2))
        bws_button.config(font=('courier', 18))
        bws_button.grid()
        back_button = Button(f2, text='Cancel', command=lambda: Stegno.home(self, f2))
        back_button.config(font=('courier', 18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()

    def frame2_encode(self, f2):
        ep = Frame(root)
        myfile = filedialog.askopenfilename(filetypes=[('png', '.png'), ('jpeg', '.jpeg'), ('jpg', '.jpg'), ('All Files', '.*')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l3 = Label(ep, text='Selected Image')
            l3.config(font=('courier', 18))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()

            key_label = Label(ep, text='Enter the secret key:')
            key_label.config(font=('courier', 18))
            key_label.grid(pady=10)
            key_entry = Entry(ep)
            key_entry.config(font=('courier', 18))
            key_entry.grid()

            l2 = Label(ep, text='Enter the message:')
            l2.config(font=('courier', 18))
            l2.grid(pady=15)
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            encode_button = Button(ep, text='Cancel', command=lambda: Stegno.home(self, ep))
            encode_button.config(font=('courier', 11))
            back_button = Button(ep, text='Encode', command=lambda: self.enc_fun(text_area, myimg, key_entry.get(), ep))
            back_button.config(font=('courier', 11))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
            f2.destroy()

    def info(self):
        try:
            str = 'Original image:-\nSize of original image: {:.2f} MB\nWidth: {}\nHeight: {}\n\n' \
                  'Decoded image:-\nSize of decoded image: {:.2f} MB\nWidth: {}\nHeight: {}'.format(
                      self.output_image_size.st_size / 1000000, self.o_image_w, self.o_image_h,
                      self.d_image_size /1000000, self.d_image_w, self.d_image_h)
            messagebox.showinfo('Info', str)
        except:
            messagebox.showinfo('Info', 'Unable to get the information')

    def genData(self, data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self, pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        
        for i in range(lendata):
            pix = [value for value in next(imdata)[:3] +
                   next(imdata)[:3] +
                   next(imdata)[:3]]
            
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                    pix[j] -= 1
                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self, text_area, myimg, key, ep):
        if len(key) < 1:
            messagebox.showinfo("Alert", "Key must be at least one character")
            return
        data = key + text_area.get("1.0", "end-1c")
        if len(data) == len(key):
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(filedialog.asksaveasfilename(initialfile=temp, filetypes=[('png', '*.png')], defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h = newimg.size
            messagebox.showinfo("Success", "Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")
            Stegno.home(self, ep)

    def page3(self, frame):
        frame.destroy()
        self.main(root)

root = Tk()

o = Stegno()
o.main(root)

root.mainloop()
