-- PostgreSQL variant, input from file
-- run with psql -f 04.sql 

-- reset state
DROP TABLE IF EXISTS day04_buf;
CREATE TABLE day04_buf (l text, r text);
\copy day04_buf (l, r) FROM 'input4.txt' WITH DELIMITER ',' CSV;

-- parse & query
WITH ranges AS (
    SELECT  ('[' || REPLACE(l, '-', ',') || ']')::numrange AS l, 
            ('[' || REPLACE(r, '-', ',') || ']')::numrange AS r
    FROM    day04_buf
)   

SELECT  SUM((l @> r OR r @> l)::int) AS part1,
        SUM((l && r)::int) AS part2
FROM    ranges;   
