from tkinter import *
import time
from datetime import datetime, timedelta
from dateutil import parser
import os
import sys
from PIL import ImageTk, Image

# -----------------------------
window =Tk()
window.geometry("950x695+350+10")
window.title("18F-FAMILY APP")
window.resizable(0, 0)
window.config(bg='#b7950b')

def resource_path(relative_path):
    """Get the correct path for bundled files (works for EXE and dev mode)."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, os.path.basename(relative_path))
    return os.path.join(os.path.abspath("."), relative_path)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# path=resource_path0(relative):

window.iconbitmap(resource_path("barlogo2.ico"))


# تابع محاسباتی---------------------------------------
def allesFunc():
    time_format = "%H:%M"
    for act in list4:
        act.delete(0, END)
    # برای ریست کردن مقدار دریافتی entry
    for low in list3:
        low.delete(0, END)
    for vol in list5:
        vol.delete(0, END)
    for te in list6:
        te.delete(0, END)


    entry_sum_A.delete(0, END)
    entry_sum_V.delete(0, END)
    # محاسبه اکتیویته یک میلی لیتر دارو
    if entry0.get() == '':
        print("Please enter whole activity")
    else:
        if (entry0.get()).isdigit() == True and (entry01.get()).isdigit() == True:
            if int(entry0.get()) > 0 and int(entry01.get()) > 0:
                answer = int(entry0.get())/int(entry01.get())
                print(answer)
            else:
                print("input are below zero")
        else:
            print("input are not number")
    if entry02.get() == '':
        print("enter valid start dispense time")
    else:
        if bool(parser.parse(entry02.get())) == True:
            print("start dispense time format is OK")
        else:
            print(ValueError())
    #   محاسبه زمان تزریق اول هر مرکز--------------
    if check_1.get():
        for t0 in list2:
            t0.delete(0, END)
        if entry03.get() !='':
            #  پیام
            payam_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=95)
            entry12.insert(0, payam_time.strftime("%H:%M"))

            #  رجائی
            rajaii_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=125)
            entry22.insert(0, rajaii_time.strftime("%H:%M"))

            #  امام
            emam_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=100)
            entry32.insert(0, emam_time.strftime("%H:%M"))
            #  شریعتی
            shariati_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=115)
            entry42.insert(0, shariati_time.strftime("%H:%M"))

            #  خاتم
            khatam_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) +timedelta(minutes=130)
            entry52.insert(0, khatam_time.strftime("%H:%M"))

            #  محک
            mahak_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=170)
            entry62.insert(0, mahak_time.strftime("%H:%M"))

            # فردوس
            ferdos_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=120)
            entry72.insert(0, ferdos_time.strftime("%H:%M"))

            # undef1
            undef1_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=180)
            entry82.insert(0, undef1_time.strftime("%H:%M"))

            # undef2
            undef2_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=330)
            entry92.insert(0, undef2_time.strftime("%H:%M"))

            # undef3
            undef3_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=180)
            entry10_2.insert(0, undef1_time.strftime("%H:%M"))

            # undef4
            undef4_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=330)
            entry11_2.insert(0, undef2_time.strftime("%H:%M"))

            # undef5
            undef5_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=330)
            entry12_2.insert(0, undef2_time.strftime("%H:%M"))

        else:
            entry03.insert(0, 30)
            payam_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=95)
            entry12.insert(0, payam_time.strftime("%H:%M"))

            #  رجائی
            rajaii_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=125)
            entry22.insert(0, rajaii_time.strftime("%H:%M"))

            #  امام
            emam_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=100)
            entry32.insert(0, emam_time.strftime("%H:%M"))
            #  شریعتی
            shariati_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=115)
            entry42.insert(0, shariati_time.strftime("%H:%M"))

            #  خاتم
            khatam_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) +timedelta(minutes=130)
            entry52.insert(0, khatam_time.strftime("%H:%M"))

            #  محک
            mahak_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=170)
            entry62.insert(0, mahak_time.strftime("%H:%M"))

            # فردوس
            ferdos_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=120)
            entry72.insert(0, ferdos_time.strftime("%H:%M"))

            # undef1
            undef1_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=210)
            entry82.insert(0, undef1_time.strftime("%H:%M"))

            # undef2
            undef2_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=360)
            entry92.insert(0, undef2_time.strftime("%H:%M"))

            
            # undef3
            undef3_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=210)
            entry10_2.insert(0, undef3_time.strftime("%H:%M"))

            # undef4
            undef4_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=360)
            entry11_2.insert(0, undef4_time.strftime("%H:%M"))

            
            # undef5
            undef5_time = datetime.strptime(
                entry02.get(), time_format) + timedelta(minutes=int(entry03.get())) + timedelta(minutes=210)
            entry12_2.insert(0, undef5_time.strftime("%H:%M"))


    else:
        for t0 in list2:
            if t0.get() == entry02.get():
                t0.delete(0, END)
                t0.insert(0, start_dis_time)
            else:
                pass

    # ایجاد حلقه اصلی-----------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    
    counter = 0
    for lm, dose, t0, low, act, vol, te, gb, di in zip(list0, list1, list2, list3, list4, list5, list6, listGBI, listDI):

        time_format = '%H:%M'

        if dose.get() != '':
            req = int(dose.get())
            print(req)
        else:
            req = 0
        print("dose field is empty")

    #    محاسبه اختلا ف زمانی دیسپنس تا تزریق اول
        if t0.get()!='':
            time_sub = datetime.strptime(
                t0.get(), time_format) - datetime.strptime(entry02.get(), time_format)
            print(time_sub.total_seconds() / 60.0)
        else:
            time_sub = 0

    #    محاسبه اکتیویته پایین

        if gb.get() !='':
            gap_time=int(gb.get())
        else:
            gap_time=35


        if di.get() !='':
            dos_inj=int(di.get())
        else:
            dos_inj=10


        sump = 0
        for i in range(req):
            num = dos_inj*2**((i*gap_time)/109.771)
            sump += num

        if entry_percent.get() != '' :
            sump=(sump-(int(entry_percent.get())/100)*sump)
        else:
            pass
    #    خروج از حلقه داخلی---------------
        print(gap_time)
        print(int(sump))
        low.insert(0, int(sump))

    #    محاسبه اکتیویته بالا
        if time_sub != 0:
            high_act = sump*pow(2, (time_sub.total_seconds() / 60.0/109.7))
            act.insert(0, int(high_act))
            print(int(high_act))
        
    #              محاسبه حجم لازم برای هر مرکز
            req_vol = (int(high_act)/int(entry0.get()))*int(entry01.get())
            vol.insert(0, float("{:.2f}".format(req_vol)))
            print(float("{:.1f}".format(req_vol)))
    #              محاسبه زمان تزریق بعدی
            interval_time = (req*gap_time)
            Next_time = datetime.strptime(
                t0.get(), time_format) + timedelta(minutes=interval_time)
            print(Next_time.strftime("%H:%M"))
        else:
            pass
        # رنگی کردن تزریق بعد برای فیلدهای مراکزی که درخواست دارند---------------
        if dose.get() != '':
           te.insert(0, Next_time.strftime("%H:%M"))
           bg_color = lm.cget("background")
           te.config(bg=bg_color)
        else:
        # برگرداندن رنگ تزریق بعد به حالت اولیه برای درخواستهای خالی----------
           default_rgb = te.winfo_rgb("SystemButtonFace") # get default RGB color
           default_hex = '#' + ''.join([hex(c)[2:].zfill(2) for c in default_rgb]) # convert to hex string
           te.config(bg=default_hex) # set background color to default

        counter += 1
    for dose, t0, low, act, vol in zip(list1, list2, list3, list4, list5):
        if dose.get() == '':
            t0.delete(0, END)
            low.delete(0, END)
            act.delete(0, END)
            vol.delete(0, END)
        else:
            pass


        
    #    خروج از حلقه اصلی ---------------------------------
    #        ------------------------------------------------------------------------------------
    #    مجموع اکتیویته بالا
    Sum_act = 0
    for act in list4:
        if act.get() != '':
           Sum_act += float("{:.2f}".format(float(act.get())))
        else:
            act.get() == 0
    entry_sum_A.insert(0, Sum_act)
    #    مجموع حجم مراکز
    Sum_vol = 0
    for vol in list5:
        if vol.get() != '':
           Sum_vol += float(vol.get())
        else:
            vol.get() == 0
    entry_sum_V.insert(0, "{:.2f} ml".format(Sum_vol))

    if Sum_vol > float(entry01.get())-1.0 and entry_percent.get() !='':
        wlabel = Label(frame2, text=f'Required Activity Is Over, Even With {entry_percent.get()} Percent Off', fg="#EC1526",
                       bg="black", font=("NPIYaghooti Regular", 20), width=44).grid(row=0, column=0)

    elif Sum_vol < float(entry01.get())-1.0 and entry_percent.get() !='':
        wlabel = Label(frame2, text=f' !!!Required Activity Is Enough With {entry_percent.get()} Percent Off!!!', fg="#21EE10",
                       bg="black", font=("NPIYaghooti Regular", 20), width=44).grid(row=0, column=0)

    elif Sum_vol > float(entry01.get())-1.0:
        print("not ok")
        wlabel = Label(frame2, text=" !!! Required Activity Is Over !!!", fg="#EC1526",
                       bg="black", font=("0 jadid bold", 20), width=44).grid(row=0, column=0)
    
    else:
        wlabel = Label(frame2, text=" "u'\u2713'"Activity Is Enough", fg="#21EE10", bg="black", font=(
            "0 jadid bold", 20), width=44).grid(row=0, column=0)
    print(check_1.get())  
# f'{name} age is {age} and d={d}'
# -----------------------------------------------------------------------------------------------------
    # ردیف 0
frame0 = Frame(window)
frame0.grid(row=0, padx=0, pady=8)
frame0.configure(bg='#154360')

lable0 = Label(frame0, text="Whole Activity:", fg="#000000", font=(
    "NPIYaghooti Regular", 14, "bold"), width=14).grid(row=0, column=0, padx=1)
entry0 = Entry(frame0, font=("STENCIL", 12),
               bg="#D5DBDB", width=8, justify='center')
entry0.grid(row=0, column=1, padx=2)
lable01 = Label(frame0, text="Whole volume:", fg="#000000", font=(
    "NPIYaghooti Regular", 14, "bold"), width=12).grid(row=0, column=2, padx=2)
entry01 = Entry(frame0, font=("STENCIL", 12),
                bg="#D5DBDB", width=8, justify='center')
entry01.grid(row=0, column=3, padx=2)
entry01.insert(0, 40)
lable02 = Label(frame0, text="D.S Time:", fg="#000000", font=(
    "NPIYaghooti Regular", 14, "bold")).grid(row=0, column=4, padx=2)
entry02 = Entry(frame0, font=("STENCIL", 12),
                bg="#D5DBDB", width=7, justify='center')
start_dis_time = time.strftime('%H:%M')
entry02.insert(0, start_dis_time)
entry02.grid(row=0, column=5, padx=2)
btn = Button(frame0, text="Run", fg="#000000", bg="red", font=(
    "NPIYaghooti Regular", 14, "bold"), width=6, command=allesFunc).grid(row=0, column=6)
# ------------------------------------------------------
#مدت زمان دیسپنس
# -------------------------------------------------------
lable03 = Label(frame0, text="G.T:", fg="#000000", font=(
    "NPIYaghooti Regular", 14, "bold")).grid(row=0, column=7, padx=2)
entry03 = Entry(frame0, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=4, justify='center')
entry03.grid(row=0, column=8, padx=1)
# ----------------------------------------------


# ------------- فریم اصلی ---------------------------------------------------------------

frame1 = Frame(window,bg='#b7950b')
frame1.grid(row=1,column=0 ,pady=0, padx=0, ipadx=0, ipady=0)

# ----------------مقداراکتیویته هر دوز------------------

entryDI1 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI1.grid(row=2, column=0, padx=10)

entryDI2 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI2.grid(row=3, column=0)

entryDI3 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI3.grid(row=4, column=0)

entryDI4 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI4.grid(row=5, column=0)

entryDI5 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI5.grid(row=6, column=0)

entryDI6 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI6.grid(row=7, column=0)

entryDI7 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI7.grid(row=8, column=0)

entryDI8 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI8.grid(row=9, column=0)

entryDI9 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI9.grid(row=10, column=0)

entryDI10 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI10.grid(row=11, column=0)

entryDI11 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI11.grid(row=12, column=0)

entryDI12 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryDI12.grid(row=13, column=0)

# ------GBI فواصل بین تزریق مراکز---------------------------------------------------
entryGB1 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB1.grid(row=2, column=1, padx=10)

entryGB2 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB2.grid(row=3, column=1)

entryGB3 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB3.grid(row=4, column=1)

entryGB4 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB4.grid(row=5, column=1)

entryGB5 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB5.grid(row=6, column=1)

entryGB6 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB6.grid(row=7, column=1)

entryGB7 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB7.grid(row=8, column=1)

entryGB8 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB8.grid(row=9, column=1)

entryGB9 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB9.grid(row=10, column=1)

entryGB10 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB10.grid(row=11, column=1)

entryGB11 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB11.grid(row=12, column=1)

entryGB12 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entryGB12.grid(row=13, column=1)


# ------------- ردیف عناوین---------------------------------------------------------------

label_GBI=Label(frame1, text="EID", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=0)

label_GBI=Label(frame1, text="GBI", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=1)
label_centername = Label(frame1, text="Cen.Name", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=2)
label_ReqNumber = Label(frame1, text="Rq.N", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=3)
label_FirstInjTime = Label(frame1, text="F.I.T", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=4)
label_DeliveryTimeActivity = Label(frame1, text="Del.T.A", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=5)
label_DispenseTimeActivity = Label(frame1, text="Dis.T.A", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=6)
label_NeededVolume = Label(frame1, text="Volume", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=7)
label_NextDispenseTime = Label(frame1, text="N.D.Time", fg="black",
                    bg='#b7950b', font=("0 jadid bold", 14)).grid(row=1, column=8)


# ردیف پیام

label_payam = Entry(frame1, fg="#00001a", bg='#ffa31a', font=(
    "0 jadid bold", 17), width=16, justify=LEFT)
label_payam.grid(row=2, column=2)
label_payam.insert(0, "Payam  :")
# ------------------------------------------------------------
entry11 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry11.grid(row=2, column=3)
# ------------------------------------------------------------
entry12 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry12.grid(row=2, column=4, padx=10)
entry12.insert(0, start_dis_time)

# -------------------------------------------------------------
entry13 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry13.grid(row=2, column=5, padx=10)
# -------------------------------------------------------------
entry14 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry14.grid(row=2, column=6, padx=10)
# -------------------------------------------------------------
entry15 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry15.grid(row=2, column=7, padx=10)
# -------------------------------------------------------------
entry16 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry16.grid(row=2, column=8, padx=10)


# ردیف رجایی

label_rajaii = Entry(frame1, fg="#00001a", bg='#8A2BE2', font=(
    "0 jadid bold", 17), width=16)
label_rajaii.grid(row=3, column=2)
label_rajaii.insert(0, "Rajaii    :")
# ---------------------------------------------------------------
entry21 = Entry(frame1, font=("STENCIL", 12,"bold"),
                bg="#D5DBDB", width=5, justify='center')
entry21.grid(row=3, column=3)
# ---------------------------------------------------------------
entry22 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry22.grid(row=3, column=4, padx=10)
entry22.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry23 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry23.grid(row=3, column=5, padx=10)
# ---------------------------------------------------------------
entry24 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry24.grid(row=3, column=6, padx=10)
# ---------------------------------------------------------------
entry25 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry25.grid(row=3, column=7, padx=10)
# ---------------------------------------------------------------
entry26 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry26.grid(row=3, column=8, padx=10)

# ردیف امام

label_emam = Entry(frame1, fg="#00001a", bg='#66ccff', font=(
    "0 jadid bold", 17), width=16)
label_emam.grid(row=4, column=2)
label_emam.insert(0, "Emam   :")
# ---------------------------------------------------------------
entry31 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry31.grid(row=4, column=3)
# ---------------------------------------------------------------
entry32 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry32.grid(row=4, column=4, padx=10)
entry32.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry33 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry33.grid(row=4, column=5, padx=10)
# ---------------------------------------------------------------
entry34 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry34.grid(row=4, column=6, padx=10)
# ---------------------------------------------------------------
entry35 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry35.grid(row=4, column=7, padx=10)
# ---------------------------------------------------------------
entry36 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry36.grid(row=4, column=8, padx=10)

# ردیف شریعتی

label_shariati = Entry(frame1, fg="#00001a", bg='#ffff4d', font=(
    "0 jadid bold", 17), width=16)
label_shariati.grid(row=5, column=2)
label_shariati.insert(0, "Shariati :")
# ---------------------------------------------------------------
entry41 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry41.grid(row=5, column=3)
# ---------------------------------------------------------------
entry42 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry42.grid(row=5, column=4, padx=10)
entry42.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry43 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry43.grid(row=5, column=5, padx=10)
# ---------------------------------------------------------------
entry44 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry44.grid(row=5, column=6, padx=10)
# ---------------------------------------------------------------
entry45 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry45.grid(row=5, column=7, padx=10)
# ---------------------------------------------------------------
entry46 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry46.grid(row=5, column=8, padx=10)

# ردیف خاتم

label_khatam = Entry(frame1, fg="#00001a", bg='#33cc00', font=(
    "0 jadid bold", 17), width=16)
label_khatam.grid(row=6, column=2)
label_khatam.insert(0, "Khatam :")
# ---------------------------------------------------------------
entry51 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry51.grid(row=6, column=3)
# ---------------------------------------------------------------
entry52 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry52.grid(row=6, column=4, padx=10)
entry52.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry53 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry53.grid(row=6, column=5, padx=10)
# ---------------------------------------------------------------
entry54 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry54.grid(row=6, column=6, padx=10)
# ---------------------------------------------------------------
entry55 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry55.grid(row=6, column=7, padx=10)
# ---------------------------------------------------------------
entry56 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry56.grid(row=6, column=8, padx=10)

# ردیف محک

label_mahak = Entry(frame1, fg="#00001a", bg='#ff3300', font=(
    "0 jadid bold", 17),width=16)
label_mahak.grid(row=7, column=2)
label_mahak.insert(0, "Mahak  :")
# ---------------------------------------------------------------
entry61 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry61.grid(row=7, column=3)
# ---------------------------------------------------------------
entry62 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry62.grid(row=7, column=4, padx=10)
entry62.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry63 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry63.grid(row=7, column=5, padx=10)
# ---------------------------------------------------------------
entry64 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry64.grid(row=7, column=6, padx=10)
# ---------------------------------------------------------------
entry65 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry65.grid(row=7, column=7, padx=10)
# ---------------------------------------------------------------
entry66 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry66.grid(row=7, column=8, padx=10)

# ردیف فردوس

label_ferdos = Entry(frame1, text="Ferdos  :", fg="#00001a", bg='#660066', font=(
    "0 jadid bold", 17), width=16)
label_ferdos.grid(row=8, column=2)
label_ferdos.insert(0,"Ferdos  :")
# ---------------------------------------------------------------
entry71 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry71.grid(row=8, column=3)
# ---------------------------------------------------------------
entry72 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry72.grid(row=8, column=4, padx=10)
entry72.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry73 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry73.grid(row=8, column=5, padx=10)
# ---------------------------------------------------------------
entry74 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry74.grid(row=8, column=6, padx=10)
# ---------------------------------------------------------------
entry75 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry75.grid(row=8, column=7, padx=10)
# ---------------------------------------------------------------
entry76 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry76.grid(row=8, column=8, padx=10)
# ------------------------------------------------------------------------------

# ردیف unknown1

label_entry_undef1 = Entry(frame1, fg="#00001a", bg='#52D9AB', font=(
    "0 jadid bold", 17), width=16)
label_entry_undef1.grid(row=9, column=2)
label_entry_undef1.insert(0, "")
# ---------------------------------------------------------------
entry81 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry81.grid(row=9, column=3)
# ---------------------------------------------------------------
entry82 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry82.grid(row=9, column=4, padx=10)
entry82.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry83 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry83.grid(row=9, column=5, padx=10)
# ---------------------------------------------------------------
entry84 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry84.grid(row=9, column=6, padx=10)
# ---------------------------------------------------------------
entry85 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry85.grid(row=9, column=7, padx=10)
# ---------------------------------------------------------------
entry86 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry86.grid(row=9, column=8, padx=10)
# ------------------------------------------------------------------------------
# ردیف unknown2

label_entry_undef2 = Entry(frame1, fg="#00001a", bg='#8568C3', font=(
    "0 jadid bold", 17), width=16)
label_entry_undef2.grid(row=10, column=2)
label_entry_undef2.insert(0, '')
# ---------------------------------------------------------------
entry91 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry91.grid(row=10, column=3)
# ---------------------------------------------------------------
entry92 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry92.grid(row=10, column=4, padx=10)
entry92.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry93 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry93.grid(row=10, column=5, padx=10)
# ---------------------------------------------------------------
entry94 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry94.grid(row=10, column=6, padx=10)
# ---------------------------------------------------------------
entry95 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry95.grid(row=10, column=7, padx=10)
# ---------------------------------------------------------------
entry96 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry96.grid(row=10, column=8, padx=10)
# ------------------------------------------------------------------------------
# ردیف unknown3

label_entry_undef3 = Entry(frame1, fg="#00001a", bg='#DC57AE', font=(
    "0 jadid bold", 17),width=16)
label_entry_undef3.grid(row=11, column=2)
label_entry_undef3.insert(0,"")
# ---------------------------------------------------------------
entry10_1 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry10_1.grid(row=11, column=3)
# ---------------------------------------------------------------
entry10_2 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry10_2.grid(row=11, column=4, padx=10)
entry10_2.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry10_3 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry10_3.grid(row=11, column=5, padx=10)
# ---------------------------------------------------------------
entry10_4 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry10_4.grid(row=11, column=6, padx=10)
# ---------------------------------------------------------------
entry10_5 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry10_5.grid(row=11, column=7, padx=10)
# ---------------------------------------------------------------
entry10_6 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry10_6.grid(row=11, column=8, padx=10)

# ----------------------------------------------------------------------------------

# ردیف unknown4

label_entry_undef4 = Entry(frame1, fg="#00001a", bg='#8EC8D0', font=(
    "0 jadid bold", 17), width=16)
label_entry_undef4.grid(row=12, column=2)
label_entry_undef4.insert(0, '')
# ---------------------------------------------------------------
entry11_1 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry11_1.grid(row=12, column=3)
# ---------------------------------------------------------------
entry11_2 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry11_2.grid(row=12, column=4, padx=10)
entry11_2.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry11_3 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry11_3.grid(row=12, column=5, padx=10)
# ---------------------------------------------------------------
entry11_4 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry11_4.grid(row=12, column=6, padx=10)
# ---------------------------------------------------------------
entry11_5 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry11_5.grid(row=12, column=7, padx=10)
# ---------------------------------------------------------------
entry11_6 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry11_6.grid(row=12, column=8, padx=10)
# ----------------------------------------------------------------------------------
# ردیف unknown5

label_entry_undef5 = Entry(frame1, fg="#00001a", bg='#B2E31A', font=(
    "0 jadid bold", 17),width=16)
label_entry_undef5.grid(row=13, column=2)
label_entry_undef5.insert(0, '')
# ---------------------------------------------------------------
entry12_1 = Entry(frame1, font=("STENCIL", 12, "bold"),
                bg="#D5DBDB", width=5, justify='center')
entry12_1.grid(row=13, column=3)
# ---------------------------------------------------------------
entry12_2 = Entry(frame1, font=("franklin gothic", 11, "bold"),
                bg="#D5DBDB", fg="red", width=5, justify='center')
entry12_2.grid(row=13, column=4, padx=10)
entry12_2.insert(0, start_dis_time)
# ---------------------------------------------------------------
entry12_3 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry12_3.grid(row=13, column=5, padx=10)
# ---------------------------------------------------------------
entry12_4 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry12_4.grid(row=13, column=6, padx=10)
# ---------------------------------------------------------------
entry12_5 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry12_5.grid(row=13, column=7, padx=10)
# ---------------------------------------------------------------
entry12_6 = Entry(frame1, font=("STENCIL", 12), width=8, justify='center',takefocus=False)
entry12_6.grid(row=13, column=8, padx=10)
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# تعریف تابع کاهش و افزایش زمان تزریق اول مراکز
    
# زمان تزریق اول
list2 = [entry12, entry22, entry32, entry42,
         entry52, entry62, entry72, entry82, entry92, entry10_2, entry11_2, entry12_2]

def plus_first_inj(t0):
    
     time_format = '%H:%M'
     added_time = datetime.strptime(t0.get(), time_format) + timedelta(minutes=5)
     f = open("myfile.txt", "a")
     f = open("myfile.txt", "w")
     f.write(str(added_time))
     t0.delete(0, END)
     t0.insert(0, added_time.strftime("%H:%M"))
     f.close()
     os.remove("myfile.txt")
def minus_first_inj(t0):
     time_format = '%H:%M'
     added_time = datetime.strptime(t0.get(), time_format) - timedelta(minutes=5)
     f = open("myfile.txt", "a")
     f = open("myfile.txt", "w")
     f.write(str(added_time))
     t0.delete(0, END)
     t0.insert(0, added_time.strftime("%H:%M"))
     f.close()
     os.remove("myfile.txt")    
# ------------------------------------------------------------------
   # دکمه های کم و زیاد زمان اولین تزریق
btn_payam_frame=Frame(frame1)
btn_payam_frame.grid(row=2, column=4, sticky="e")

btn_plus_payam = Button(btn_payam_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[0]:plus_first_inj(t0))
btn_plus_payam.grid(row=0, column=0)
btn_minus_payam = Button(btn_payam_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[0]:minus_first_inj(t0))
btn_minus_payam.grid(row=1, column=0)
# -------------------------
btn_rajaii_frame=Frame(frame1)
btn_rajaii_frame.grid(row=3, column=4, sticky="e")

btn_plus_rajaii = Button(btn_rajaii_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[1]:plus_first_inj(t0))
btn_plus_rajaii.grid(row=0, column=0)
btn_minus_rajaii = Button(btn_rajaii_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[1]:minus_first_inj(t0))
btn_minus_rajaii.grid(row=1, column=0)
# -------------------------


btn_emam_frame=Frame(frame1)
btn_emam_frame.grid(row=4, column=4, sticky="e")

btn_plus_emam = Button(btn_emam_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[2]:plus_first_inj(t0))
btn_plus_emam.grid(row=0, column=0)
btn_minus_emam = Button(btn_emam_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[2]:minus_first_inj(t0))
btn_minus_emam.grid(row=1, column=0)
# -------------------------
btn_shariati_frame=Frame(frame1)
btn_shariati_frame.grid(row=5, column=4, sticky="e")

btn_plus_shariati = Button(btn_shariati_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[3]:plus_first_inj(t0))
btn_plus_shariati.grid(row=0, column=0)
btn_minus_shariati = Button(btn_shariati_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[3]:minus_first_inj(t0))
btn_minus_shariati.grid(row=1, column=0)
# -------------------------
btn_khatam_frame=Frame(frame1)
btn_khatam_frame.grid(row=6, column=4, sticky="e")

btn_plus_khatam = Button(btn_khatam_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[4]:plus_first_inj(t0))
btn_plus_khatam.grid(row=0, column=0)
btn_minus_khatam = Button(btn_khatam_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[4]:minus_first_inj(t0))
btn_minus_khatam.grid(row=1, column=0)
# -------------------------
btn_mahak_frame=Frame(frame1)
btn_mahak_frame.grid(row=7, column=4, sticky="e")

btn_plus_mahak = Button(btn_mahak_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[5]:plus_first_inj(t0))
btn_plus_mahak.grid(row=0, column=0)
btn_minus_mahak = Button(btn_mahak_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[5]:minus_first_inj(t0))
btn_minus_mahak.grid(row=1, column=0)
# -------------------------
btn_ferdos_frame=Frame(frame1)
btn_ferdos_frame.grid(row=8, column=4, sticky="e")

btn_plus_ferdos = Button(btn_ferdos_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[6]:plus_first_inj(t0))
btn_plus_ferdos.grid(row=0, column=0)
btn_minus_ferdos = Button(btn_ferdos_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[6]:minus_first_inj(t0))
btn_minus_ferdos.grid(row=1, column=0)
# -------------------------

btn_undef1_frame=Frame(frame1)
btn_undef1_frame.grid(row=9, column=4, sticky="e")

btn_plus_undef1 = Button(btn_undef1_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[7]:plus_first_inj(t0))
btn_plus_undef1.grid(row=0, column=0)
btn_minus_undef1 = Button(btn_undef1_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[7]:minus_first_inj(t0))
btn_minus_undef1.grid(row=1, column=0)
# -------------------------

btn_undef2_frame=Frame(frame1)
btn_undef2_frame.grid(row=10, column=4, sticky="e")

btn_plus_undef2 = Button(btn_undef2_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[8]:plus_first_inj(t0))
btn_plus_undef2.grid(row=0, column=0)
btn_minus_undef2 = Button(btn_undef2_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[8]:minus_first_inj(t0))
btn_minus_undef2.grid(row=1, column=0)
# -------------------------
btn_undef3_frame=Frame(frame1)
btn_undef3_frame.grid(row=11, column=4, sticky="e")

btn_plus_undef3 = Button(btn_undef3_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[9]:plus_first_inj(t0))
btn_plus_undef3.grid(row=0, column=0)
btn_minus_undef3 = Button(btn_undef3_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[9]:minus_first_inj(t0))
btn_minus_undef3.grid(row=1, column=0)
# -------------------------

btn_undef4_frame=Frame(frame1)
btn_undef4_frame.grid(row=12, column=4, sticky="e")

btn_plus_undef4 = Button(btn_undef4_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[10]:plus_first_inj(t0))
btn_plus_undef4.grid(row=0, column=0)
btn_minus_undef4 = Button(btn_undef4_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[10]:minus_first_inj(t0))
btn_minus_undef4.grid(row=1, column=0)
# -------------------------
btn_undef5_frame=Frame(frame1)
btn_undef5_frame.grid(row=13, column=4, sticky="e")

btn_plus_undef5 = Button(btn_undef5_frame, text="+", fg="#000000", bg="green", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[11]:plus_first_inj(t0))
btn_plus_undef5.grid(row=0, column=0)
btn_minus_undef5 = Button(btn_undef5_frame, text="-", fg="#000000", bg="red", takefocus=False, font=(
    "cooper black", 6, "bold"), width=3, height=1, command=lambda t0=list2[11]:minus_first_inj(t0))
btn_minus_undef5.grid(row=1, column=0)



#   ردیف مجموع  و حالت دستی
# چک باکس
#  ایجاد چک باتون


def check1Clicked():
    if check_1.get():
        print('Checkbox 1 selected')
    else:
        print('Checkbox 1 unselected')


check_1 = IntVar()
check_but_1 = Checkbutton(frame1, text='Auto fill time', variable=check_1,
                          onvalue=1, offvalue=0, command=check1Clicked)
check_but_1.grid(row=14, column=4)


# مجموع
label_sum_A = Label(frame1, text=" Activity Sum ", font=("0 jadid bold", 10, "bold"),
                    bg='#adad85')
label_sum_A.grid(row=15, column=6, pady=0, ipady=0)
entry_sum_A = Entry(frame1,bg='#c18585', font=("STENCIL", 14),takefocus=False, width=7, justify='center')
entry_sum_A.grid(row=14, column=6, padx=15)
label_sum_V = Label(frame1, text=" Volume Sum ", font=("0 jadid bold", 10, "bold"),
                    bg='#adad85')
label_sum_V.grid(row=15, column=7, pady=0, ipady=0)
entry_sum_V = Entry(frame1,bg='#c18585', font=("STENCIL", 15),takefocus=False, width=7, justify='center')
entry_sum_V.grid(row=14, column=7, padx=15)
# ------------------------------درصد کاهش

label_enter=Label(frame1,text="apply", font=("0 jadid bold", 10, "bold"),bg='#DA8416')
label_enter.grid(row=14, column=1, padx=0, pady=15)

entry_percent = Entry(frame1, fg="#000000", bg='yellow', font=(
    "NPIYaghooti Regular", 15, "bold"),justify='center' ,width=11)
entry_percent.grid(row=14, column=2)


label_percent=Label(frame1,text=" %  off  ", font=("0 jadid bold", 10, "bold"),bg='#DA8416')
label_percent.grid(row=14, column=3)

# ----------------پنجره اخطار--------

frame2 = Frame(window, height=50, bg='#b7950b')
frame2.grid(row=2, pady=0, padx=0)

wlabel = Label(frame2, text="***Welcom to 18F-FAMILY Dose Calculator***", fg="#24abf7", bg="black", font=(
    "NPIYaghooti Regular", 20), width=60, height=2).grid(row=0, column=0, pady=(10, 0))


# لوگوی پارس ایزوتوپ-----------------------------------

img1 = ImageTk.PhotoImage(Image.open(resource_path("firstlogo.png")))

mylabel = Label(window, image=img1)
mylabel.place(x=-2, y=-2)

# -----------------------------------------
# دکمه start صفحه welcom

def on_click():
    mylabel.destroy()
    startbtn.destroy()


startbtn = Button(window, text="Let's Go", bg="#fad7a0", font=(
    "bold", 10, "bold"), width=8, height=2, command=on_click)
startbtn.place(x=463, y=393)

# -----------------------------------------
# لیست ردیف بالا مربوط به اکتیویته کل و حجم کل و .... 
listuprow=[entry0, entry01, entry02, entry03]

# --------------------------------------------------

# لیست ورودی زمان بین تزریق ها GBI----------

listGBI=[entryGB1,entryGB2,entryGB3,entryGB4,
entryGB5,entryGB6,entryGB7,entryGB8,entryGB9,entryGB10,entryGB11,entryGB12]

# لیست مقدار هر دوز---------------------

listDI=[entryDI1,entryDI2,entryDI3,entryDI4,
entryDI5,entryDI6,entryDI7,entryDI8,entryDI9,entryDI10,entryDI11,entryDI12]


# ردیف لیبل مراکز
list0=[label_payam, label_rajaii, label_emam, label_shariati, label_khatam, label_mahak, label_ferdos,
label_entry_undef1, label_entry_undef2, label_entry_undef3, label_entry_undef4, label_entry_undef5]
# تعداد دوز درخواستی
list1 = [entry11, entry21, entry31, entry41,
         entry51, entry61, entry71, entry81, entry91, entry10_1, entry11_1,entry12_1]
# زمان تزریق اول
list2 = [entry12, entry22, entry32, entry42,
         entry52, entry62, entry72, entry82, entry92, entry10_2, entry11_2,entry12_2]
# اکتیویته پائین
list3 = [entry13, entry23, entry33, entry43,
         entry53, entry63, entry73, entry83, entry93, entry10_3, entry11_3,entry12_3]
# اکتیویته بالا
list4 = [entry14, entry24, entry34, entry44,
         entry54, entry64, entry74, entry84, entry94, entry10_4, entry11_4,entry12_4]
# حجم لازم
list5 = [entry15, entry25, entry35, entry45,
         entry55, entry65, entry75, entry85, entry95, entry10_5, entry11_5,entry12_5]
# تزریق بعدی
list6 = [entry16, entry26, entry36, entry46,
         entry56, entry66, entry76, entry86, entry96, entry10_6, entry11_6,entry12_6]
#  درصد کاهش
list7=[entry_percent]
# لیست دکمه های افزایش
list8=[btn_plus_payam, btn_plus_rajaii, btn_plus_emam, btn_plus_shariati,
btn_plus_khatam,btn_plus_mahak, btn_plus_ferdos, btn_plus_undef1,btn_plus_undef2]
# لیست دکمه های کاهش
list9=[btn_minus_payam, btn_minus_rajaii, btn_minus_emam, btn_minus_shariati,
btn_minus_khatam,btn_minus_mahak, btn_minus_ferdos, btn_minus_undef1,btn_minus_undef2]


concatedlist = listuprow + list0 + list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9


window.mainloop()
