SampleRecord = LOAD '/user/cloudera/ficheroanios'
USING PigStorage(';') AS (Year:chararray);
GroupByYear = GROUP SampleRecord BY Year;
CountByYear = FOREACH GroupByYear
GENERATE CONCAT ((chararray)$0,CONCAT(':',(chararray)COUNT($1)));
STORE CountByYear
INTO '/user/cloudera/contadorAnios' USING PigStorage('t');
