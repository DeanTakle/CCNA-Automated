import netmiko
from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.1',
    'username': '',
    'password': ''
}

devices = [R1]

def Hostname():
    try:
        for device in devices:
            connection = ConnectHandler(**device)
            hostname = [f'hostname {device}']
            connection.send_command(hostname)
            print(f'Device will be named {hostname}')
            connection.disconnect()       
    except Exception as e:
        print(f'Error occured {e} when connectig to: {device['ip']}')

def Config_Ints():
    try:
        for device in device:
            connection = ConnectHandler(**device)
            int_g0 = ['int g0/0', 'ip add 15.255.255.254 255.0.0.0', 'no shut']
            int_g1 = ['int g0/1', 'ip add 182.98.255.254 255.255.0.0', 'no shut']
            int_g2 = ['int g0/2', 'ip add 201.191.20.254 255.255.255.0', 'no shut']
            connection.send_command(int_g0, int_g1, int_g2)
            connection.disconnect() 
    except Exception as e:
        print(f'Error occured {e} when connectig to: {device['ip']}')

def Config_Int_Desc():
    try:
        for device in devices:
            connection = ConnectHandler(**device)
            desc_g0 = ['int g0/0', 'desc link to SW1']
            desc_g1 = ['int g0/1', 'desc link to SW2']
            desc_g2 = ['int g0/2', 'desc link to SW3']
            connection.send_command(desc_g0, desc_g1, desc_g2)
            connection.disconnect() 
    except Exception as e:
        print(f'Error occured {e} when connectig to: {device['ip']}')

Hostname()
Config_Ints()
Config_Int_Desc()
