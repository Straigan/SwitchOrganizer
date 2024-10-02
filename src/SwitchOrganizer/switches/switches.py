from netmiko import ConnectHandler


def connection_and_upload_conf_to_switch(ip_address_switch: str, username: str, password: str, commands_to_switch: str) -> None:

    for ip_addres_switch in filter(None, ip_address_switch.split('\n')):
        snr_switch_param = {
            'device_type': 'cisco_ios',
            'host': ip_addres_switch,
            'username': username,
            'password': password,
            'port': 22,
        }
        
        net_connect = ConnectHandler(**snr_switch_param)
        net_connect.enable()
        
        for command in commands_to_switch.split('\n'):
            print(net_connect.send_command_timing(command))
    
        net_connect.disconnect()
    