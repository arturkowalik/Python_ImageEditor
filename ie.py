from PIL import Image, ImageFilter
import tkinter
from tkinter import ttk, filedialog 
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image


##########################
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
##########################
class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Image ediotor by Artur Kowalik.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1, minsize=500)
        self.grid_rowconfigure(1, weight=0, minsize=200)


        input_image = Image.open("image.JPG")
        self.photoname = "image.JPG"
        
        
        def fileopen():
            self.filename= filedialog.askopenfilename(initialdir="/", 
                                                 title="Select a image",
                                                 filetypes = (("images files",
                                                               "*.jpg"),
                                                              ("all files",
                                                               "*.*")))
            if  self.filename == "":
                self.filename = "image.JPG" 
            self.photoname = self.filename
            self.img = (Image.open(self.filename))
            #resize image using resize method
            self.resized = self.img.resize((975,500), Image.ANTIALIAS)
            self.resized=ImageTk.PhotoImage(self.resized)
            self.label1.configure(image=self.resized)
            
            
        def fileprint():
            print(self.photoname)
            
        
        def blur():
            #open img
            self.input_image = Image.open(self.photoname)
            #blur it
            filter_str = 20
            self.before = self.input_image
            self.after = self.before.filter(ImageFilter.BoxBlur(filter_str))
            self.after.save("blurred_img.PNG")
            #resize it
            self.img_blured = (Image.open("blurred_img.PNG"))
            self.resized_blur = self.img_blured.resize((975,500), Image.ANTIALIAS)
            self.resized_blur.save("resized_blurred_img.PNG")

            #load image tkinter 
            self.resizedblurredimg = ImageTk.PhotoImage(Image.open("resized_blurred_img.PNG"))
            #load img to label
            self.label1.configure(image=self.resizedblurredimg)
            
            
            
            

        def outline():
            self.input_image = Image.open(self.photoname)
            self.input_image = self.input_image.convert('RGB')
            self.edged_image = self.input_image.filter(ImageFilter.FIND_EDGES)
            self.edged_image.save("edged_img.PNG")
            self.resized_edged_image = self.edged_image.resize((975,500), Image.ADAPTIVE)
            self.resized_edged_image.save("resized_edged_img.PNG")
            self.resized.edgy_image = ImageTk.PhotoImage(Image.open("resized_edged_img.PNG"))
            self.label1.configure(image=self.resized.edgy_image)
            
            


        def default_img():
            
            
            self.img = (Image.open(self.photoname))
            #resize image using resize method
            self.resized = self.img.resize((975,500), Image.ANTIALIAS)
            self.resized=ImageTk.PhotoImage(self.resized)
            self.label1.configure(image=self.resized)
            


        #configure upper frame
        self.frame_up = customtkinter.CTkFrame(master=self, 
                                               corner_radius=0.5,
                                               )
        self.frame_up.grid(row=0, column=0, sticky="nswe",)
        
        #configure down frame
        self.frame_down = customtkinter.CTkFrame(master=self,
                                                 corner_radius=0,
                                                 fg_color="black",
                                                 )
        self.frame_down.grid(row=1, column=0, sticky="nswe")

        # ============ configuring upper label and load test image  ============        
        #load image to script
        self.img = (Image.open("image.jpg"))
        #resize image using resize method
        self.resized = self.img.resize((975,500), Image.ANTIALIAS)
        self.resized=ImageTk.PhotoImage(self.resized)
        #load image to label and place it to grid
        self.label1 = customtkinter.CTkLabel(master=self.frame_up,
                               image=self.resized)
        self.label1.grid(row=0, column=0)


        # ============ configuring lower label and buttons  ============        
        
        button_0 = customtkinter.CTkButton(master=self.frame_down,
                                           text="open file", 
                                           padx=5, pady=5, corner_radius=0,
                                           command=fileopen
                                           )
        button_0.grid(row=0, column=1)
        
        button_4 = customtkinter.CTkButton(master=self.frame_down,
                                           text="print file name", 
                                           padx=5, pady=0, corner_radius=0,
                                           command=fileprint
                                           )
        button_4.grid(row=0, column=2)
        
        button_1 = customtkinter.CTkButton(master=self.frame_down,
                                              text="Blur", padx=5, pady=5,
                                              corner_radius=0,
                                              command=blur
                                            )
        button_1.grid(row=0, column=0)
        
        button_2 = customtkinter.CTkButton(master=self.frame_down,
                                           corner_radius=0, 
                                           text="Outline",
                                           padx=5, pady=0,
                                           command=outline,
                                           )
        button_2.grid(row=1, column=0)
        
        button_3 = customtkinter.CTkButton(master=self.frame_down,
                                           corner_radius=0, 
                                           text="Default",
                                           padx=5, pady=5,
                                           command=default_img)
        button_3.grid(row=2, column=0)
        

        
        
        
        
        
        
        
    
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
    










    
    
# def lineout():
#     before = input_image
#     after = before.filter(ImageFilter.FIND_EDGES)
#     after.save("lined_img.JPG")
    
# blur()
# lineout()
