from tkinter import *
from PIL import Image, ImageTk
from globalvar import ACHIEVEMENT_LIST

def achv_notif(index:int):
    achv_message = ACHIEVEMENT_LIST[index-1]
    ## dimensions
    wd = 530
    hg = 280

    ## style
    bg_c = "#2d162d"       ### c for color
    head_c = "YELLOW" 
    head_style = ("Charybdis", 17, "bold")
    achv_c = "WHITE"
    achv_style = ("Charybdis", 15)

    ## main window
    main = Tk()
    main.title("Congratulations")
    main.iconbitmap('sprite/number_game.ico')
    main.geometry(f"{wd}x{hg}")
    main.minsize(wd, hg)
    main.maxsize(wd, hg)

    ## background 
    back = Frame(main)  
    back.pack()
    bgimg= ImageTk.PhotoImage(Image.open("sprite/tv.png").resize((wd,hg)))
    limg= Label(back, i=bgimg)
    limg.config(bg=bg_c) # hex code for the PURPLE used in bg game screen
    limg.grid(column=0, row=0, columnspan=3,rowspan=3)
    
    ## message
    mesg = Label(back, text="You have unlocked a new achievement !", bg=bg_c, fg=head_c)
    mesg.configure(font=head_style)
    mesg.grid(column=1, row=0)

    mesg = Label(back, text=achv_message.replace(": ","\n"+"-"*int(3*len(achv_message.split(":")[0])/2)+"\n"), bg=bg_c, fg=achv_c)
    mesg.configure(font=achv_style)
    mesg.grid(column=1, row=1)

    main.mainloop()



if __name__ == "__main__":
    achv_notif(1)