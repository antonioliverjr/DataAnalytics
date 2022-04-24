import os
from auxilio_emerg_extractzip import extract_csv
from auxilio_emerg_spark import tratamento_csv

def main():
    path_download = 'C:\\Users\\antoliverjr\\Downloads'
    path_historico = 'C:\\Workspace\\DataAnalytics\\Auxilio_Emergencial\\historico_zip'
    path_files = 'C:\\Workspace\\DataAnalytics\\Auxilio_Emergencial\\csv_aux_emergencial'

    try:
        path_file_name = extract_csv('202104', path_download, path_historico, path_files)
        print('Zip Extraído com sucesso')
    except Exception as error:
        print(error)

    if os.path.exists(path_file_name):
        if tratamento_csv(path_file_name, path_files):
            print('Sucesso no processamento')
        else:
            print('Erro processamento CSV')
    else:
        print('Erro processamento CSV')

if __name__ == '__main__':
    main()