import io
import json
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_topstories_ids(*args, **kwargs):
    """
    Get IDs list of top stories.

    API Docs: https://github.com/HackerNews/API#new-top-and-best-stories.
    """

    logger = kwargs.get('logger')

    # Prepare to execute the Top Stories ID List request
    newstories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    count_items = len(requests.get(newstories_url).json())
    top_new_story_ids = requests.get(newstories_url).json()[:100]

    logger.info(f"Total of {count_items} items, selected the first {len(top_new_story_ids)}.")

    # For each ID in the list, get the data in the news
    results = []
    for item_id in top_new_story_ids:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        ).json()
        results.append(item)

        if len(results) % 20 == 0:
            logger.info(f"Got {len(results)} items so far.")

    # Return the DataFrame of the Top Stories
    return pd.DataFrame(results)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
