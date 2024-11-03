import customtkinter as ctk
from PIL import Image, ImageTk
import customtkinter as ctk
from pandastable import Table
import pandas as pd
from tkinter import IntVar
from datetime import datetime
from test import PDFGenerator
# نص ثابت
x = '''جمهورية العراق 
هيئة النزاهة الاتحادية 
دائرة التحقيقات 
مديرية تحقيق البصرة'''

pdf_generator = PDFGenerator(config_path=r'C:\Users\rf\Desktop\wkhtmltopdf\bin\wkhtmltopdf.exe')


# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def create_responsive_gui():
    # Create the main window
    root = ctk.CTk()
    root.title("Responsive CustomTkinter GUI") 

    y = IntVar()
    input_fields = {}

    def exit_fullscreen(event):
        root.attributes('-fullscreen', False)

    root.bind("<Escape>", exit_fullscreen)  # Exit fullscreen on Escape key

    tab_frame = ctk.CTkFrame(root)
    tab_frame.pack(side="left", fill="y", padx=20, pady=20)

    main_frame = ctk.CTkFrame(root, fg_color="#1D3C6B")
    main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
    

    def mack_data_frame():
        df = pd.read_csv('saved_data.csv')
        data_frame = ctk.CTkFrame(main_frame, fg_color="#1D3C6B")
        data_frame.grid(fill=ctk.BOTH, expand=True, padx=20, pady=20)
        tabel = Table(data_frame, dataframe=df) 
        tabel.show()
        

    def show_tab(tab_name):
        for widget in main_frame.winfo_children():
            widget.destroy()  # Clear previous content

        if tab_name == "الاستعلامات":
            inquiries()

        elif tab_name == "البيانات":
            inquiries()
            bot_comand()
        elif tab_name == "التعديل":
            edit()

    def inquiries():
        # Create a sub frame for inquiries
        sub_frame()

        # Create a frame for the inquiries section
        inquiry_frame = ctk.CTkFrame(main_frame, fg_color="#44689D", corner_radius=30)
        inquiry_frame.grid(row=1, column=0, columnspan=3, padx=55, pady=15)

        label2 = ctk.CTkLabel(inquiry_frame, text="الأستعلامات",
                               text_color="#ffffff", width=300, height=70, font=("Arial", 36, "bold"))
        label2.pack(padx=80, pady=15)

        # Create input fields
        create_input_field("الأسم", 'img/الأسم.png', 2, 1)
        create_input_field("الوظيفة", 'img/الوضيفه.png', 2, 0)
        create_input_field("رقم الهوية", 'img/الرقم.png', 3, 1)
        create_input_field("تاريخ وجهة الاصدار", 'img/الرقم.png', 3, 0)
        create_input_field("صفة المراجعة", 'img/صفه.png', 4, 0, colspan=3)
        create_input_field("جهة المراجعة", 'img/جهة.png', 5, 0, colspan=3)

        # Submit Button
        create_button("img/SUBMET.png", "", 6, 0, save_data)
        # Finish Button
        # create_button("img/noun-7211434-FFFFFF.png", "", 6, 1)

        # Configure grid weights for responsive resizing
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Configure sub_frame grid weights








    def edit():
        sub_frame()
        
        inquiry_frame = ctk.CTkFrame(main_frame, fg_color="#44689D", corner_radius=30)
        inquiry_frame.grid(row=1, column=0, columnspan=3, padx=55, pady=15)

        label2 = ctk.CTkLabel(inquiry_frame, text="التعديل",
                               text_color="#ffffff", width=300, height=70, font=("Arial", 36, "bold"))
        label2.pack(padx=80, pady=15)

        radio(master=main_frame, text='الأسم', hover_color='white', variable=y, value=0, pady=10, row=2, column=1, padx=68)
        radio(master=main_frame, text='رقم الهوية', hover_color='white', variable=y, value=1, pady=10, row=2, column=0, padx=0)

        create_input_field('البحث','img/الأسم.PNG',4,0,3,)

        icon = ImageTk.PhotoImage(Image.open('img/SUBMET.png'))
        button = ctk.CTkButton(master=main_frame, width=227, height=64, corner_radius=30, fg_color="#44689D", image=icon, compound="left", text='',command=bot_comand_edit)
        button.grid(row=7, column=1, columnspan=3, padx=68, pady=27.5, sticky="ew")
        

        icon = ImageTk.PhotoImage(Image.open('img/الطبع.png'))
        button = ctk.CTkButton(master=main_frame, width=227, height=64, corner_radius=30, fg_color="#44689D", image=icon, compound="left", text='',command=printing)
        button.grid(row=8, column=1, columnspan=3, padx=68, pady=27.5, sticky="ew")


        icon = ImageTk.PhotoImage(Image.open('img/الحذف.png'))
        button = ctk.CTkButton(master=main_frame, width=227, height=64, corner_radius=30, fg_color="#44689D", image=icon, compound="left", text='',command=delet)
        button.grid(row=9, column=1, columnspan=3, padx=68, pady=27.5, sticky="ew")



    
    def radio(master,text,value,row,column, hover_color, variable, pady, padx, columnspan=1):
        radio_btn1 = ctk.CTkRadioButton(master=master , text=text, hover_color=hover_color, variable=variable, value=value, command=rad_bot_comand)
        radio_btn1.grid(pady=pady, padx=padx, row=row, column=column, columnspan=columnspan)

        


    def sub_frame():

        sub_frame = ctk.CTkFrame(main_frame, fg_color="#FFFFFF", height=125, corner_radius=20)
        sub_frame.grid(row=0, column=0, columnspan=30, padx=15, pady=10, sticky="nsew")

        # Load and display images
        img1 = Image.open("img/شعار النزاهة.jpg").resize((120, 90), Image.LANCZOS)
        img1_tk = ImageTk.PhotoImage(img1)
        img_label1 = ctk.CTkLabel(sub_frame, image=img1_tk, text='')
        img_label1.grid(row=0, column=2, padx=5, pady=10)

        img_label1.image = img1_tk  # Keep reference to avoid garbage collection
        img2 = Image.open("img/الشعار.png").resize((120, 120), Image.LANCZOS)
        img2_tk = ImageTk.PhotoImage(img2)
        img_label2 = ctk.CTkLabel(sub_frame, image=img2_tk, text='')
        img_label2.grid(row=0, column=0, padx=5, pady=10)

        img_label2.image = img2_tk  # Keep reference to avoid garbage collection
        label = ctk.CTkLabel(sub_frame, text=x, text_color="black", font=("Arial", 20, "bold"), justify="right")
        label.grid(row=0, column=1, padx=5, pady=5)

        sub_frame.grid_columnconfigure(0, weight=0)
        sub_frame.grid_columnconfigure(1, weight=1)
        sub_frame.grid_columnconfigure(2, weight=0)



    def create_input_field(label_text, icon_path, row, column, colspan=1):
           # Create input field with icon
           icon = ImageTk.PhotoImage(Image.open(icon_path))
           frame = ctk.CTkFrame(master=main_frame, height=40, corner_radius=10, fg_color='#44689D')
           frame.grid(row=row, column=column, columnspan=colspan, padx=68, pady=55/2, sticky="ew")

           label = ctk.CTkLabel(master=frame, text=label_text, bg_color="#44689D", width=120, image=icon, compound="right", font=("Arial", 20, "bold"))
           label.pack(padx=10, side="right")

           entry = ctk.CTkEntry(
               master=frame,
               fg_color='#ffffff',
               bg_color='white',
               border_color='#ffffff',
               width=380,
               height=40,
               text_color="black",
               font=("Arial", 16),
               justify="right"
           )
           entry.pack(fill=ctk.X, expand=True)
           input_fields[label_text] = entry

    def create_button(icon_path, button_text, row, column, command):
        # Create button with icon
        icon = ImageTk.PhotoImage(Image.open(icon_path))
        button = ctk.CTkButton(master=main_frame, width=227, height=64, corner_radius=30, fg_color="#44689D", image=icon, compound="left", text=button_text, command=command)
        button.grid(row=row, column=column, columnspan=1, padx=68, pady=27.5, sticky="ew")



    def printing():
        search_value = input_fields['البحث'].get()
        search_type = y.get()  # الحصول على نوع البحث
        df = pd.read_csv('saved_data.csv')
        df['رقم الهوية'] = pd.to_numeric(df['رقم الهوية'], errors='coerce')  # تحويل عمود رقم الهوية إلى أعداد صحيحة
    
        # البحث بناءً على نوع البحث
        if search_type == 0:
            results = df[df['الأسم'].str.contains(search_value, na=False)]
        elif search_type == 1:
            search_value = int(search_value)
            results = df[df['رقم الهوية'] == search_value]
    
        if len(results) == 1:
            row = results.iloc[0]
            pdf_generator.generate_pdf('reviewer_data.pdf', row, open_pdf=True)
            edit()
        elif len(results) > 1:
            top = ctk.CTkToplevel()
            top.title('Error')
            top.attributes('-topmost', True)
            top.geometry("500x200")
            text = ctk.CTkLabel(master=top, text='اكتب الأسم الكامل', font=("Arial", 50))
            text.pack(padx=10, pady=10, expand=True)
        else:
            top = ctk.CTkToplevel()
            top.title('Error')
            top.attributes('-topmost', True)
            top.geometry("500x200")
            text = ctk.CTkLabel(master=top, text='لا توجد نتائج لهذا اللأسم', font=("Arial", 50))
            text.pack(padx=10, pady=10, expand=True)
    
            edit()

    def delet():
        # الحصول على القيمة المراد البحث عنها من حقل الإدخال
        search_value = input_fields['البحث'].get()
        search_type = y.get()

        # قراءة البيانات من ملف CSV
        df = pd.read_csv('saved_data.csv')
        df['رقم الهوية'] = pd.to_numeric(df['رقم الهوية'], errors='coerce')

        # البحث عن الصفوف التي تحتوي على القيمة المراد حذفها
        # وتصفية DataFrame بحيث لا يحتوي على الصفوف التي تطابق القيمة
        if search_type == 0:
            df = df[df['الأسم'] != search_value]
            df.to_csv('saved_data.csv', index=False)

        elif search_type == 1:
            search_value = int(search_value)
            df = df[df['رقم الهوية'] != search_value]
            df.to_csv('saved_data.csv', index=False)

        # إعادة كتابة الملف بدون الصفوف التي تم حذفها
        

        edit()

    def rad_bot_comand():
        print(y.get)





    def create_input_field_to_edit(label_text, icon_path, row, column, valio,  colspan=1):
        # Create input field with icon
        icon = ImageTk.PhotoImage(Image.open(icon_path))
        frame = ctk.CTkFrame(master=main_frame, height=40, corner_radius=10, fg_color='#44689D')
        frame.grid(row=row, column=column, columnspan=colspan, padx=68, pady=55/2, sticky="ew")
        label = ctk.CTkLabel(master=frame, text=label_text, bg_color="#44689D", width=120, image=icon, compound="right", font=("Arial", 20, "bold"))
        label.pack(padx=10, side="right")
        entry = ctk.CTkEntry(
            master=frame,
            fg_color='#ffffff',
            bg_color='white',
            border_color='#ffffff',
            width=380,
            height=40,
            text_color="black",
            font=("Arial", 16),
            justify="right",
        )
        entry.insert(0, valio)
        entry.pack(fill=ctk.X, expand=True)
        input_fields[label_text] = entry
    
    
    def bot_comand_edit():
        search_value = input_fields['البحث'].get()  # الحصول على قيمة البحث
        search_type = y.get()
        df = pd.read_csv('saved_data.csv')
        df['رقم الهوية'] = pd.to_numeric(df['رقم الهوية'], errors='coerce')
        
        if search_type == 0: 

            results = df[df['الأسم'].str.contains(search_value, na=False)]

        elif search_type == 1:  # إذا كان الخيار هو رقم الهوية
            search_value = int(search_value)
            results = df[df['رقم الهوية'] == search_value]
            results = results

        if len(results) == 1:
            # استخراج القيم الفردية من السطر
            row = results.iloc[0]
    
            # إنشاء الحقول مع القيم الموجودة
            create_input_field_to_edit("الأسم", 'img/الأسم.png', 3, 1, valio=row['الأسم'])
            create_input_field_to_edit("الوظيفة", 'img/الوضيفه.png', 3, 0, valio=row['الوظيفة'])
            create_input_field_to_edit("رقم الهوية", 'img/الرقم.png', 4, 1, valio=row["رقم الهوية"])
            create_input_field_to_edit("تاريخ وجهة الاصدار", 'img/الرقم.png', 4, 0, valio=row["تاريخ وجهة الاصدار"])
            create_input_field_to_edit("صفة المراجعة", 'img/صفه.png', 5, 0, valio=row["صفة المراجعة"], colspan=3)
            create_input_field_to_edit("جهة المراجعة", 'img/جهة.png', 6, 0, valio=row["جهة المراجعة"], colspan=3)


            
        elif len(results) > 1:
            top = ctk.CTkToplevel()
            top.title('Error')
            top.attributes('-topmost', True)
            top.geometry("500x200")
            text = ctk.CTkLabel(master=top,text='اكتب الأسم الكامل', font=("Arial", 50))
            text.pack(padx = 10, pady = 10, expand=True)
            
        else:
            top = ctk.CTkToplevel()
            top.title('Error')
            top.attributes('-topmost', True)
            top.geometry("500x200")
            text = ctk.CTkLabel(master=top,text='لا توجد نتائج لهذا اللأسم', font=("Arial", 50))
            text.pack(padx = 10, pady = 10, expand=True)

   
    
 

    def save_data():
        data = {label: entry.get() for label, entry in input_fields.items()}
        data["وقت الحفظ"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # تحويل البيانات إلى DataFrame
        df = pd.DataFrame([data])

        # حفظ البيانات في ملف CSV
        df.to_csv("saved_data.csv", mode='a', index=False, header=not pd.io.common.file_exists("saved_data.csv"))

    def data_edits():
            search_value = input_fields['البحث'].get()
            df = pd.read_csv('saved_data.csv')
            results = df[df['الأسم'].str.contains(search_value, na=False)]
            # تحديث البيانات
            for label in input_fields.keys():
                df.at[results.index[0], label] = input_fields[label].get()  # تعديل البيانات

            # حفظ البيانات المحدثة في ملف CSV
            df.to_csv("saved_data.csv", index=False)



    def bot_comand():
        df = pd.read_csv('saved_data.csv')
        global top
        top = ctk.CTkToplevel()
        top.title('Data')
        top.attributes('-topmost', True)
        tabel = Table(top, dataframe=df)   
        tabel.show()


    # Create tab buttons
    tab1_button = ctk.CTkButton(tab_frame, text="الاستعلامات", command=lambda: show_tab("الاستعلامات"))
    tab1_button.pack(pady=10, padx=10)

    tab2_button = ctk.CTkButton(tab_frame, text="التعديل و البحث", command=lambda: show_tab("التعديل"))
    tab2_button.pack(pady=10, padx=10)

    tab3_button = ctk.CTkButton(tab_frame, text="البيانات", command=lambda: show_tab("البيانات"))
    tab3_button.pack(pady=10, padx=10)

    # Show the first tab by default
    show_tab("الاستعلامات")

    # Start the application
    root.mainloop()


if __name__ == '__main__':
    create_responsive_gui()
