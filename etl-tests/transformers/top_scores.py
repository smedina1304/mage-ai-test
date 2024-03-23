from urllib.parse import urlparse

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Select the top 10 scores.

    Args:
        data: Data from load_topstories_ids
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        top10: DataFrame with top 10 scores
    """
    # Specify your transformation logic here

    top10 = data[['url','score']].sort_values('score', ascending=False).copy()[0:10]
    top10['url'] = top10['url'].apply(lambda x: urlparse(x).netloc)

    return top10


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
