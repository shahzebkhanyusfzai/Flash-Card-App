import tkinter as tk
from PIL import Image, ImageTk
import csv
import random
import pandas as pd
import time


class capstone():


    def UI_Design(self,root):
        root.geometry("700x600")

        # Open and resize background image
        background_image = Image.open("card_back.png")
        background_image = background_image.resize((700, 600), Image.LANCZOS)

        background_photo = ImageTk.PhotoImage(background_image)

        # Create background label and add image
        background_label = tk.Label(root, image=background_photo)
        background_label.place(x=0, y=0)

        # Open and resize foreground image
        front_image = Image.open("card_front.png")
        front_image = front_image.resize((400, 360), Image.LANCZOS)

        front_photo = ImageTk.PhotoImage(front_image)

        # Create foreground label and add image
        front_label = tk.Label(root, image=front_photo)
        front_label.place(x=150, y=50)

        # Create Right button
        Right_image = Image.open("right.png")
        Right_image = Right_image.resize((80, 80), Image.LANCZOS)

        Right_photo = ImageTk.PhotoImage(Right_image)

        Right_Btn = tk.Button(root, image=Right_photo,command=self.RightFunc)
        Right_Btn.place(x=180, y=380)

        # Create Wrong button
        Wrong_image = Image.open("wrong.png")
        Wrong_image = Wrong_image.resize((80, 80), Image.LANCZOS)
        Wrong_photo = ImageTk.PhotoImage(Wrong_image)
        wrong_btn = tk.Button(root, image=Wrong_photo,command=self.WrongFunc)
        wrong_btn.place(x=440, y=380)

        

        while True:
            self.continue_loop = True
            self.myF,self.myE,self.myrow = self.ReturnWords()
            French_label = tk.Label(root,text=self.myF,font=("Arial", 60), fg="Green")
            French_label.place(x=200, y=130)
            root.update()
            # waiting for user to see the word and recall his/her memory for the translated word
            time.sleep(3)
            # French word label needs to be destroyed because the translated or english word will have to come over and take place
            French_label.destroy()
            English_label = tk.Label(root,text=self.myE,font=("Arial", 60), fg="Green")
            English_label.place(x=200, y=130)
            root.update()
            # print(self.myrow)
            # The while loop below ensures the infinite waiting time for the user to decide if he has to click on tick or cross
            while self.continue_loop:
                root.update()
            English_label.destroy()

# This function will get us get hold of french , english words and the random row no the function will generate
    def ReturnWords(self):
        df = pd.read_csv('french_words.csv')
        self.random_row = df.sample().index[0]
        # print(self.random_row)
        self.myfrench = df.iloc[self.random_row]['French']
        self.myenglish = df.iloc[self.random_row]['English']
        return self.myfrench,self.myenglish,self.random_row

#this function is executed when tick is clicked, and makes sure the word gets deleted off the list of our collection of words, and helps in moving forward in the while loop by switching the continue_loop variable
    def RightFunc(self):
        with open('french_words.csv', 'r') as file:
            myval = int(self.random_row) + 1
            rows = list(csv.reader(file))
            rows[myval] = ''
            


        with open('french_words.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row:  # only write row if it's not empty
                    writer.writerow(row)

        self.continue_loop = False
        print('rightfunc')        


# Executed when cross is clicked and helps the while loop in UI function move forward
    def WrongFunc(self):
        self.continue_loop = False
        print('wrongfunc')


          





mygame = capstone()
master = tk.Tk()
mygame.UI_Design(master)


