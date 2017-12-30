#!/usr/bin/env python
import re
import json

review_clean = open('yelp_academic_dataset_review_clean1.json', 'w+')
line_counter = 0

for line in open('yelp_academic_dataset_review.json'):
  if line_counter < 1000:
	line_counter += 1
	review_json = json.loads(line)
  	review_json['text']=review_json['text'].replace('\n', ' ').replace('!', ' ').replace('.', ' ').replace(',', ' ').replace(';', ' ').encode('utf-8').lower()
  	json.dump(review_json, review_clean)
  	review_clean.write('\n')

