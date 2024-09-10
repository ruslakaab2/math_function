from liblary import *
def yraw_menu():
    try:
        wnd=Tk()
        wnd.title("квадратные уравнения с решением теореммы виета и дискриминанта ")
        wnd['bg']="Yellow"
        wnd.geometry("500x500+600+250")

        resh=Label(wnd, text="_")
        resh.grid(column=0,row=5)
        def GO_resh():
            a=int(entry_a.get())
            b=int(entry_b.get())
            c=int(entry_c.get())
            s=sposob.get()
            print(s)
            x1,x2,reshenie=resh_descim_vieta(a,b,c,s)
            resh.config(text=reshenie)



        text1=Label(wnd,text="Решение квадратных уравнений \n ax**2+bx+c",font=("Arial",12,"bold"))
        lbl_a=Label(wnd,text="a=")
        lbl_b=Label(wnd,text="b=")
        lbl_c=Label(wnd,text="c=")
        entry_a=Entry(wnd)
        entry_b=Entry(wnd)
        entry_c=Entry(wnd)
        sposob=IntVar()
        yraw_go=Button(wnd,text="\nРешить уравнение\n",bg="orange",command=GO_resh)
        text1.grid(column=0,row=0)
        lbl_a.grid(column=1, row=1)
        lbl_b.grid(column=1,row=2)
        lbl_c.grid(column=1, row=3)
        entry_a.grid(column=2, row=1)

        entry_b.grid(column=2,row=2)
        entry_c.grid(column=2, row=3)
        Label(wnd,text="способ решения уравнения").grid(column=0,row=1)
        tk.Radiobutton(wnd,text="Теорема Виета",variable=sposob,value=1,command=lambda :sposob.set(1)).grid(column=0,row=2)
        tk.Radiobutton(wnd,text="Дискриминант",variable=sposob,value=2,command=lambda :sposob.set(2)).grid(column=0,row=3)
        yraw_go.grid(column=0,row=4)
    except:
        return "нету","нету","ОШИБКА!"



        wnd.mainloop()
