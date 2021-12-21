from netmiko import ConnectHandler
from dotenv import load_dotenv
import os


class Switch():

    sw_config = {
            'device_type': 'cisco_ios',
            'host':   '',
            'username': 'tsmtbs07',
            'password': '',
        }

    sw_handler = None


    def __init__(self,host='192.168.10.165'):
        load_dotenv()
        self.sw_config['host'] = host
        self.sw_config['password'] = os.getenv("SW_PASSWORD")


    def Close(self):

        return True


    def Connect(self):
        self.sw_handler = ConnectHandler(**self.sw_config)    
        return self.sw_handler


    def GetInterfaces(self):
        if not self.sw_handler:
            self.Connect()
        
        return self.sw_handler.send_command('show ip int brief')

    def ShutInterface(self,interface=None):
        if not interface:
            return False

        if not self.sw_handler:
            self.Connect()

        int_str = 'interface %s' % interface
        commands = [int_str,
                    'shutdown']
        
        return self.sw_handler.send_config_set(commands)

    
    def NoShutInterface(self,interface=None):
        if not interface:
            return False

        if not self.sw_handler:
            self.Connect()

        int_str = 'interface %s' % interface
        commands = [int_str,
                    'no shutdown']
        
        return self.sw_handler.send_config_set(commands)    
