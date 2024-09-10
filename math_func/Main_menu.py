from liblary import *

wnd = Tk()
wnd.geometry("300x200+250+250")
wnd["bg"] = "Green"
wnd.title("математические сложности -> это просто")

lbl1 = Label(wnd, text="выберите чем хотите воспользоваться ")
graf_button = Button(wnd, text="графики функций", command=main_graf.grafiks_func)
yraw_button = Button(wnd, text="квадратные уравнения",command=yraw_menu)

lbl1.grid(column=1,row=0)
graf_button.grid(column=1,row=2)
yraw_button.grid(column=1,row=3)
wnd.mainloop()