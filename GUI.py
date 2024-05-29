from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Calories_Counter_App as cc
import matplotlib.pyplot as plt
import PIL as pil
import json

global root
root=CTk()
root.title("Calories Tracking")
root.iconbitmap("dumbbell_41551.ico")
root.geometry("800x600")
root.resizable(0,0)

class App(CTk):
    p=cc.Person()
    
    def __init__(self,master):
        global list
        list=cc.Manager()
        global label_list
        label_list=[]
        
        side_img_data = pil.Image.open("image00019.jpg")
        side_img=CTkImage(side_img_data,size=(400, 600))
        
        global my_label
        my_label=CTkLabel(master,text="",image=side_img)
        my_label.pack(side=LEFT)
        
        global main_frame
        main_frame=CTkFrame(master,width=400,height=600,fg_color="white",corner_radius=0)
        main_frame.pack_propagate(0) # Ngan chan frame thay doi kich thuoc theo noi dung
        main_frame.pack(expand=TRUE, side=RIGHT)
        
        welcome=CTkLabel(main_frame, text="Welcome Back!", text_color="blue", anchor=W, justify=LEFT, font=("Arial Bold", 24))
        welcome.pack(anchor=W,pady=(25,5),padx=(25,0)) # pady them y pixel theo chieu doc, padx them x pixel theo chieu ngang
        # pady=(top, bottom), padx=(left, right)
        
        enter_info=CTkLabel(main_frame,text="Enter your information",text_color="gray",anchor=W,justify=LEFT,font=("Arial Bold", 12))
        enter_info.pack(anchor=W,padx=25)
        
        name=CTkLabel(main_frame, text="Name:", text_color="#2560be", anchor=W, justify=LEFT, font=("Arial Bold", 16))
        name.pack(anchor=W,pady=(20,0),padx=25)
        
        global name_entry
        name_entry=CTkEntry(main_frame,width=300,fg_color="#EEEEEE",border_width=1,border_color="#2560be",text_color="black")
        name_entry.pack(anchor=W,pady=(5,0),padx=25)
        
        age=CTkLabel(main_frame, text="Age:", text_color="#2560be", anchor=W, justify=LEFT, font=("Arial Bold", 16))
        age.pack(anchor=W,pady=(15,0),padx=25)

        global age_entry
        age_entry=CTkEntry(main_frame,width=300,fg_color="#EEEEEE",border_width=1,border_color="#2560be",text_color="black")
        age_entry.pack(anchor=W,pady=(5,0),padx=25)
        
        gender_frame=CTkFrame(main_frame,width=400,height=50,fg_color="white")
        global gender_var
        gender_var=StringVar()
        
        gender=CTkLabel(gender_frame, text="Gender:", text_color="#2560be", anchor=W, justify=LEFT, font=("Arial Bold", 16))
        gender.pack(side=LEFT)
       
        gender_entry1=CTkRadioButton(gender_frame,text= "Male", value= "Male", variable=gender_var,corner_radius=50,
                                     fg_color="#2560be",border_color="#2560be",text_color="#2560be",font=("Arial Bold", 14))
        gender_entry1.pack(side=LEFT,padx=15)
        
        gender_entry2=CTkRadioButton(gender_frame,text= "Female", value= "Female", variable=gender_var,corner_radius=50,
                                     fg_color="#2560be",border_color="#2560be",text_color="#2560be",font=("Arial Bold", 14))
        gender_entry2.pack(side=LEFT)
        
        gender_frame.pack(anchor=W,pady=(15,0),padx=25)

        height=CTkLabel(main_frame, text="Height (cm):", text_color="#2560be", anchor=W, justify=LEFT, font=("Arial Bold", 16))
        height.pack(anchor=W,pady=(15,0),padx=25)
        
        global height_entry
        height_entry=CTkEntry(main_frame,width=300,fg_color="#EEEEEE",border_width=1,border_color="#2560be",text_color="black")
        height_entry.pack(anchor=W,pady=(5,0),padx=25)
        
        weight=CTkLabel(main_frame, text="Weight (kg):", text_color="#2560be", anchor=W, justify=LEFT, font=("Arial Bold", 16))
        weight.pack(anchor=W,pady=(15,0),padx=25)
        
        global weight_entry
        weight_entry=CTkEntry(main_frame,width=300,fg_color="#EEEEEE",border_width=1,border_color="#2560be",text_color="black")
        weight_entry.pack(anchor=W,pady=(5,0),padx=25)
        
        target=CTkLabel(main_frame, text="Target weight (kg):", text_color="#2560be", anchor=W, justify=LEFT, font=("Arial Bold", 16))
        target.pack(anchor=W,pady=(15,0),padx=25)
        
        global target_entry
        target_entry=CTkEntry(main_frame,width=300,fg_color="#EEEEEE",border_width=1,border_color="#2560be",text_color="black")
        target_entry.pack(anchor=W,pady=(5,0),padx=25)
        
        global last_time
        last_time=CTkButton(main_frame,text="Last time",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 17),text_color="white",corner_radius=50,command=self.Last)
        last_time.pack(anchor=W,side=LEFT,padx=25)
        
        global submit
        submit=CTkButton(main_frame,text="Submit >",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 17),text_color="white",corner_radius=50,command=lambda:self.Tab2(master))
        #hover_color: mau khi di chuot vao button
        submit.pack(anchor=W,side=LEFT,padx=50)     
        
    def Last(self):
        with open("user.json","r") as openfile:
            json_object=json.load(openfile)
            self.p.__dict__=json_object
            
        name_entry.insert(0,self.p.getName())
        age_entry.insert(0,self.p.getAge())
        gender_var.set(self.p.getGender())
        height_entry.insert(0,self.p.getHeight())
        weight_entry.insert(0,self.p.getWeight())
        target_entry.insert(0,self.p.getTarget())
                            
    def AddToListB(self):
        if serving_entry.get() != "":
            f.setServ(int(serving_entry.get()))
            list.add(f)
            color_frame2.pack_forget()
            food_frame.pack_forget()
            color_frame1.pack_propagate(0)
            color_frame1.pack(anchor=N)
            breakfast_frame.pack_propagate(0)
            breakfast_frame.pack(side=LEFT,anchor=S)
            lunch_frame.pack_propagate(0)
            lunch_frame.pack(side=LEFT,anchor=S)
            dinner_frame.pack_propagate(0)
            dinner_frame.pack(side=LEFT,anchor=S)
            food_label1=CTkLabel(breakfast_frame,text=f.getName()+" ("+str(f.getServing())+" "+f.getUnit()+")\n",text_color="gray",anchor=W,justify=LEFT,font=("Arial Bold", 18))
            food_label1.pack(side=TOP,anchor=NW,pady=5,padx=5)
            label_list.append(food_label1)
     
    def AddToListL(self):
        if serving_entry.get() != "":
            f.setServ(int(serving_entry.get()))
            list.add(f)
            color_frame2.pack_forget()
            food_frame.pack_forget()
            color_frame1.pack_propagate(0)
            color_frame1.pack(anchor=N)
            breakfast_frame.pack_propagate(0)
            breakfast_frame.pack(side=LEFT,anchor=S)
            lunch_frame.pack_propagate(0)
            lunch_frame.pack(side=LEFT,anchor=S)
            dinner_frame.pack_propagate(0)
            dinner_frame.pack(side=LEFT,anchor=S)
            food_label2=CTkLabel(lunch_frame,text=f.getName()+" ("+str(f.getServing())+" "+f.getUnit()+")\n",text_color="gray",anchor=W,justify=LEFT,font=("Arial Bold", 18))
            food_label2.pack(side=TOP,anchor=NW,pady=5,padx=5)
            label_list.append(food_label2)
        
    def AddToListD(self):
        if serving_entry.get() != "":
            f.setServ(int(serving_entry.get()))
            list.add(f)
            color_frame2.pack_forget()
            food_frame.pack_forget()
            color_frame1.pack_propagate(0)
            color_frame1.pack(anchor=N)
            breakfast_frame.pack_propagate(0)
            breakfast_frame.pack(side=LEFT,anchor=S)
            lunch_frame.pack_propagate(0)
            lunch_frame.pack(side=LEFT,anchor=S)
            dinner_frame.pack_propagate(0)
            dinner_frame.pack(side=LEFT,anchor=S)
            food_label3=CTkLabel(dinner_frame,text=f.getName()+" ("+str(f.getServing())+" "+f.getUnit()+")\n",text_color="gray",anchor=W,justify=LEFT,font=("Arial Bold", 18))
            food_label3.pack(side=TOP,anchor=NW,pady=5,padx=5)
            label_list.append(food_label3)

    def AddFood(self,master):
        master.configure(fg_color="white")
        color_frame1.pack_forget()
        breakfast_frame.pack_forget()
        lunch_frame.pack_forget()
        dinner_frame.pack_forget()
        global color_frame2
        color_frame2=CTkFrame(root,width=800,height=50,fg_color="#2560be",corner_radius=0,border_color="#2560be",border_width=0)
        color_frame2.pack_propagate(0)
        color_frame2.pack(anchor=N)
        global food_frame
        food_frame=CTkFrame(root,width=800,height=550,fg_color="white")
        food_frame.pack_propagate(0)
        food_frame.pack()
        
        select=CTkLabel(food_frame,text="Select your food",text_color="#2560be",anchor=W,justify=LEFT,font=("Arial Bold", 24))
        select.pack(anchor=CENTER,pady=(50,0))
        
        back=CTkButton(color_frame2,text= "< Back",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 18),text_color="white",corner_radius=50,command=self.Back2)
        back.pack(anchor=W,side=LEFT)
        
        global food_list
        food_list=["Pho Bo","Banh Cuon","Banh Mi","Banh Bao","Bun Moc","Bun Rieu","Banh Trang","Pho Ga","Xoi","Mi Goi","Chao Long","Banh Gio","Khoai Lang",
                   "Chao Suon","Bun Bo","Com Trang","Com Tam","Com Rang Dua Bo","Takoyaki","Ramen","Udon","Pizza","Hamburger","Hot Dog","Ga Ran","Kem","Banh Ngot",
                   "Chocolate","Chips","Uc Ga","Thit Bo","Ca Chep","Tom","Dui Ga","Thit Heo","Thit Trau","Thit De","Thit Ngan","Cua","Thit Vit","Thit Chim","Tao","Chuoi"
                   ,"Dao","Nho","Rau Cai","Rau Den","Rau Muong","Trung","Sua Bo"]
        global food
        food=Combobox(food_frame,values=food_list,justify=CENTER,width=30,font=("Times New Roman", 16))
        food.current(0)
        food.bind("<<ComboboxSelected>>",self.Add)
        food.pack(anchor=CENTER,pady=50)
        food.bind("<KeyRelease>",self.Search)
        
    def Search(self,event):
        value=event.widget.get()
        if value=="":
            food["values"]=food_list
            
        else:
            data=[]
            for item in food_list:
                if value.lower() in item.lower():
                    data.append(item)
            food["values"]=data        
        
    def Add(self,event):
        global f
        global serving_entry
        while True:
            if food.get()=="Pho Bo":
                f=cc.PhoBo(0)
                
            elif food.get()=="Banh Cuon":
                f=cc.BanhCuon(0)
                
            elif food.get()=="Banh Mi":
                f=cc.BanhMi(0)
                
            elif food.get()=="Banh Bao":
                f=cc.BanhBao(0)
                                                
            elif food.get()=="Bun Moc":
                f=cc.BunMoc(0)
                
            elif food.get()=="Bun Rieu":
                f=cc.BunRieu(0)
                
            elif food.get()=="Banh Trang":
                f=cc.BanhTrang(0)
                
            elif food.get()=="Pho Ga":
                f=cc.PhoGa(0)
                
            elif food.get()=="Xoi":
                f=cc.Xoi(0)
                
            elif food.get()=="Mi Goi":
                f=cc.MiGoi(0)
                
            elif food.get()=="Chao Long":
                f=cc.ChaoLong(0)
                
            elif food.get()=="Banh Gio":
                f=cc.BanhGio(0)
                
            elif food.get()=="Khoai Lang":
                f=cc.KhoaiLang(0)
                
            elif food.get()=="Chao Suon":
                f=cc.ChaoSuon(0)
                
            elif food.get()=="Bun Bo":
                f=cc.BunBo(0)
                
            elif food.get()=="Com Trang":
                f=cc.ComTrang(0)
                
            elif food.get()=="Com Tam":
                f=cc.ComTam(0)
                
            elif food.get()=="Com Rang Dua Bo":
                f=cc.ComRangDuaBo(0)
                
            elif food.get()=="Takoyaki":
                f=cc.Takoyaki(0)
                
            elif food.get()=="Ramen":
                f=cc.Ramen(0)
                
            elif food.get()=="Udon":
                f=cc.Udon(0)
                
            elif food.get()=="Pizza":
                f=cc.Pizza(0)
                
            elif food.get()=="Hamburger":
                f=cc.Hamburger(0)
                
            elif food.get()=="Hot Dog":
                f=cc.HotDog(0)
                
            elif food.get()=="Ga Ran":
                f=cc.GaRan(0)
                
            elif food.get()=="Kem":
                f=cc.Kem(0)
                
            elif food.get()=="Banh Ngot":
                f=cc.BanhNgot(0)
                
            elif food.get()=="Chocolate":
                f=cc.Chocolate(0)
                
            elif food.get()=="Chips":
                f=cc.Chips(0)
             
            elif food.get()=="Uc Ga":
                f=cc.UcGa(0)
                
            elif food.get()=="Thit Bo":
                f=cc.Bo(0)
                
            elif food.get()=="Ca Chep":
                f=cc.CaChep(0)
                
            elif food.get()=="Tom":
                f=cc.Tom(0)
                
            elif food.get()=="Dui Ga":
                f=cc.DuiGa(0)
                
            elif food.get()=="Thit Heo":
                f=cc.Heo(0)
                
            elif food.get()=="Thit Trau":
                f=cc.Trau(0)
                
            elif food.get()=="Thit De":
                f=cc.De(0)
                
            elif food.get()=="Thit Ngan":
                f=cc.Ngan(0)
                
            elif food.get()=="Cua":
                f=cc.Cua(0)
                
            elif food.get()=="Thit Vit":
                f=cc.Vit(0)
                
            elif food.get()=="Thit Chim":
                f=cc.Chim(0)
                
            elif food.get()=="Tao":
                f=cc.Tao(0)
                
            elif food.get()=="Chuoi":
                f=cc.Chuoi(0)
                
            elif food.get()=="Dao":
                f=cc.Dao(0)
                
            elif food.get()=="Nho":
                f=cc.Nho(0)
                
            elif food.get()=="Rau Cai":
                f=cc.RauCai(0)
                
            elif food.get()=="Rau Den":
                f=cc.RauDen(0)
                
            elif food.get()=="Rau Muong":
                f=cc.RauMuong(0)
                
            elif food.get()=="Trung":
                f=cc.Trung(0)
                
            elif food.get()=="Sua Bo":
                f=cc.SuaBo(0)
                
            food.state(["disabled"]) # Khoa lai combobox
            serving_label=CTkLabel(food_frame,text="Serving size ("+ f.getUnit()+"): ",text_color="#2560be",anchor=W,justify=LEFT,font=("Arial Bold", 24))
            serving_label.pack(anchor=CENTER,pady=(30,0))
            serving_entry=CTkEntry(food_frame,width=300,fg_color="#EEEEEE",border_width=1,border_color="#2560be",text_color="black")
            serving_entry.pack(anchor=CENTER,pady=(20,0))
            add_button1=CTkButton(food_frame,text="Add to breakfast",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 16),text_color="white",corner_radius=50,command=self.AddToListB)
            add_button1.pack(anchor=W,side=LEFT,pady=(10,0),padx=70)
            add_button2=CTkButton(food_frame,text="Add to lunch",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 16),text_color="white",corner_radius=50,command=self.AddToListL)
            add_button2.pack(anchor=W,side=LEFT,pady=(10,0),padx=15)
            add_button3=CTkButton(food_frame,text="Add to dinner",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 16),text_color="white",corner_radius=50,command=self.AddToListD)
            add_button3.pack(anchor=W,side=LEFT,pady=(10,0),padx=70)
            break
            
    def Continue(self):
        if name_entry.get()!="" and age_entry.get()!="0" and gender_var.get()!="" and height_entry.get()!="0"and weight_entry.get()!="0"and target_entry.get()!="0":
            try:
                self.p.setName(str(name_entry.get()))
                self.p.setAge(int(age_entry.get()))
                self.p.setGender(str(gender_var.get()))
                self.p.setHeight(float(height_entry.get()))
                self.p.setWeight(float(weight_entry.get()))
                self.p.setTarget(float(target_entry.get()))
            
                json_string=json.dumps(self.p.__dict__,indent=4) #__dict__ tra ve dictionary chua tat ca thuoc tinh cua object
                with open ("user.json","w") as outfile:
                    outfile.write(json_string)
            
                my_label.pack_forget()
                main_frame.pack_forget()
            
                color_frame1.pack_propagate(0)
                color_frame1.pack(anchor=N)
                breakfast_frame.pack_propagate(0)
                breakfast_frame.pack(side=LEFT,anchor=S)
                lunch_frame.pack_propagate(0)
                lunch_frame.pack(side=LEFT,anchor=S)
                dinner_frame.pack_propagate(0)
                dinner_frame.pack(side=LEFT,anchor=S,fill=X)
            except:
                messagebox.showerror("Error","Please check again your information")       
        else:
            messagebox.showerror("Error","Please fill in all the fields")
                        
    def Back1(self):
        color_frame1.pack_forget()
        breakfast_frame.pack_forget()
        lunch_frame.pack_forget()
        dinner_frame.pack_forget()
        my_label.pack(side=LEFT)
        main_frame.pack_propagate(0)
        main_frame.pack(expand=TRUE, side=RIGHT)
        submit.pack_forget()
        last_time.pack_forget()
        continue1=CTkButton(main_frame,text="Continue",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 16),text_color="white",corner_radius=50,command=self.Continue)
        continue1.pack(anchor=W,pady=(25,0),padx=140)
        
    def Back2(self):
        color_frame2.pack_forget()
        food_frame.pack_forget()
        color_frame1.pack_propagate(0)
        color_frame1.pack(anchor=N)
        breakfast_frame.pack_propagate(0)
        breakfast_frame.pack(side=LEFT,anchor=S)
        lunch_frame.pack_propagate(0)
        lunch_frame.pack(side=LEFT,anchor=S)
        dinner_frame.pack_propagate(0)
        dinner_frame.pack(side=LEFT,anchor=S,fill=X)
        
    def Back3(self):
        color_frame3.pack_forget()
        chart_frame.pack_forget()
        analyze_frame.pack_forget()
        bmi_frame.pack_forget()
        color_frame1.pack_propagate(0)
        color_frame1.pack(anchor=N)
        breakfast_frame.pack_propagate(0)
        breakfast_frame.pack(side=LEFT,anchor=S)
        lunch_frame.pack_propagate(0)
        lunch_frame.pack(side=LEFT,anchor=S)
        dinner_frame.pack_propagate(0)
        dinner_frame.pack(side=LEFT,anchor=S,fill=X)

    def Clear(self):
        list.food_list.clear()
        for item in label_list:
            item.destroy()
    
    def Tab2(self,master):
        if name_entry.get()!="" and age_entry.get()!="0" and gender_var.get()!="" and height_entry.get()!="0"and weight_entry.get()!="0"and target_entry.get()!="0":
            try:    
                self.p.setName(str(name_entry.get()))
                self.p.setAge(int(age_entry.get()))
                self.p.setGender(str(gender_var.get()))
                self.p.setHeight(float(height_entry.get()))
                self.p.setWeight(float(weight_entry.get()))
                self.p.setTarget(float(target_entry.get()))
       
                json_string=json.dumps(self.p.__dict__,indent=4) 
                with open ("user.json","w") as outfile:
                    outfile.write(json_string)
                
                my_label.pack_forget()
                main_frame.pack_forget()
            
                global color_frame1
                color_frame1=CTkFrame(root,width=800,height=50,fg_color="#2560be",corner_radius=0,border_color="#2560be",border_width=0)
                color_frame1.pack_propagate(0)
                color_frame1.pack(anchor=N)
            
                back=CTkButton(color_frame1,text= "< Back",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 18),text_color="white",corner_radius=50,command=self.Back1)
                back.pack(anchor=W,side=LEFT)
            
                how=CTkLabel(color_frame1, text="Meals", text_color="white", anchor=CENTER, font=("Times New Roman Bold", 34))
                how.pack(anchor=CENTER,padx=(0,110))           
            
                global breakfast_frame
                breakfast_frame=CTkFrame(root,width=266,height=550,fg_color="white",corner_radius=0,border_color="black",border_width=1)
                breakfast_frame.pack_propagate(0)
                breakfast_frame.pack(side=LEFT,anchor=S)
                global lunch_frame
                lunch_frame=CTkFrame(root,width=266,height=550,fg_color="white",corner_radius=0,border_color="black",border_width=1)
                lunch_frame.pack_propagate(0)
                lunch_frame.pack(side=LEFT,anchor=S)
                global dinner_frame
                dinner_frame=CTkFrame(root,width=267,height=550,fg_color="white",corner_radius=0,border_color="black",border_width=1)
                dinner_frame.pack_propagate(0)
                dinner_frame.pack(side=LEFT,anchor=S,fill=X)
            
                last_frame1=CTkFrame(breakfast_frame,width=266,height=50,fg_color="#2560be",corner_radius=0,border_color="#2560be",border_width=0)
                last_frame1.pack_propagate(0)
                last_frame1.pack(side=BOTTOM)
            
                last_frame2=CTkFrame(lunch_frame,width=266,height=50,fg_color="#2560be",corner_radius=0,border_color="#2560be",border_width=0)
                last_frame2.pack_propagate(0)
                last_frame2.pack(side=BOTTOM)
            
                last_frame3=CTkFrame(dinner_frame,width=267,height=50,fg_color="#2560be",corner_radius=0,border_color="#2560be",border_width=0)
                last_frame3.pack_propagate(0)
                last_frame3.pack(side=BOTTOM)
            
                b_label=CTkLabel(breakfast_frame, text="Breakfast", text_color="#2560be", anchor=W, justify=CENTER, font=("Arial Bold", 22))
                b_label.pack(anchor=W,pady=(10,10),padx=80)
            
                l_label=CTkLabel(lunch_frame, text="Lunch", text_color="#2560be", anchor=W, justify=CENTER, font=("Arial Bold", 22))
                l_label.pack(anchor=W,pady=(10,10),padx=100)
            
                d_label=CTkLabel(dinner_frame, text="Dinner", text_color="#2560be", anchor=W, justify=CENTER, font=("Arial Bold", 22))
                d_label.pack(anchor=W,pady=(10,10),padx=90)
            
                add1=CTkButton(last_frame2,text= "Add food",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 18),text_color="white",corner_radius=50,command=lambda:self.AddFood(master))
                add1.pack(anchor=N)
            
                proceed=CTkButton(last_frame3,text= "Proceed >",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 18),text_color="white",corner_radius=50,command=self.Tab3)
                proceed.pack(anchor=N)
            
                clearall=CTkButton(last_frame1,text= "Clear all",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 18),text_color="white",corner_radius=50,command=self.Clear)
                clearall.pack(anchor=N)
            
            except:
                messagebox.showerror("Error","Please check again your information")
                
        else:
            messagebox.showerror("Error","Please fill in all the fields")
            
    def Help(self):
        messagebox.showinfo("Help","BMI < 18.5: Underweight\n18.5 <= BMI < 24.9: Normal\n24.9 <= BMI <= 29.9: Overweight\nBMI >= 30: Obese")

    def Tab3(self):
        if len(list.food_list)==0:
            messagebox.showerror("Error","Please add food")
            
        else:
            color_frame1.pack_forget()
            breakfast_frame.pack_forget()
            lunch_frame.pack_forget()
            dinner_frame.pack_forget()
        
            global color_frame3
            color_frame3=CTkFrame(root,width=800,height=50,fg_color="#2560be",corner_radius=0,border_color="#2560be",border_width=0)
            color_frame3.pack_propagate(0)
            color_frame3.pack(anchor=N)

            back=CTkButton(color_frame3,text= "< Back",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 18),text_color="white",corner_radius=50,command=self.Back3)
            back.pack(anchor=W,side=LEFT)

            global chart_frame
            chart_frame=CTkFrame(root,width=400,height=550,fg_color="white",border_color="black",border_width=1,corner_radius=0)
            chart_frame.pack_propagate(0)
            chart_frame.pack(side=LEFT,anchor=W)
        
            global analyze_frame
            analyze_frame=CTkFrame(root,width=400,height=275,fg_color="white",border_color="black",border_width=1,corner_radius=0)
            analyze_frame.pack_propagate(0)
            analyze_frame.pack(side=TOP,anchor=E)
        
            global bmi_frame
            bmi_frame=CTkFrame(root,width=400,height=275,fg_color="white",border_color="black",border_width=1,corner_radius=0)
            bmi_frame.pack_propagate(0)
            bmi_frame.pack(side=BOTTOM,anchor=E)
            
            c=plt.figure(figsize=(20,20))
            nutritions=["Carbohyrates","Protein","Fat"]
            number=[list.CalfromCarbs(),list.CalfromProtein(),list.CalfromFat()]
            plt.pie(number,labels=nutritions,autopct='%2.1f%%')
            plt.title(label="Nutrition Distribution",fontsize=24,pad=25,color="#2560be")
            canvas=FigureCanvasTkAgg(c,chart_frame)
            canvas.get_tk_widget().pack(fill=BOTH,expand=True)
        
            analyze=CTkLabel(analyze_frame,text="Analysis",text_color="#2560be",anchor=N,justify=CENTER,font=("Arial Bold", 24))
            analyze.pack(anchor=N,pady=(20,0))
        
            totalCal=CTkLabel(analyze_frame,text=f"Total Calories: {list.totalCalories():.1f}",text_color="black",anchor=W,justify=LEFT,font=("Arial", 16))
            totalCal.pack(anchor=W,pady=(15,0),padx=10)
            totalCarbs=CTkLabel(analyze_frame,text=f"Carbs: {list.totalCarbs():.1f} g",text_color="black",anchor=W,justify=LEFT,font=("Arial", 16))
            totalCarbs.pack(anchor=W,pady=(10,0),padx=10)
            totalProtein=CTkLabel(analyze_frame,text=f"Protein: {list.totalProtein():.1f} g",text_color="black",anchor=W,justify=LEFT,font=("Arial", 16))
            totalProtein.pack(anchor=W,pady=(10,0),padx=10)
            totalFat=CTkLabel(analyze_frame,text=f"Fat: {list.totalFat():.1f} g",text_color="black",anchor=W,justify=LEFT,font=("Arial", 16))
            totalFat.pack(anchor=W,pady=(10,0),padx=10)
        
            if self.p.getWeight()>self.p.getTarget():
                result=CTkLabel(analyze_frame,text=f"You need to eat {list.totalCalories()-500:.1f} calories a day to lose 0.5kg\nper week",text_color="black",anchor=W,justify=LEFT,font=("Arial", 16))
                result.pack(anchor=W,pady=(15,0),padx=10)
            
            elif self.p.getWeight()<self.p.getTarget():
                result=CTkLabel(analyze_frame,text=f"You need to eat {list.totalCalories()+500:.1f} calories a day to gain 0.5kg\nper week",text_color="black",anchor=W,justify=LEFT,font=("Arial", 16))
                result.pack(anchor=W,pady=(15,0),padx=10)
            
            else:
                result=CTkLabel(analyze_frame,text="You are on the right track!",text_color="black",anchor=W,justify=LEFT,font=("Arial", 16))
                result.pack(anchor=W,pady=(15,0),padx=10)
     
            bmi= CTkLabel(bmi_frame,text="BMI",text_color="#2560be",anchor=N,justify=CENTER,font=("Arial Bold", 24))
            bmi.pack(anchor=N,pady=(20,0))
        
            bmi_label=CTkLabel(bmi_frame,text=f"Your BMI: {self.p.getBMI():.1f}",text_color="black",anchor=W,justify=LEFT,font=("Arial", 18))
            bmi_label.pack(anchor=W,pady=(20,0),padx=10)
        
            if self.p.getBMI()<18.5:
                bmi_result=CTkLabel(bmi_frame,text="You are underweight !",text_color="black",anchor=W,justify=LEFT,font=("Arial", 18))
                bmi_result.pack(anchor=W,pady=(15,0),padx=10)
            
            elif self.p.getBMI()>=18.5 and self.p.getBMI()<24.9:
                bmi_result=CTkLabel(bmi_frame,text="You are normal !",text_color="black",anchor=W,justify=LEFT,font=("Arial", 18))
                bmi_result.pack(anchor=W,pady=(15,0),padx=10)
            
            elif self.p.getBMI()>=24.9 and self.p.getBMI()<29.9:
                bmi_result=CTkLabel(bmi_frame,text="You are overweight !",text_color="black",anchor=W,justify=LEFT,font=("Arial", 18))
                bmi_result.pack(anchor=W,pady=(15,0),padx=10)
            
            else:
                bmi_result=CTkLabel(bmi_frame,text="You are obese !",text_color="black",anchor=W,justify=LEFT,font=("Arial", 18))
                bmi_result.pack(anchor=W,pady=(15,0),padx=10)
            
            help_button=CTkButton(bmi_frame,text="Help",height=50,width=50,fg_color="#2560be",hover_color="blue",font=("Arial Bold", 16),text_color="white",corner_radius=50,command=self.Help)
            help_button.pack(anchor=N,pady=30)

a=App(root)
root.mainloop()