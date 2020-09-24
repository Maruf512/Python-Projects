from tkinter import*
from selenium import webdriver
from time import sleep
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title('Youtube Automation')
# icon location
root.iconbitmap('D:/Documents/ICON/Graphicloads-Flat-Finance-Global.ico')
root.geometry("250x200")

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')

def search():
    a = btn2.get()
    if a != "":
        driver.get("https://www.youtube.com/")
        driver.find_element_by_name("search_query").send_keys(a)
        driver.find_element_by_id("search-icon-legacy").click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()
        driver.maximize_window()
    else:
        messagebox.showerror("Error!!", "The Search area is Empty!!")


b = Label(root, text="Youtube Automation").pack()
# Search Area
btn2 = Entry(root, width=40, borderwidth=5).pack()
# Search Button
btn = Button(root, text="Search", command=search).pack()


root.mainloop()