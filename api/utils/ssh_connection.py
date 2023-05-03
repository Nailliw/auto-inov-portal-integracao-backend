import paramiko
from paramiko.client import SSHClient


class SSH:
    def __init__(self, hostname, username, password):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=hostname, username=username, password=password)

    def exec_command(self, _command):
        _stdin, _stdout, _stderr = self.ssh.exec_command(_command)
        if _stderr.channel.recv_exit_status() != 0:
            return _stderr.read()
        else:
            return _stdout.read()

    def exec_list_of_commands(self, commands_list):
        return [self.exec_command(_cmd) for _cmd in commands_list]
