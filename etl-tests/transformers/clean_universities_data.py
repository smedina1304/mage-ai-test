if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Clean and Transform Universities data from Dataframe

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    data['domains'] = [','.join(map(str, l)) for l in data['domains']]
    data['web_pages'] = [','.join(map(str, l)) for l in data['web_pages']]
    data.drop('state-province', axis='columns', inplace=True)
    data.rename(columns={'alpha_two_code': 'country_code'}, inplace=True)
    data = data[['name','country_code','country','domains','web_pages']]
    data = data.reset_index(drop=True)
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
