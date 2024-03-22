import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Loading Universities data from API
    """
    p_country = kwargs['param_country']
    url = f'http://universities.hipolabs.com/search?country={p_country}'
    response = requests.get(url).json()
    df = pd.DataFrame(response)

    print(f"Total Number of universities in {p_country} returned by API {len(df)}")

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
