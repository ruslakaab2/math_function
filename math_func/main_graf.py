from liblary import *
def grafiks_func() :


    func_math = ["k*x+b", "k/x","x^3"]

    wnd = Tk()
    wnd.geometry("250x250+500+250")
    wnd.title("графики функций")
    wnd["bg"] = ("purple")

    lbl1 = Label(wnd, text="функции", fg="black", bg="blue")
    lbl1.grid(column=0, row=0)

    text_y = Label(wnd, text="y = ")
    text_y.grid(column=0, row=1)

    combo_box = ttk.Combobox(wnd, value=func_math)
    combo_box.grid(column=1, row=1)

    def get_func():
        global lbl_k, entry_k, lbl_b, entry_b, button_final

        lbl_b = Label(wnd, text="b= ")
        entry_b = Entry(wnd)
        lbl_b.grid(column=0, row=3)
        entry_b.grid(column=1, row=3)

        if combo_box.get() == "k*x+b":
            lbl_k = Label(wnd, text="k= ")
            entry_k = Entry(wnd)
            lbl_k.grid(column=0, row=4)
            entry_k.grid(column=1, row=4)
        elif combo_box.get() == "k/x":
            lbl_k = Label(wnd, text="k= ")
            entry_k = Entry(wnd)
            lbl_k.grid(column=0, row=4)
            entry_k.grid(column=1, row=4)
            lbl_b.destroy()
            entry_b.destroy()
        elif combo_box.get() == "x^3":
            lbl_b.destroy()
            entry_b.destroy()


        def on_final_button_click():
            if combo_box.get() == "x^3":
                opred_func_result = opred_func(combo_box.get())
            elif combo_box.get() == "k*x+b":
                k = entry_k.get()
                b = entry_b.get()
                opred_func_result = opred_func(combo_box.get(), int(k), int(b))
            elif combo_box.get()=="k/x":
                k = entry_k.get()
                opred_func_result = opred_func(combo_box.get(), int(k))


        button_final = Button(wnd, text="вывести результат", command=on_final_button_click)
        button_final.grid(column=1, row=5)

    button = Button(wnd, text="выбрать функцию", command=get_func)
    button.grid(column=1, row=2)

    wnd.mainloop()
