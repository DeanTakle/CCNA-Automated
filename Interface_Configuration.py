import netmiko
from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.1',
    'username': '',
    'password': ''
}

SW1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.2',
    'username': '',
    'password': ''
}

SW2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.2.2',
    'username': '',
    'password': ''
}

devices = [R1, SW1, SW2]

def Hostname():
    for device in devices:
        try:
            connection = ConnectHandler(**device)
            hostname = [f'hostname {device}']
            connection.send_command(hostname)
            running_config = connection.send_command('sh run | sec hostname')
            print(f'Hostname is: {running_config}')
            connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')

def Conifg_Ints():
    for device in devices:
        try:
            if device['name'] == 'R1':
                connection = ConnectHandler(**device)
                int_g00 = ['int g0/0', 'ip add 172.16.255.254 255.255.0.0' 'no shut']
                connection.send_command(int_g00)
                running_config = connection.send_command('sh run | sec g0/0')
                print(f'This is the newly configured int: {running_config}')
                connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')

def Speed_and_Duplex():
    for device in devices:
        try:
            if device['name'] == 'R1':
                connection = ConnectHandler(**device)
                int_g00 = ['int g0/0', 'speed full', 'duplex full', 'no shut']
                connection.send_command(int_g00)
                running_config = connection.send_command('sh run | sec g0/0')
                print(f'This is the newly configured int: {running_config}')
                connection.disconnect()
            elif device['name'] == 'SW1':
                connection = ConnectHandler(**device)
                int_g01 = ['int g0/1', 'speed full', 'duplex full', 'no shut']
                int_g02 = ['int g0/2', 'speed full', 'duplex full', 'no shut']
                connection.send_command(int_g01, int_g02)
                running_config = connection.send_command('sh run | sec g0/1', 'sh run | sec g0/2')
                print(f'This is the newly configured int: {running_config}')
                connection.disconnect()
            elif device['name'] == 'SW1':
                connection = ConnectHandler(**device)
                int_g01 = ['int g0/1', 'speed full', 'duplex full', 'no shut']
                connection.send_command(int_g01)
                running_config = connection.send_command('sh run | sec g0/1')
                print(f'This is the newly configured int: {running_config}')
                connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')

def Config_Desc():
    for device in devices:
        try:
            if device['name'] == 'R1':
                connection = ConnectHandler(**device)
                int_g00 = ['int g0/0', 'desc link to SW1', 'no shut']
                connection.send_command(int_g00)
                running_config = connection.send_command('sh run | sec g0/0')
                print(f'This is the newly configured int: {running_config}')
                connection.disconnect()
            elif device['name'] == 'SW1':
                connection = ConnectHandler(**device)
                int_g01 = ['int g0/1', 'desc link to R1', 'no shut']
                int_g02 = ['int g0/2', 'desc link to SW2', 'no shut']
                connection.send_command(int_g01, int_g02)
                running_config = connection.send_command('sh run | sec g0/1', 'sh run | sec g0/2')
                print(f'This is the newly configured int: {running_config}')
                connection.disconnect()
            elif device['name'] == 'SW1':
                connection = ConnectHandler(**device)
                int_g01 = ['int g0/1', 'desc link to SW1', 'no shut']
                connection.send_command(int_g01)
                running_config = connection.send_command('sh run | sec g0/1')
                print(f'This is the newly configured int: {running_config}')
                connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')
    
def Disable_Ints():
    for device in devices:
        try:
            if device['name'] == 'R1':
                connection = ConnectHandler(**device)
                disable_ints = ['int range g0/1 - 2','shut']
                connection.send_command(disable_ints)
                ip_int_brief_config = connection.send_command('sh ip int br')
                print(f'This is the newly configured ints: {ip_int_brief_config}')
                connection.disconnect()
            elif device['name'] == 'SW1':
                connection = ConnectHandler(**device)
                disable_ints = ['int range f0/3 - 24', 'shut']
                connection.send_command(disable_ints)
                ip_int_brief_config = connection.send_command('sh ip int br')
                print(f'This is the newly configured int: {ip_int_brief_config}')
                connection.disconnect()
            elif device['name'] == 'SW1':
                connection = ConnectHandler(**device)
                disable_ints = ['int range f0/3 - 24, g0/2', 'shut']
                connection.send_command(disable_ints)
                ip_int_brief_config = connection.send_command('sh ip int br')
                print(f'This is the newly configured int: {ip_int_brief_config}')
                connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')

Hostname()
Config_Desc()
Speed_and_Duplex()
Conifg_Ints()
Disable_Ints()
