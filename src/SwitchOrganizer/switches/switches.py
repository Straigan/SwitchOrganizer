from netmiko import ConnectHandler, exceptions
from tkinter import INSERT


# Connecting and sending commands to the switch
def connection_and_upload_conf_to_switch(username_input: str, password_input: str, ip_switch_input: str, command_to_switch_input: str, result_output: str) -> str:
    
    result_output.configure(state='normal')
    for ip_addres_switch in filter(None, ip_switch_input.split('\n')):
        snr_switch_param = {
            'device_type': 'cisco_ios',
            'host': ip_addres_switch,
            'username': username_input,
            'password': password_input,
            'port': 22,
        }
        try:
            net_connect = ConnectHandler(**snr_switch_param)
        except exceptions.NetmikoTimeoutException:
            message = f"{ip_addres_switch} ===== веден не корректный IP адрес устройства или устройство не доступно\n"
            result_output.insert(INSERT, message)
            continue
        except exceptions.NetmikoAuthenticationException:
            message = f"{ip_addres_switch} ===== введены не корретные логин или пароль\n"
            result_output.insert(INSERT, message)
            continue
        net_connect.enable()
        
        for command in command_to_switch_input.split('\n'):
            net_connect.send_command_timing(command)
        
        net_connect.disconnect()

        message = f"{ip_addres_switch} ======= ОК\n"
        result_output.insert(INSERT, message)

    result_output.configure(state='disabled')