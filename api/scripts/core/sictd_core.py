import subprocess


class SictdCore:
    def init_actions(self, actions):
        if 'reciclagem' in actions:
            self.sictd_reciclagem()
        else:
            print('Action não cadastrada.')

    @staticmethod
    def sictd_reciclagem():
        subprocess.call(['sh', 'api/scripts/bash/SICTD-Reciclagem v1.2.sh'])

    def sictd_status(self):
        subprocess.call(['sh', 'api/scripts/bash/SICTD-Status v1.sh'])
