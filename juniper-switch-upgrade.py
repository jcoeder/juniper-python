import paramiko
import jnpr.junos
import getpass
import pprint
import time


switch = input('Switch: ')
username = input('Username: ')
password = getpass.getpass(prompt='Password: ')

def is_root():
    if username == 'root':
        remote_conn.send('cli\n')
        time.sleep(2)
    else:
        pass

try:
    with jnpr.junos.Device(host=switch, user=username, password=password) as device:
        pprint.pprint(device.facts)
except:
    print('Unable to connect to the Netconf Service.')
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(switch, username=username, password=password, look_for_keys=False, allow_agent=False)
    
    remote_conn = remote_conn_pre.invoke_shell()
   
    is_root()

    remote_conn.send('configure\n') 
    time.sleep(2)
    output = remote_conn.recv(1000)
    print(output.decode())

    remote_conn.send('set system service netconf ssh\n')
    time.sleep(1)
    output = remote_conn.recv(1000)
    print(output.decode())

    remote_conn.send('commit\n')
    time.sleep(3)
    output = remote_conn.recv(1000)
    print(output.decode())

    remote_conn.send('exit\n')
    time.sleep(1)
    output = remote_conn.recv(1000)
    print(output.decode())

    remote_conn.send('exit\n')
    time.sleep(1)
    output = remote_conn.recv(1000)
    print(output.decode())

    remote_conn.send('exit\n')
    time.sleep(1)
    output = remote_conn.recv(1000)
    print(output.decode())
