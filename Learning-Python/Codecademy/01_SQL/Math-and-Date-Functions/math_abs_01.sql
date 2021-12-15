/*
 * A school holds an event every month where a glass jar is filled
 * with jelly beans, and students can guess how many jelly beans
 * are contained in the jar. Students who make the closest guess
 * win a pack of new notebooks.
 *
 * Using the guesses table with the ABS() function, write a query
 * to find out how close each student’s guess is to the actual number
 * of jelly beans in the jar, which is 804.
 * Select the name and the absolute difference of each guess from 804.
 *
 * How close are each of the guesses?
 *
 */
WITH
    solution AS (
        SELECT
            804 AS solution
    )
SELECT
    AVG(g.guess),
    s.solution,
    ABS(AVG(g.guess) - s.solution) AS difference
FROM
    guesses g
    CROSS JOIN solution s;