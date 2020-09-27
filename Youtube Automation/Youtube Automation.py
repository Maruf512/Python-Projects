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
# History Bar

frame_s = LabelFrame(root,bd=3,relief=GROOVE,text="History",font=("Times",11,"italic"))
frame_s.place(x=10,y=140,width=380,height=103)

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
        text_s = Label(frame_s, text=x, font=("Times", 12, "italic")).pack()

    else:
        messagebox.showerror("Error!!", "The Search area is Empty!!")

def exit():
    z = messagebox.askyesno("Exit!!", "Do you want to exit ?")
    if z==1:
        driver.quit()
        root.quit()


# def mute_btn():
#     driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[28]/div[2]/div[1]/span[4]/button').click()

# def playbtn():
#     driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[28]/div[2]/div[1]/span[2]/button').click()

b = Label(root, text="Youtube Automation", fg="white", bg="red", bd=10, pady=2, font=("Times", 18, "bold"))
b.pack(fill=X)
# Search Area

enter = Entry(root, width=33, borderwidth=5, font=("Times", 14))
enter.place(x=13.5, y=55)

# Search Button
btn = Button(root, text="Search", padx=5, pady=3, bd=2, command=search, font=("Times", 11))
btn.place(x=330, y=53)

# # Pause And Play Btn
# paus = Button(root, text="Play", padx=5, pady=3, bd=2, command=playbtn, font=("Times", 10))
# paus.place(x=13.5, y=95)

# # Mute Btn
# mute = Button(root, text="Mute", padx=5, pady=3, bd=2, command=mute_btn, font=("Times", 10))
# mute.place(x=70, y=95)
# # Exit
btn3 = Button(root, text="Exit", padx=5, pady=3, bd=2, command=exit, font=("Times", 10))
btn3.place(x=132, y=95)




root.mainloop()
