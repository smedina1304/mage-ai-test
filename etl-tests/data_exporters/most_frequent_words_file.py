from mage_ai.io.file import FileIO
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_most_frequent_words_to_file(df: DataFrame, **kwargs) -> None:
    """
    Exporting data most frequent words to filesystem.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    logger = kwargs.get('logger')

    dir_path = kwargs['data_storage_path']
    dir_path = f'{dir_path}/TopStories'    
    
    filepath = f'{dir_path}/most_frequent_words.csv'

    logger.info(f"Output CSV file: {filepath}")

    FileIO().export(df, filepath)
