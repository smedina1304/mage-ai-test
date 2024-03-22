import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, data_2, *args, **kwargs):
    """
    Counts the most frequently used words in the news.

    Args:
        data: Data from load_topstories_ids
        data_2: Data from load_stopwords_zip
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    logger = kwargs.get('logger')

    logger.info(f'Data from load_topstories_ids: {data.shape[0]}')
    logger.info(f'Data from load_stopwords_zip : {data_2.shape[0]}')

    # stopwords - Convert from dataframe to set
    stopwords = set(data_2['words'].tolist())

    # topstories - Copy from original Data
    topstories = data.copy()

    # loop through the titles and count the frequency of each word
    word_counts = {}
    for raw_title in topstories["title"]:
        title = raw_title.lower()
        for word in title.split():
            cleaned_word = word.strip(".,-!?:;()[]'\"–")
            if cleaned_word not in stopwords and len(cleaned_word) > 0:
                word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1

    # Get the top 25 most frequent words
    top_words = {
        pair[0]: pair[1]
        for pair in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    }

    logger.info(f'top_words is {type(top_words)}')

    return top_words


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
