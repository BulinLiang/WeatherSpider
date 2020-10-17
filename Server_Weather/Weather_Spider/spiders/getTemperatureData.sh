#!/bin/bash
export PATH=$PATH:/usr/local/bin

# cd /home/walden/PycharmProjects/Server_Weather/Weather_Spider/spiders

# nohup /home/walden/anaconda3/bin/scrapy crawl temperature --nolog 
cd /home/walden/PycharmProjects/Server_Weather/Weather_Spider/spiders && /home/walden/anaconda3/bin/scrapy crawl temperature --nolog 
 	
