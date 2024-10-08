from netmiko import ConnectHandler, exceptions
from tkinter import INSERT


# Connecting and sending commands to the switch
def connection_and_upload_conf_to_switch(result_ent, ip_address_switch: str, username: str, password: str, commands_to_switch: str) -> str:
    
    result_ent.configure(state='normal')
    for ip_addres_switch in filter(None, ip_address_switch.split('\n')):
        snr_switch_param = {
            'device_type': 'cisco_ios',
            'host': ip_addres_switch,
            'username': username,
            'password': password,
            'port': 22,
        }
        try:
            net_connect = ConnectHandler(**snr_switch_param)
        except exceptions.NetmikoTimeoutException:
            message = f"{ip_addres_switch} ===== веден не корректный IP адрес устройства или устройство не доступно\n"
            result_ent.insert(INSERT, message)
            continue
        except exceptions.NetmikoAuthenticationException:
            message = f"{ip_addres_switch} ===== введены не корретные логин и пароль\n"
            result_ent.insert(INSERT, message)
            continue
        net_connect.enable()
        
        for command in commands_to_switch.split('\n'):
            net_connect.send_command_timing(command)
        
        net_connect.disconnect()

        message = f"{ip_addres_switch} ======= ОК\n"
        result_ent.insert(INSERT, message)

    result_ent.configure(state='disabled')