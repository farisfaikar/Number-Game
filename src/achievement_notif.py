from tkinter import *

from PIL import Image, ImageTk

from globalvar import ACHIEVEMENT_LIST


def achv_notif(index: int):
    achv_message = ACHIEVEMENT_LIST[index - 1]
    ## dimensions
    wd = 530
    hg = 280

    ## style
    bg_c = "#2d162d"  ### c for color
    head_c = "#f7f4c4"
    head_style = ("Charybdis", 17, "bold")
    achv_c = "#f19d5d"
    achv_style = ("Charybdis", 15)

    ## main window
    main = Tk()
    main.title("New Achievement")
    main.iconbitmap("sprite/number_game.ico")
    main.geometry(f"{wd}x{hg}")
    main.minsize(wd, hg)
    main.maxsize(wd, hg)

    ## background
    back = Frame(main)
    back.pack()
    bgimg = ImageTk.PhotoImage(
        Image.open("sprite/tv.png").resize((wd, hg)), master=back
    )
    limg = Label(back, i=bgimg)
    limg.config(bg=bg_c)  # hex code for the PURPLE used in bg game screen
    limg.grid(column=0, row=0, columnspan=3, rowspan=3)

    ## message
    mesg = Label(back, text="Congratulations !", bg=bg_c, fg=head_c)
    mesg.configure(font=head_style)
    mesg.grid(column=0, row=0, columnspan=3)

    mesg = Label(
        back,
        text=achv_message.replace(
            ": ", "\n" + "-" * int(3 * len(achv_message.split(":")[0]) / 2) + "\n"
        ),
        bg=bg_c,
        fg=achv_c,
    )
    mesg.configure(font=achv_style)
    mesg.grid(column=0, row=1, columnspan=3)

    ## ok button
    button = Button(back, text="Continue", command=main.destroy)
    button.configure(
        activebackground="DARKGREEN",
        activeforeground="GREY",
        bg="#74a441",
        fg="WHITE",
        borderwidth=3,
        overrelief="groove",
        state="normal",
        relief="ridge",
        takefocus=0,
        font=("Charybdis", 12, "bold"),
    )
    button.grid(row=2, column=2)

    main.mainloop()


def all_achievements(list_ach):
    for a in list_ach:
        achv_notif(a)


if __name__ == "__main__":
    achv_notif(2)
