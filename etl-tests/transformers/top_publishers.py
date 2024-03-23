if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Post count to check top publishers.

    Args:
        data: Data from load_topstories_ids
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        top_publishers: DataFram with top 10 publishers
    """
    logger = kwargs.get('logger')

    logger.info(f'Data from load_topstories_ids: {data.shape[0]}')

    # Selects data and counts posts by publisher
    topstories = data[['by','url','descendants','score']].copy()
    grp = topstories.groupby(['by'])['by'].count().reset_index(name='counts')
    
    # Select top 10 publishers
    top_publishers=grp.sort_values('counts', ascending=False)[:10]

    return top_publishers


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
