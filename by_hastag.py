from TikTokApi import TikTokApi
import pandas as pd

api = TikTokApi.get_instance()

hashtag = api.search_for_hashtags(search_term="tiki", count=28)


data_hashtag1 = pd.DataFrame(hashtag)

