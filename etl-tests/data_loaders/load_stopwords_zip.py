import io
import pandas as pd
import requests

from zipfile import ZipFile
from urllib.request import urlopen

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_stopwords_zip(*args, **kwargs):
    """
    Download the 'stopwords.zip' file.
    Extract the stopword list from the CSV into the ZIP.
    Add other local stopwords to the list.
    """

    logger = kwargs.get('logger')

    # Download of the 'stopwords.zip'
    url = 'https://docs.dagster.io/assets/stopwords.zip'
    logger.info(f'URL ZIP: {url}')
    resp = urlopen(url)

    # Read the 'stopwords.zip' file in memory
    stopwords_zip = ZipFile(io.BytesIO(resp.read()))

    logger.info(f'List of files in the zip: {stopwords_zip.namelist()}')

    # Local stopwords list
    stopwords = {"ai", "the", "an", "of", "to", "in", 
                 "for", "and", "with", "on", "is", "yc",
                 "s23", "x", "far", "this", "than", "it",
                 "a", "hn", "why", "new", "show", "that"}

    # Read stopwords list from the CSV into the ZIP
    for line in stopwords_zip.open('stopwords.csv').readlines():
        stopwords.add(line.decode('utf-8'))

    logger.info(f'Stopwords size: {len(stopwords)}')

    # Return DataFrame from stopwords list
    return pd.DataFrame(list(stopwords), columns = ['words'])


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
