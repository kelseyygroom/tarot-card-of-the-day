from tarot_backend import draw_card, get_date_string
import tkinter as tk
from tkinter import font, Label
from PIL import Image, ImageTk, ImageFont, ImageDraw

def main():
    # get card information from card database and backend functionality
    __, name, description, image_path = draw_card().values()
    
    # create window root and configure
    root = tk.Tk()
    root.geometry("600x700")
    root.configure(background="white")

    # creating title from custom font
    custom_title_font = ImageFont.truetype("fonts/Mistic-Regular.ttf", 50)
    img = Image.new("RGBA", (600,73), color="white")
    draw = ImageDraw.Draw(img)
    draw.text((100, 10), "Your Card of the Day", font=custom_title_font, fill="black")
    tk_img = ImageTk.PhotoImage(img)

    title = tk.Label(root, image=tk_img, borderwidth=0, highlightthickness=0, relief="flat")

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_lable = tk.Label(root, image=photo, borderwidth=0, highlightthickness=0, relief="flat")
    
    
    # subtitle label using custom font
    date_str = get_date_string()
    custom_subtitle_font = ImageFont.truetype("fonts/Mistic-Regular.ttf", 27)
    sub_img = Image.new("RGBA", (300,45), color="white")
    draw_subtitle = ImageDraw.Draw(sub_img)
    draw_subtitle.text((23,5), date_str, font=custom_subtitle_font, fill="black")
    subtitle_tk = ImageTk.PhotoImage(sub_img)

    sub_label = tk.Label(root, image=subtitle_tk, borderwidth=0, highlightthickness=0, relief="flat")
    sub_label.image = subtitle_tk

    # open the tarot card image
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_lable = tk.Label(root, image=photo, borderwidth=0, highlightthickness=0, relief="flat")


    # pack the GUI
    title.pack()
    sub_label.pack()
    image_lable.pack()
    

    root.mainloop()

    

if __name__ == "__main__":
    main()