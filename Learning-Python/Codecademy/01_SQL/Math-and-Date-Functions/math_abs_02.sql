/*
 * Find out the absolute value of the difference between the average
 * guess of all students from the actual jelly bean count, which is 804.
 *
 * Is the average guess close to the actual count?
 *
 */
WITH
    solution AS (
        SELECT
            804 AS solution
    )
SELECT
    ROUND(AVG(g.guess), 0) AS average_guess,
    s.solution,
    ABS(ROUND(AVG(g.guess), 0) - s.solution) AS difference
FROM
    guesses g
    CROSS JOIN solution s;