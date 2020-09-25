from tkinter import*
from selenium import webdriver
from time import sleep
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title('Youtube Automation')
# Your icon location
root.iconbitmap('Graphics-Vibe-Neon-Glow-Social-Youtube.ico')
root.geometry("400x250")
# Chrome driver Location
driver = webdriver.Chrome('chromedriver.exe')

def search():
    a = enter.get()
    if a !="":
        driver.get("https://www.youtube.com/")
        driver.find_element_by_name("search_query").send_keys(a)
        driver.find_element_by_id("search-icon-legacy").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()
        driver.maximize_window()
        x = enter.get()
        y = Label(root, text=x, font=("Times", 10, "italic"))
        y.pack()
    else:
        messagebox.showerror("Error!!", "The Search area is Empty!!")

def exit():
    z = messagebox.askyesno("Exit!!", "Do you want to exit ?")
    if z==1:
        driver.quit()
        root.quit()
    else:
        return

def mute_btn():
    driver.find_element_by_xpath('//*[@id="movie_player"]/div[28]/div[2]/div[1]/span[4]/button').click()

def playbtn():
    driver.find_element_by_xpath('//*[@id="movie_player"]/div[28]/div[2]/div[1]/span[2]/button').click()

b = Label(root, text="Youtube Automation", fg="red", font=("Times", 18, "bold"))
b.pack()
# Search Area

enter = Entry(root, width=40, borderwidth=5, font=("Times", 14))
enter.pack()

# Search Button
btn = Button(root, text="Search", command=search, font=("Times", 11))
btn.pack()

# Pause And Play Btn
paus = Button(root, text="Pause/Play", command=playbtn)
paus.pack()

# Mute Btn
mute = Button(root, text="Mute/UnMute", command=mute_btn)
mute.pack()
# Exit
btn3 = Button(root, text="Exit", command=exit, font=("Times", 11))
btn3.pack()

root.mainloop()
