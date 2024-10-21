from tkinter import Button, END, Entry, Label, scrolledtext, Tk, ttk

from settings.settings_app import *
from switches.switches import connection_and_upload_conf_to_switch


class App(Tk): 
    
    def __init__(self):
        super().__init__() 
        # Fied enter login for connect switch
        username_label = Label(text='Логин', font=SIZE_FONT)
        username_label.place(x=USERNAME_LABEL_PLACE_X, y=USERNAME_LABEL_PLACE_Y)
        
        username_input = Entry(font=SIZE_FONT)
        username_input.place(x=USERNAME_INPUT_PLACE_X, y=USERNAME_INPUT_PLACE_Y)
        
        # Filed enter password for connect switch
        password_label = Label(text='Пароль', font=SIZE_FONT)
        password_label.place(x=PASSWORD_LABEL_PLACE_X, y=PASSWORD_LABEL_PLACE_Y)
        
        password_input = Entry(show='*', font=SIZE_FONT)
        password_input.place(x=PASSWORD_INPUT_PLACE_X, y=PASSWORD_INPUT_PLACE_Y)
        
        # Filed enter ip address switch
        ip_switch_label = Label(text='IP адреса', font=SIZE_FONT)
        ip_switch_label.place(x=IP_SWITCH_LABEL_PLACE_X, y=IP_SWITCH_LABEL_PLACE_Y)
        
        ip_switch_input = scrolledtext.ScrolledText(height=SCROLL_TEXT_H, width=SCROLL_TEXT_W, font=SIZE_FONT)
        ip_switch_input.place(x=IP_SWITCH_INPUT_PLACE_X, y=IP_SWITCH_INPUT_PLACE_Y)
        
        # Filed enter command for switch
        comand_to_switch_label = Label(text='Комманды для коммутаторов', font=SIZE_FONT)
        comand_to_switch_label.place(x=COMMAND_TO_SWITCH_LABEL_X, y=COMMAND_TO_SWITCH_LABEL_Y)
        
        command_to_switch_input = scrolledtext.ScrolledText(height=SCROLL_TEXT_H, width=SCROLL_TEXT_W, font=SIZE_FONT)
        command_to_switch_input.place(x=COMMAND_TO_SWITCH_INPUT_X, y=COMMAND_TO_SWITCH_INPUT_Y)
        
        # Filed enter conclusion result
        result_output = scrolledtext.ScrolledText(height=RESULT_SCROLL_TEXT_H, width=RESULT_SCROLL_TEXT_W, font=SIZE_FONT)
        result_output.place(x=RESULT_OUTPUT_PLACE_X, y=RESULT_OUTPUT_PLACE_Y)

        run_script_connection_and_upload_conf_to_switch = lambda result_output=result_output: connection_and_upload_conf_to_switch(
                                username_input=username_input.get(), 
                                password_input=password_input.get(),
                                ip_switch_input=ip_switch_input.get(1.0, END), 
                                command_to_switch_input=command_to_switch_input.get(1.0, END),
                                result_output=result_output
                                )
        
        # Button for connect switch and input commands in switch
        button_run_script_connection_and_upload_conf_to_switch = Button(text='RUN', bg='green',command=(run_script_connection_and_upload_conf_to_switch))
        button_run_script_connection_and_upload_conf_to_switch.place(
                                                                     x=BUTTON_RUN_SCRIPT_PLACE_X, 
                                                                     y=BUTTON_RUN_SCRIPT_PLACE_Y, 
                                                                     relheight=BUTTON_RUN_SCRIPT_RH, 
                                                                     relwidth=BUTTON_RUN_SCRIPT_RW
                                                                     )