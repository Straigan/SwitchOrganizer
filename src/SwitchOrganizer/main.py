from tkinter import Button, END, Entry, Label, scrolledtext, Tk, ttk

from SwitchOrganizer.switches.switches import connection_and_upload_conf_to_switch


def run_app():
    window = Tk()
    
    window.title('SwitchOrganizer')
    window.geometry("930x1000")
    
    # Выбор модели коммутатора для настройки
    model_switch_lbl = Label(text='Модель коммутатора', font='10')
    model_switch_lbl.place(x=300, y=10)
    
    model_switch_list = ['SNR', 'CISCO', 'ELTEX']
    model_switch_combobox = ttk.Combobox(values=model_switch_list, width=33)
    model_switch_combobox.place(x=300, y=58)
    
    # Ввод логина для подключения к коммутатору
    vvod_login_lbl = Label(text='Логин', font='10')
    vvod_login_lbl.place(x=20, y=10)
    
    vvod_login_ent = Entry()
    vvod_login_ent.place(x=100, y=18)
    
    # Ввод пароля для подключения к коммутатору
    vvod_pass_lbl = Label(text='Пароль', font='10')
    vvod_pass_lbl.place(x=20, y=50)
    
    vvod_pass_ent = Entry(show='*')
    vvod_pass_ent.place(x=100, y=58)
    
    # Поле ввода IP адресов коммутаторов
    vvod_ip_lbl = Label(text='IP адреса', font='10')
    vvod_ip_lbl.place(x=160, y=150)
    
    vvod_ip_ent = scrolledtext.ScrolledText(height=20, width=50)
    vvod_ip_ent.place(x=20, y=200)
    
    # Поле ввода комманд для коммутаторов
    vvod_comand_lbl = Label(text='Комманды для коммутаторов', font='10')
    vvod_comand_lbl.place(x=560, y=150)
    
    vvod_comand_ent = scrolledtext.ScrolledText(height=20, width=50)
    vvod_comand_ent.place(x=500, y=200)
    
    # Кнопка применения комманд для выбранных коммутаторов по IP адресам
    
    con_up_sw = lambda: connection_and_upload_conf_to_switch(
                            ip_address_switch=vvod_ip_ent.get("1.0", END), 
                            username=vvod_login_ent.get(), 
                            password=vvod_pass_ent.get(), 
                            commands_to_switch=vvod_comand_ent.get("1.0", END)
                            )
    
    calc_btn = Button(text='RUN', bg='green',command=(con_up_sw))

    calc_btn.place(x=405, y=550, relwidth=0.1, relheight=0.04)
    
    result_ent = scrolledtext.ScrolledText(height=20, width=110)
    result_ent.place(x=20, y=600)

    window.mainloop()


if __name__ == '__main__':
    run_app()