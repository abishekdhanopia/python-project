import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import Tk,font
from tkinter import messagebox
from PIL import ImageTk,Image


#student login inside:
def studentlogin(wind):
    wind.destroy()
    wind=Tk()
    wind.geometry("1500x700")
    wind.title("Student Login")
    frame=Frame(wind,width=1500,height=800,bg="plum3")
    frame.pack()
    f=font.Font(weight="bold",family="Serif",size=45)
    x=Label(frame,text="STUDENT IDENTIFICATION",font=f)
    x.configure(bg="plum3",fg="gray23")
    x.place(relx=.20,rely=.05)

    label_font=font.Font(weight="bold",family="Serif",size=30)
    a=Label(wind,text="Password:",font=label_font,bg="plum3")
    a.place(relx=.20,rely=.45)
    d=Label(wind,text="User Name:",font=label_font,bg="plum3")
    d.place(relx=.20,rely=.30)
    a1=Entry(font=label_font,bg="lavender")
    a1.place(relx=.40,rely=.45)
    d1=Entry(font=label_font,bg="lavender")
    d1.place(relx=.40,rely=.30)

 

    #logic in click the student login button:
    def studentloginpage(wind):
        wind.destroy()
        wind=Tk()
        wind.title("Student registered page")
        wind.geometry("1500x900")
        frame=Frame(wind,width=1500,height=50,bg="purple2")
        frame.place(anchor="n",relx=0.5,rely=0)
        frame.pack()

        f=font.Font(weight="bold",family="Serif",size=30)
        s=Label(frame,text="REGISTERED FOR JOINT ENTRANCE EXAM(MAIN)",font=f)
        s.configure(bg="purple2",fg="yellow")
        s.place(relx=.27,rely=.1)


        f=font.Font(weight="bold",family="Serif",size=28)
        t="STUDENT PROFILE"
        l=Label(wind,text=t,font=f).place(relx=.42,rely=.1)

        frame2=Frame(wind,width=1500,height=50,bg="purple2")
        frame2.place(relx=.0,rely=.9)
        f=font.Font(weight="bold",family="Serif",size=30)
        x=Label(frame2,text="Thank you for registration Best of Luck !!!",font=f)
        x.configure(bg="purple2",fg="yellow")
        x.place(relx=.25,rely=.1)

        
        frame2=Frame(wind,width=367,height=585,bg="purple2") 
        frame2.place(relx=0.13,rely=0.49,anchor="center")

        label_font=font.Font(weight="bold",family="Serif",size=25)
        rec1=Button(frame2,text="Home",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        rec1.place(relx=.03,rely=.10)

        
        label_font=font.Font(weight="bold",family="Serif",size=25)
        rec2=Button(frame2,text="Upload",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        rec2.place(relx=.03,rely=.28)

        
        label_font=font.Font(weight="bold",family="Serif",size=25)
        rec3=Button(frame2,text="Save",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        rec3.place(relx=.03,rely=.46)

        label_font=font.Font(weight="bold",family="Serif",size=25)
        rec4=Button(frame2,text="Delete",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        rec4.place(relx=.03,rely=.64)

        label_font=font.Font(weight="bold",family="Serif",size=25)
        rec5=Button(frame2,text="Logout",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        rec5.place(relx=.03,rely=.82)


        var=open("stpro.txt","r")
        a=Label(wind,text="Mother Occupation:",font=label_font,fg="black").place(relx=.3,rely=.8)
        b=Label(wind,text="Mother Name:",font=label_font,fg="black").place(relx=.3,rely=.75)
        c=Label(wind,text="Father Occupation:",font=label_font,fg="black").place(relx=.3,rely=.7)
        d=Label(wind,text="Father Name:",font=label_font,fg="black").place(relx=.3,rely=.65)
        e=Label(wind,text="Location:",font=label_font,fg="black").place(relx=.3,rely=.6)
        d=Label(wind,text="State:",font=label_font,fg="black").place(relx=.3,rely=.55)
        e=Label(wind,text="Religion:",font=label_font,fg="black").place(relx=.3,rely=.5)
        f=Label(wind,text="Email ID:",font=label_font,fg="black").place(relx=.3,rely=.45)
        g=Label(wind,text="Registration Number:",font=label_font,fg="black").place(relx=.3,rely=.4)
        h=Label(wind,text="Gender:",font=label_font,fg="black").place(relx=.3,rely=.35)
        i=Label(wind,text="Date Of Birth:",font=label_font,fg="black").place(relx=.3,rely=.3)
        j=Label(wind,text="Age:",font=label_font,fg="black").place(relx=.3,rely=.25)
        k=Label(wind,text="Student Name:",font=label_font,fg="black").place(relx=.3,rely=.2)
        var.close()


    #student login button
    label_font=font.Font(weight="bold",family="Serif",size=30)
    w=Button(wind,text="Login",bg="lavender",activebackground="dimgray",command=lambda:studentloginpage(wind),font=label_font)
    w.place(relx=.45,rely=.75)
    wind.mainloop() 


#student registration inside:
def StudentRegistration(wind):
    wind.destroy()
    wind=Tk()
    wind.geometry("1500x700")
    wind.title("Student Registration")
    frame=Frame(wind,width=1500,height=800,bg="plum3")
    frame.pack()

    #parent biodata label:
    f=font.Font(weight="bold",family="Serif",size=23)
    x=Label(frame,text="PARENT BIODATA",font=f)
    x.configure(bg="plum3",fg="gray23")
    x.place(relx=.70,rely=.0)

    #parent biodata information:
    label_font=font.Font(weight="bold",family="Serif",size=17)
    h=Label(wind,text="Mother Occupation:",font=label_font,bg="plum3")
    h.place(relx=.6,rely=.4)
    j=Label(wind,text="Mother Name:",font=label_font,bg="plum3")
    j.place(relx=.6,rely=.3)
    k=Label(wind,text="Father Occupation:",font=label_font,bg="plum3")
    k.place(relx=.6,rely=.2)
    l=Label(wind,text="Father Name:",font=label_font,bg="plum3")
    l.place(relx=.6,rely=.1)

    #parent biodata entry box:
    label_font=font.Font(weight="bold",family="Serif",size=14)
    h1=Entry(font=label_font,bg="lavender")
    h1.place(relx=.8,rely=.4)
    j1=Entry(font=label_font,bg="lavender")
    j1.place(relx=.8,rely=.3)
    k1=Entry(font=label_font,bg="lavender")
    k1.place(relx=.8,rely=.2)
    l1=Entry(font=label_font,bg="lavender")
    l1.place(relx=.8,rely=.1)



    #student biodata label:
    f=font.Font(weight="bold",family="Serif",size=20)
    x=Label(frame,text="STUDENT BIODATA",font=f)
    x.configure(bg="plum3",fg="gray23")
    x.place(relx=.12,rely=.0)

    #location:
    label_font=font.Font(weight="bold",family="Serif",size=17)
    a=Label(wind,text="Location:",font=label_font,bg="plum3")
    a.place(relx=.03,rely=.90)

    #Combo box State Selection:
    label_font=font.Font(weight="bold",family="Serif",size=17)
    combo=Label(wind,text="State:",font=label_font,bg="plum3")
    combo.place(relx=.03,rely=.80)
    label_font=font.Font(weight="bold",family="Serif",size=16)
    combo=ttk.Combobox(wind,font=label_font,values=["andhrapradesh","arunachalpradesh","assam","bihar","chhattisgarh","goa","gujurat","haryana","himachalpradesh","jharkhand","karnataka","kerala","madhyapradesh","maharastra","manipur","meghalaya","mizoram","nagaland","odisha","punjab","rajasthan","sikkim","tamilnadu","telangana","tripura","uttarakhand","uttarpradesh","westbengal"])
    combo.place(relx=.3,rely=.80)

    #registration number to religion
    label_font=font.Font(weight="bold",family="Serif",size=17)
    b=Label(wind,text="Religion:",font=label_font,bg="plum3")
    b.place(relx=.03,rely=.70)
    c=Label(wind,text="Email ID:",font=label_font,bg="plum3")
    c.place(relx=.03,rely=.60)
    d=Label(wind,text="Registration Number:",font=label_font,bg="plum3")
    d.place(relx=.03,rely=.50)

    #Gender Selection:
    r=Label(wind,text="Gender:",font=label_font,bg="plum3")
    r.place(relx=.03,rely=.40)
    var1=IntVar()
    r1=Radiobutton(wind,text="Male",variable=var1,value=1,font=label_font,bg="plum3")
    r1.place(relx=.3,rely=.40)
    r2=Radiobutton(wind,text="Female",variable=var1,value=2,font=label_font,bg="plum3")
    r2.place(relx=.4,rely=.40)

    #student name to date of birth:
    label_font=font.Font(weight="bold",family="Serif",size=17)
    e=Label(wind,text="Date Of Birth:",font=label_font,bg="plum3")
    e.place(relx=.03,rely=.30)
    g=Label(wind,text="Age:",font=label_font,bg="plum3")
    g.place(relx=.03,rely=.20)
    y=Label(wind,text="Student Name:",font=label_font,bg="plum3")
    y.place(relx=.03,rely=.10)

    #student biodata entry box:
    label_font=font.Font(weight="bold",family="Serif",size=14)
    a1=Entry(font=label_font,bg="lavender")
    a1.place(relx=.30,rely=.10)
    b1=Entry(font=label_font,bg="lavender")
    b1.place(relx=.30,rely=.20)
    c1=Entry(font=label_font,bg="lavender")
    c1.place(relx=.30,rely=.30)
    d1=Entry(font=label_font,bg="lavender")
    d1.place(relx=.30,rely=.50)
    e1=Entry(font=label_font,bg="lavender")
    e1.place(relx=.30,rely=.60)
    f1=Entry(font=label_font,bg="lavender")
    f1.place(relx=.30,rely=.70)
    g1=Entry(font=label_font,bg="lavender")
    g1.place(relx=.30,rely=.90)


    #connect to file handling:

    #activate register button:
    
    def new1():
        var=open("stpro.txt","a")
        var.write("\n"+a1.get()+"\t")
        var.write(b1.get()+"\t")
        var.write(c1.get()+"\t")
        var.write(d1.get()+"\t")
        var.write(e1.get()+"\t")
        var.write(f1.get()+"\t")
        var.write(g1.get()+"\t")
        var.write(combo.get()+"\t")
        var.write(str(var1.get())+"\t")
        var.write(h1.get()+"\t")
        var.write(j1.get()+"\t")
        var.write(k1.get()+"\t")
        var.write(l1.get()+"\t")
        var.close()
        studentlogin(wind)

    #Register Button:
    label_font=font.Font(weight="bold",family="Serif",size=20)
    w=Button(wind,text="Register",bg="lavender",activebackground="dimgray",command=lambda:new1(),font=label_font)
    w.place(relx=.76,rely=.52)


    wind.mainloop()


#admin login inside:
def adminlogin(wind):
    wind.destroy()
    wind=Tk()
    wind.geometry("1500x700")
    wind.title("Admin Login")
    frame=Frame(wind,width=1500,height=800,bg="plum3")
    frame.pack()
    f=font.Font(weight="bold",family="Serif",size=45)
    x=Label(frame,text="ADMIN IDENTIFICATION",font=f)
    x.configure(bg="plum3",fg="gray23")
    x.place(relx=.23,rely=.05)

    label_font=font.Font(weight="bold",family="Serif",size=30)
    a=Label(wind,text="Password:",font=label_font,bg="plum3")
    a.place(relx=.20,rely=.45)
    d=Label(wind,text="User Name:",font=label_font,bg="plum3")
    d.place(relx=.20,rely=.30)
    a1=Entry(font=label_font,bg="lavender")
    a1.place(relx=.40,rely=.45)
    d1=Entry(font=label_font,bg="lavender")
    d1.place(relx=.40,rely=.30)



    #admin dashboard:

    #activate admin login button (check new page open our profile):-

    
    def adminloginpage(wind):
        wind.destroy()
        wind=Tk()
        wind.title("Admin Page")
        wind.geometry("1500x900")
        frame=Frame(wind,width=1500,height=60,bg="purple2")
        frame.place(anchor="n",relx=0.5,rely=0)
        frame.pack()

    # header line of content:
        f=font.Font(weight="bold",family="Serif",size=35)
        k=Label(frame,text="ADMIN IDENTIFY BY JEE(MAIN) REGISTRATION",font=f)
        k.configure(bg="purple2",fg="yellow")
        k.place(relx=.17,rely=.1)


    #Center line of content:
        f=font.Font(weight="bold",family="Serif",size=28)
        t="UNDERTAKING BY NATIONAL TESTING AGENCY"
        l=Label(wind,text=t,font=f).place(relx=.30,rely=.1)


    #Image admin page:
        img=ImageTk.PhotoImage(Image.open("admindash.jpg"))
        label=Label(wind,image=img)
        label.place(relx=.6,rely=.5)
        

    #side view button frame:
        frame1=Frame(wind,width=367,height=579,bg="purple2") 
        frame1.place(relx=0.13,rely=0.49,anchor="center")
        
       

    #home button:
        label_font=font.Font(weight="bold",family="Serif",size=25)
        click1=Button(frame1,text="Home",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        click1.place(relx=.03,rely=.10)

    #student profile button:
        label_font=font.Font(weight="bold",family="Serif",size=25)
        click2=Button(frame1,text="Student Profile",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        click2.place(relx=.03,rely=.28)

    #staff button:
        label_font=font.Font(weight="bold",family="Serif",size=25)
        click3=Button(frame1,text="Staff",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        click3.place(relx=.03,rely=.46)

    #exam scheduled button:
        label_font=font.Font(weight="bold",family="Serif",size=25)
        click4=Button(frame1,text="Exam Scheduled",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        click4.place(relx=.03,rely=.64)
    
    #logout button:
        label_font=font.Font(weight="bold",family="Serif",size=25)
        click5=Button(frame1,text="logout",bg="purple2",fg="yellow",activebackground="lavender",font=label_font)
        click5.place(relx=.03,rely=.82)

    #lower content:
        frame=Frame(wind,width=1500,height=60,bg="purple2")
        frame.place(relx=.0,rely=.9)
        f=font.Font(weight="bold",family="Serif",size=35)
        x=Label(frame,text="CopyAllRights Reserved 2024",font=f)
        x.configure(bg="purple2",fg="yellow")
        x.place(relx=.27,rely=.1)




    #admin login button    
    label_font=font.Font(weight="bold",family="Serif",size=30)
    w=Button(wind,text="Login",bg="lavender",activebackground="dimgray",command=lambda:adminloginpage(wind),font=label_font)
    w.place(relx=.45,rely=.75)
    wind.mainloop()



#home page:
wind=Tk()
wind.title("attendance register")
wind.geometry("1500x700")
frame=Frame(wind,width=1500,height=50,bg="purple2")
frame.place(anchor="n",relx=0.5,rely=0)
frame.pack()

#upper label:
f=font.Font(weight="bold",family="Serif",size=30)
x=Label(frame,text="STUDENT ATTENDANCE REGISTER",font=f)
x.configure(bg="purple2",fg="yellow")
x.place(relx=.25,rely=.1)

#centre decoration:
f=font.Font(weight="bold",family="Serif",size=28)
t="WELCOME TO JEE MAIN ENTRANCE EXAM"
l=Label(wind,text=t,font=f).place(relx=.22,rely=.1)

#Image for homepage:
img=ImageTk.PhotoImage(Image.open("frontend.jpg"))
label=Label(wind,image=img)
label.place(relx=.3,rely=.25)





#student login button:
label_font=font.Font(weight="bold",family="Serif",size=28)
b1=Button(wind,text="Student Login",fg="yellow",bg="purple2",activebackground="lavender",command=lambda:studentlogin(wind),font=label_font)
b1.place(relx=.05,rely=.70)

#sudent registration tbutton:
label_font=font.Font(weight="bold",family="Serif",size=28)
b2=Button(wind,text="Student Registration",fg="yellow",bg="purple2",activebackground="lavender",command=lambda:StudentRegistration(wind),font=label_font)
b2.place(relx=.35,rely=.70)

#admin login button:
label_font=font.Font(weight="bold",family="Serif",size=28)
b3=Button(wind,text="Admin Login",bg="purple2",fg="yellow",activebackground="lavender",command=lambda:adminlogin(wind),font=label_font)
b3.place(relx=.72,rely=.70)

#lower label:
frame=Frame(wind,width=1500,height=50,bg="purple2")
frame.place(relx=.0,rely=.9)
f=font.Font(weight="bold",family="Serif",size=30)
x=Label(frame,text="@ CopyRight 2024 abishek",font=f)
x.configure(bg="purple3",fg="yellow")
x.place(relx=.27,rely=.1)


wind.mainloop()





    
    
    



      





