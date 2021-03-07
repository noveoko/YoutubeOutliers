## Fake Guru Detection 

Data collection, cleaning, and model training

## Goal
To create a way to automatically classify and discover Youtube channels that may be of interest to fans of YT channels that combat various forms of online activity: [CoffeeZilla](https://www.youtube.com/channel/UCFQMnBA3CS502aghlcr0_aw), [Tom Nash](https://www.youtube.com/results?search_query=tom+nash),[Barely Sociable](https://www.youtube.com/channel/UC9PIn6-XuRKZ5HmYeu46AIw) and others. 

## The Potential Fake Guru List
The following is a list of Youtube creator channels that may or may not match the classification known as "fake guru" which is based on a shortlist of niche content producers. Names are in this list if the trained deep learning model classified a majority of video titles as matching a "fake guru" pattern. Not all creators here are fake gurus, this is because the convention used by fake gurus to name their videos is a sort of standard across Youtube (ie Clickbait titles) so it's a challenge to seperate click-bait from fake guru. :) Also, some people that appeal to young people and flash cars may not be considered fake gurus by the general definition of "overpriced mml seminars etc." but may match the lifestyle/brand in other ways. 

>>> [the list](sorted.md)

## Every PERSON mentioned across all CoffeeZilla episodes

At first I thought there would be a wealth of names on the CoffeeZilla playlists. I used SPACY to try to extract PERSON entities but it's not very good and extracted many random names and mistook name of non-persons for PERSON type. So this is a work in progress for sure. Perhaps such a list could be used in the future to improve the model.

[names mentioned on CoffeeZilla](people_mentioned_on_coffeezilla.txt)

## Life Hacks

Keywords to use to find fake gurus fast

```
feel great make money drop ship love life
```

## Datasets

[Kaggle Youtube videos Dataset](https://www.kaggle.com/datasnaek/youtube-new?select=USvideos.csv)
