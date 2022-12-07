-- PostgreSQL variant, input from file
-- run with psql -f 04.sql 

-- reset state
DROP TABLE IF EXISTS day04_buf, day04_ranges;
CREATE TABLE day04_buf (l VARCHAR(255), r VARCHAR(255));
CREATE TABLE day04_ranges (l numrange, r numrange);

\copy day04_buf (l, r) FROM 'input4.txt' WITH DELIMITER ',' CSV;

-- parse input as ranges
INSERT INTO day04_ranges (l,r)
SELECT  ('[' || REPLACE(l, '-', ',') || ']')::numrange AS l, 
        ('[' || REPLACE(r, '-', ',') || ']')::numrange AS r
FROM    day04_buf;
    
-- query
SELECT  SUM(CASE WHEN l @> r OR r @> l THEN 1 ELSE 0 END) AS part1,
        SUM(CASE WHEN l && r THEN 1 ELSE 0 END) AS part2
FROM    day04_ranges;   
