# -*- coding: UTF-8 -*-
import paramiko
import content

class SSH:
    def __init__(self, **kwargs):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.kwargs = kwargs

    def __enter__(self):

        '''Как написать код для подключения к удаленному хосту с импрортируемым модулем paramiko'''
        kw = self.kwargs
        self.client.connect(hostname=kw.get('hostname'), username=kw.get('username'),
                            password=kw.get('password'), port=int(kw.get('port', 22)))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def exec_cmd(self, cmd):

        ''' Необходимо выполнить команду с помощью скрипта (к прим. ls -al)'''
        stdin, stdout, stderr = self.client.exec_command(cmd)
        data = stdout.read()
        # if stderr:
            # print(stderr)
        return data.decode()


# if __name__ == '__main__':
def parsstat():

    with SSH(hostname='123', username='root', password='456', port=22) as ssh:
        data = []
        for i in content.projectdirs.items():
            out = ssh.exec_cmd('cat cmc/services/{}/{} | grep STATISTIC | tail -n1'.format(i[0], i[1]))
            # print('Project: {}, Stat: {}'.format(i[0], out), file=open('log.log', 'a'))  # и записью вывода в лог
            data.append('Project: {}, Stat: {}'.format(i[0], out))
        return data
