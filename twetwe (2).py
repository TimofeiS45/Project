import tkinter as tk
from tkinter import ttk
from MyDb import Data_Base 
from tkinter import *
from tkinter import messagebox
from MyDb import Data_Base




def table(heads, request):

    entry_widgets = {}

    win_table = tk.Toplevel()
    win_table.geometry('1000x700')
    
    frame_text = tk.Frame(win_table, height=0)
    frame_text.pack(fill="both", expand=True)

    canvas = tk.Canvas(win_table, bg='#242424')
    canvas.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(canvas, command=canvas.yview)
    scrollbar.pack(side="right", fill='y')
    
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.configure(yscrollcommand=scrollbar.set)
    


    request = Data_Base.request_data(request=request)
    rows = len(request)
    cols = len(request[0]) if request else 0
    


    for j, header in enumerate(heads):
        label = tk.Label(frame, text=header.upper(), width=15, font=("Arial", 10, "bold"))
        label.grid(row=0, column=j, padx=5, pady=5)

    for i in range(rows):

        for j in range(cols):
            
            label = tk.Label(frame, text=str(request[i][j]), width=15)
            label.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")  
            # if i < rows - 1:
            #     line_frame = tk.Frame(frame, height=3, bg='black')
            #     line_frame.grid(row=i*2+2, column=0, columnspan = cols, rowspan=1, sticky = 'ew' )
    


    for j, header in enumerate(heads):
            entry = tk.Entry(frame_text)
            entry.grid(row=rows*2+1, column=j, padx=5, pady=5)
            entry_widgets[header] = entry  # Store entry widgets in the dictionary

        # Add a save button below the entry fields
    button_save = tk.Button(frame_text, text='Сохранить', command=lambda: text_box_save(entry_widgets))
    button_save.grid(row=rows*2+2, column=0, columnspan=cols, pady=10)

def text_box_save(entry_widgets):
    # Retrieve values from entry widgets
    entry_values = {header: entry.get() for header, entry in entry_widgets.items()}
    print('entry_val: ', entry_values)
    # Generate SQL query based on entry values
    columns = ", ".join(entry_values.keys())
    values = ", ".join([f"'{value}'" for value in entry_values.values()])
    print('Col: ', columns )
    print('val: ', values)
    request = f"INSERT INTO table_name ({columns}) VALUES ({values})"

    # Execute SQL query
    Data_Base.change_data(request)

        




   
def abitur_op():
    heads = ['id', 'office', 'sys_id', 'cpu_id', 'ram_id', 'disk_id', 'net_id', 'count_disk', 'count_net'] 
    request = 'select * from pc'
    table(heads, request)
  

  


def spravka():
        messagebox.showinfo(title='Справка', message='''
       Aboba
        ''')
       


def click():
    username = username_entry.get()
    password = password_entry.get()

    if username == '1' and password == '1':
        
        main_window = tk.Toplevel(root)
        main_window.title("Главное окно")
        main_window.geometry('600x350')
        main_window.resizable(width=False, height=False)
        main_window['bg'] = 'blue'


        btn = tk.Button(main_window, text="Абитуриенты", command=abitur_op, width=15, height=2)
        btn.grid(row=0, column=0)
        btn = tk.Button(main_window, text="Специальности", command=main_window.destroy, width=15, height=2)
        btn.grid(row=0, column=1)
        btn = tk.Button(main_window, text="Экзамены", command=main_window.destroy, width=15, height=2)
        btn.grid(row=0, column=2)
        btn = tk.Button(main_window, text="Итоги экзаменов", command=main_window.destroy, width=15, height=2)
        btn.grid(row=0, column=3)
        btn = tk.Button(main_window, text="Справка", command=spravka, width=10, height=2)
        btn.grid(row=0, column=7)
        root.withdraw()
        
    else:
        messagebox.showerror('Ошибка авторизации', 'Неверное имя пользователя или пароль.')




root = Tk()
root.title('Учет данных абитуриентов')
root.geometry('600x350')
root.resizable(width=False, height=False)
root['bg'] = 'blue'



main_label = Label(root, text='Авторизация', font='Ariel 15', bg='blue', fg='white')
main_label.pack()

username_label = Label(root, text='Имя пользователя:', font='Ariel 11', bg='blue', fg='white', padx=10, pady=8)
username_label.pack()

username_entry = Entry(root, bg='white', fg='black', font = 'Ariel 11')
username_entry.pack()

password_label = Label(root, text='Пароль:', font='Ariel 11', bg='blue', fg='white', padx=10, pady=8)
password_label.pack()

password_entry = Entry(root, bg='white', fg='black', font = 'Ariel 11')
password_entry.pack()

send_btn = Button(root, text='Войти', command=click)
send_btn.pack(padx=10, pady=8)




root.mainloop()