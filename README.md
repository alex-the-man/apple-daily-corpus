# Apple Daily Corpus - 蘋果日報語料庫
Text corpus of articles published by Apple Daily between 2002/01/01 to 2021/06/20.

## Format
Articles published on the same day are organized into the same csv file. The csv file name represents the published date in `yyyymmdd` format. Each article is stored as a row in the csv.

Each csv has the following columns:
### key

An unique key to identify the row/article.

### date

The published date in `yyyymmdd` format.

### article_daily_id

The id of the article on each day. For example, article with id 0 is the headline of that day.

### title

The title of the article. It is also included at the beginning of the text. Users using column text does not need do extra work to scan this column.
  
### text

The text of the article. Line endings are not preserved.

## Build

Makefile is included to build the corpus from the orginial backup `apple-articles-plaintext-20020101-20210620.zip`. 

To build the corpus:
1. Download `apple-articles-plaintext-20020101-20210620.zip` from the internet. Unzip it to the root of the repository, keep the `data` folder structure. 
2. Run `make all` to build the corpus.
  It requires `xargs`, `python3` and `BeautifulSoup`.
3. csv files are generated under the `corpus` folder.

## Sample using the corpus
2 Spark notebooks are included in the `sample` folder.

### ngram.ipynb

List all frequently used pharses in the corpus.

### sentences.ipynb

Parse and scan for all the sentense in the corpus.

## Missing articles
Some of the articles are missing in the corpus. They are listed in `error.log`.

## License
This dataset is released under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0) license.
