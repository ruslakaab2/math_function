from liblary import *

def resh_descim_vieta(a, b, c ,sposob):
    try:
        reshenie="ошибка"
        x1="нету"
        x2="нету"
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            if a>1:
                x1=(-b+(math.sqrt(discriminant)))/(2*a)
                x2=(-b-(math.sqrt(discriminant)))/(2*a)
            if a==1:
                x1 = (-b + (math.sqrt(discriminant))) / (2)
                x2 = (-b - (math.sqrt(discriminant))) / (2)
            if sposob==1:
                sum_korn=-(b/a)
                mnoj_korn=c/a
                reshenie=(f"{a}x**2+{b}x+{c} \n D={b}**2 - 4 * {a} * {c} = {discriminant}>0 \n x1+x2 = {sum_korn} \n x1*x2 = {mnoj_korn} \n Ответ:x1={x1} x2={x2}")
            else:
                reshenie = (f"{a}x**2+{b}x+{c} \n D={b}**2 - 4 * {a} * {c} = {discriminant}>0 \n x1= (-{b} + {math.sqrt(discriminant)}) / {a} * 2 \n x2=(-{b} - {math.sqrt(discriminant)}) / {a} * 2 \n Ответ:x1={x1} x2={x2}")
        elif discriminant==0:
            if a>1:
                x1=(-b)/(2*a)
            if a==1:
                x1 = (-b) / (2)
            reshenie = (
                f"{a}x**2+{b}x+{c} \n D={b}**2 - 4 * {a} * {c} = {discriminant} -> 1 корень и прийдеться решать дискриминантом "
                f"\n x1= -{b} / ({a} * 2) \n"
                f" Ответ:x1={x1}")
            x2="его нет"
        else:
            reshenie=(f"{a}x**2+{b}x+{c} \n D={b}**2 - 4 * {a} * {c} = {discriminant}<0 \n Ответ : корней нет")
        return x1,x2,reshenie
    except (TypeError, ValueError):
        return 0,0,"возникла ошибка"





