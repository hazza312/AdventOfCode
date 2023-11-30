-- PostgreSQL variant, input from file
-- run with psql -f 05.sql 
-- treat each stack element as a row, all stacks in single table

-- reset state
DROP VIEW IF EXISTS commands;
DROP TABLE IF EXISTS stacks, buf;
CREATE TABLE stacks (id SERIAL, crate CHAR, stack INT);
CREATE INDEX idx_stack ON stacks (stack);
CREATE TABLE buf (id SERIAL, line VARCHAR(255));

-- read initial stack and commands into buffer table
\copy buf (line) FROM 'input5.txt'

-- mark the first line of non-crate input
SELECT id as endcrateline FROM buf WHERE SUBSTR(line, 2, 1) = '1' \gset

-- insert the initial items from the stack
WITH ids AS (SELECT generate_series AS i FROM generate_series(1, 9))
INSERT INTO stacks (stack, crate)
SELECT      i AS stack, SUBSTR(buf.line, 2 + 4 * (i-1), 1) AS chr 
FROM        buf 
CROSS JOIN  ids 
WHERE       buf.id < :endcrateline 
AND         SUBSTR(buf.line, 2 + 4 * (i-1), 1) NOT IN (' ', '')
ORDER BY    buf.id DESC, ids.i ASC;

-- helper view to parse the commands
CREATE VIEW commands AS 
WITH regex AS (
    SELECT      regexp_match(line, 'move (\d+) from (\d+) to (\d+)') AS match
    FROM        buf
    WHERE       buf.id >= :endcrateline+2
    ORDER BY    id ASC
)
SELECT match[1]::int AS n, match[2]::int AS src, match[3]::int AS dst FROM regex;

-- for each command, delete rows from src stack, and insert into dst stack
-- change DESC to ASC in the INSERT query to control order items items are
-- pushed onto the dst stack (DESC for first part of puzzle, ASC for second)
DO $$
DECLARE 
    cmd record;
BEGIN
    FOR cmd in SELECT n, src, dst FROM commands 
    LOOP
        WITH deletion as (
            DELETE FROM stacks
            WHERE id IN (SELECT     id 
                        FROM        stacks
                        WHERE       stack = cmd.src 
                        ORDER BY    id DESC 
                        LIMIT       cmd.n)
            RETURNING id, crate
        )
        INSERT INTO stacks (crate, stack) 
        SELECT      crate, cmd.dst 
        FROM        (SELECT     crate
                    FROM        deletion
                    ORDER BY    deletion.id DESC -- <-- this
                    ) as _;
    END LOOP;
END; 
$$;

WITH top_ids AS (
    SELECT      MAX(id) as id 
    FROM        generate_series(1, 9) 
    JOIN        stacks ON stacks.stack = generate_series
    GROUP BY    generate_series 
    ORDER BY    generate_series ASC
)
SELECT  STRING_AGG(crate, '') AS result
FROM    (SELECT crate from top_ids JOIN stacks USING (id) ORDER BY stack) as _;
