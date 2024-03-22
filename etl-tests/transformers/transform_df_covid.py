from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df: DataFrame, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    
    df = df[['date',	'confirmed',	'deaths',	'recovered',	'tests',	'vaccines',	'people_vaccinated',
         'people_fully_vaccinated',	'administrative_area_level_1',	'administrative_area_level_2',	
         'population',	'iso_alpha_3',	'iso_alpha_2',	'key_jhu_csse',	'key_gadm']].copy()

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
