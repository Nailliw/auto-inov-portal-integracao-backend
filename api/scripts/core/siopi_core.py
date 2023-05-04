import subprocess


class SiopiCore:
    def init_actions(self, actions):
        if 'reciclagem' in actions:
            self.siopi_reciclagem()
        else:
            print('Action não cadastrada.')

    @staticmethod
    def siopi_reciclagem():
        subprocess.call(['sh', 'api/scripts/bash/SIOPI_Reciclagem v1.1.sh'])

    def siopi_status(self):
        subprocess.call(['sh', 'api/scripts/bash/SIOPI_Status v1.sh'])
