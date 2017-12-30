line = load '/user/cloudera/yelp_academic_dataset_review_clean1.json'
USING JsonLoader('votes: (funny:int, useful:int, cool:int), user_id:chararray, review_id:chararray, text:chararray, business_id:chararray, stars:int, date:chararray, type:chararray');

words = foreach line generate flatten(TOKENIZE((chararray)$3)) as word;

wordgroup = group words by word;
wordcounter = foreach wordgroup generate group, COUNT(words);
store wordcounter into '/user/cloudera/review_wordcountclean1';
