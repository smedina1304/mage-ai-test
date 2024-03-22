import os
from mage_ai.io.file import FileIO
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

def dir_check(dir_name, is_create=True):
    """
    Function to check if the directory exists and create it if necessary.
    """
    dir_exists = os.path.isdir(dir_name)

    print(f'dir exists({dir_name}):', dir_exists)
    if (not dir_exists) and (is_create):
        os.makedirs(dir_name)
        print(f'dir created:', dir_name)   


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Export Universities data to file CSV.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    dir_path = kwargs['data_storage_path']
    dir_path = f'{dir_path}/Universities'
    dir_check(dir_name = dir_path)

    file_path = f'{dir_path}/universities_data.csv'
    FileIO().export(data, file_path)



