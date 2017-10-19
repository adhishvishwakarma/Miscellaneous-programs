"""
Check health status of multiple servers
This code will read the line by line server names from the input file 
    and update the status in the output-<datetime> file inside output folder.

This code will work even if you are using windows system and your server is in Linux.
"""

import datetime
import os
import paramiko
import sys


username = '<Username>'
password = '<password>'

filename = '<filename with relative/absolute path>'

output_folder = os.path.join(os.path.dirname(filename), 'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

today = datetime.datetime.now()
format_date = today.strftime("%Y%m%d %I%M%S")
output_file = os.path.join(output_folder, 'output-%s.txt' % format_date)


def ssh_connection(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=username, password=password)
        """If you need to run any command after connecting server,
        please uncomment next three lines"""
        # stdin, stdout, stderr = ssh.exec_command("<Your Command>")
        # for line in stdout.readlines():
        #     print line.strip()
        return "connected"
        ssh.close()
    except paramiko.AuthenticationException:
        return "Authentication Failed"
        # quit()
    except:
        return "Unknown error"
        # quit()


def check_all_servers():
    x = open(filename, 'r')
    y = x.readlines()
    w = open(output_file,  'w+')
    for host in y:
        w.write("%s : %s \n" % (host, ssh_connection(host)))
        # print host, ssh_connection(host)


if len(sys.argv) == 1:
    print sys.argv
    check_all_servers()
else:
    z = open(output_file, 'w+')
    z.write("%s : %s \n" % (sys.argv[1], ssh_connection(sys.argv[1])))
