from netmiko import ConnectHandler, exceptions

# Connecting and sending commands to the switch
def connection_and_upload_conf_to_switch(ip_address_switch: str, username: str, password: str, commands_to_switch: str) -> str:

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
            print(f"{ip_addres_switch} Введен не корректный IP адрес устройства или устройство не доступно")
            continue
        except exceptions.NetmikoAuthenticationException:
            print(f"{ip_addres_switch} Введены не корретные логин и пароль")
            break
        net_connect.enable()
        
        for command in commands_to_switch.split('\n'):
            net_connect.send_command_timing(command)
    
        net_connect.disconnect()

        print(f"{ip_addres_switch} ======= ОК")
