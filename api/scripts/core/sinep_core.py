import subprocess


class SinepCore:
    def init_actions(self, actions):
        if 'reciclagem' in actions:
            self.sinep_reciclagem()
        else:
            print('Action não cadastrada.')

    @staticmethod
    def sinep_reciclagem():
        subprocess.call(['sh', 'api/scripts/bash/SIOPI_Reciclagem v1.1.sh'])

    def sinep_status(self):
        subprocess.call(['sh', 'api/scripts/bash/SINEP_Status v1.sh'])
