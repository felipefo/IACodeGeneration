import luigi
import subprocess
import logging
logging.getLogger('luigi-interface').setLevel(logging.WARNING)

class GeracaoEntidades(luigi.Task):
    def output(self):
        return luigi.LocalTarget('task_a_output.txt')

    def run(self):
        subprocess.run(['python', 'main.py'], check=True)

class FormatSaida(luigi.Task):
    def requires(self):
        return GeracaoEntidades()
    def output(self):
        return luigi.LocalTarget('task_b_output.txt')
    def run(self):
        subprocess.run(['python', './pos_geracao/processa_saida.py'], check=True)

class ContextDb(luigi.Task):
    def requires(self):
        return FormatSaida()

    def output(self):
        return luigi.LocalTarget('task_c_output.txt')

    def run(self):
        subprocess.run(['python', 'contextdb.py'], check=True)

if __name__ == '__main__':
    luigi.build([GeracaoEntidades()], local_scheduler=True)
