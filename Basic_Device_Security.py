import netmiko
from netmiko import ConnectHandler

#1st need to add loopback interfaces with coresponding IPs on all devices being automated.

R1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.1',
    'username': '',
    'password': ''
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.2.1',
    'username': '',
    'password': ''
}

R3 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.3.1',
    'username': '',
    'password': ''
}

S1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.2',
    'username': '',
    'password': ''
}

S2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.2.2',
    'username': '',
    'password': ''
}

devices = [R1, R2, R3, S1, S2]

def Unencrypted_Pass():
    for device in devices:
        try:
            connection = ConnectHandler(**device)
            unencrypted_pass_commands = ['enable password CCNA'] #Defines commands that do not have outputs
            connection.send_command(unencrypted_pass_commands)
            running_config = connection.send_command('sh run | sec pass') #Command that shows only sections with passwrods
            print(f'This is what unecnrypted password looks like in running config: {running_config}')
            connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')

def Password_Encryption():
    for device in devices:
        try:
            connection = ConnectHandler(**device)
            password_encryption_commands = ['service password-encryption'] #Defines commands that do not have outputs
            connection.send_command(password_encryption_commands)
            running_config = connection.send_command('sh run | sec pass')
            print(f'This is what unecnrypted password looks like after "service password-encryption" in running config: {running_config}')
            connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')

def Encrypted_Pass():
    for device in devices:
        try:
            connection = ConnectHandler(**device)
            encrypted_pass_commands = ['enable secret Cisco'] #Defines commands that do not have outputs
            connection.send_command(encrypted_pass_commands)
            running_config = connection.send_command('sh run | sec pass')
            print(f'This is what encrypted password looks like in running config: {running_config}')
            connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')

def Save_Run_To_Start():
    for device in devices:
        try:
            connection = ConnectHandler(**device)
            save_run_to_start = ['Copy run start'] #Defines commands that do not have outputs
            connection.send_command(save_run_to_start)
            startup_config = connection.send_command('sh start')
            print(f'This is what "Satrtup Config" looks like when "Copy Run Start" is used: {startup_config}')
            connection.disconnect()
        except Exception as e:
            print(f'Error Occured {e} when connecting to {device['ip']}')


Unencrypted_Pass()
Password_Encryption()
Encrypted_Pass()
Save_Run_To_Start()