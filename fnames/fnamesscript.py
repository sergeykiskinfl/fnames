# Запускает web-crawler 'free-proxy-list'. Сохраняет полученные данные в файл 'proxies.txt' в ту же папку, где находится скрипт. 
# Если 'proxies.txt' уже есть заменяет его.

import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

filePath = os.path.dirname(os.path.realpath(__file__)) + '/proxies.txt'

if os.path.exists(filePath):
    os.remove(filePath)

process = CrawlerProcess(get_project_settings())

process.crawl('free-proxy-list', filePath)
process.start()
