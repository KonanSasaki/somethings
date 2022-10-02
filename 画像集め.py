#lxmlのバージョンは3.7.3以下にする。そうじゃないとエラーが発生する。
from icrawler.builtin import BingImageCrawler

# クローラーを生成、保存先などを指定
bing_crawler = BingImageCrawler(downloader_threads=4,storage={'root_dir':'C:\\XXXX'})

# キーワードや枚数を入力させてそれに応じて画像収集する
bing_crawler.crawl(keyword=str(input('キーワード')), filters=None, offset=0, max_num=int(input('枚数')))
