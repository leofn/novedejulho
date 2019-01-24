import os
import requests as req

from ndj_toolbox.fetch import (xml_df, save_files)

url = 'https://www.al.sp.gov.br/repositorioDados/administracao/funcionarios_cargos.xml'
arquivo = 'servidores_cargos'
data_dir = 'data'


def create_dir():
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)


def process_request():
    xml_data = req.get(url).content
    dataset = xml_df(xml_data).process_data()
    dataset = dataset[['NomeFuncionario', 'NomeCargo', 'IdCargo',
                       'NomeRegime', 'IdRegime', 'DataInicio',
                       'DataFim']]
    dataset = dataset.rename(columns={
        'NomeFuncionario': 'nm_funcionario', 'NomeCargo': 'nm_cargo',
        'IdCargo': 'id_cargo', 'NomeRegime': 'nm_regime',
        'IdRegime': 'id_regime', 'DataInicio': 'dt_inicio',
        'DataFim': 'dt_fim'
    })
    save_files(dataset, data_dir, arquivo)


if __name__ == '__main__':
    create_dir()
    process_request()
