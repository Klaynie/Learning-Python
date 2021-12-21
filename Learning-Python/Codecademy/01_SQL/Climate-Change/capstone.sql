-- 1 Explore data
SELECT
    *
FROM
    state_climate
;
SELECT
    DISTINCT `state`
FROM
    state_climate
;
-- 2 Running AVG per state
SELECT
    `state`,
    `year`,
    tempc,
    AVG(tempc) OVER (
        PARTITION BY state
        ORDER BY
            `year`
    ) AS 'running_avg_tempc'
FROM
    state_climate
;
-- 3 Lowest temperature per state
SELECT
    *
FROM (
    SELECT
        `state`,
        `year`,
        tempc,
        FIRST_VALUE (tempc) OVER (
            PARTITION BY `state`
            ORDER BY
                `tempc`
        ) AS 'lowest_temp'
    FROM
        state_climate
    ORDER BY
        `state`,
        `year`
)
WHERE
    tempc = lowest_temp
;
-- 4 Highest temperature
SELECT
    *
FROM (
    SELECT
        `state`,
        `year`,
        tempc,
        LAST_VALUE (tempc) OVER (
            PARTITION BY `state`
            ORDER BY
                `tempc` RANGE BETWEEN UNBOUNDED PRECEDING AND
                UNBOUNDED FOLLOWING
        ) AS 'highest_temp'
    FROM
        state_climate
    ORDER BY
        `state`,
        `year`
)
WHERE
    tempc = highest_temp
;
-- 5 Change in temp to previous year
SELECT
    `state`,
    `year`,
    tempc,
    tempc - LAG(tempc, 1, tempc) OVER (
        PARTITION BY `state`
        ORDER BY
            `year`
    ) AS tempc_change
FROM
    state_climate
ORDER BY
    4 DESC
;
-- 6 Rank of lowest temperature
SELECT
    RANK() OVER (
        ORDER BY
            tempc
    ) AS 'coldest_rank',
    `state`,
    `year`,
    tempc
FROM
    state_climate
;
-- 7 Rank of highest temperature by state
SELECT
    RANK() OVER (
        PARTITION BY `state`
        ORDER BY
            tempc DESC
    ) AS 'highest_rank',
    `state`,
    `year`,
    tempc
FROM
    state_climate
ORDER BY
    1,
    2
;
-- 8 Quartiles of coldest temperature by state
SELECT
    NTILE(4) OVER (
        PARTITION BY `state`
        ORDER BY
            tempc
    ) AS 'quartile',
    `state`,
    `year`,
    tempc
FROM
    state_climate
;
-- 9 Quintile of coldest temperature
SELECT
    NTILE(5) OVER (
        ORDER BY
            tempc
    ) AS 'quartile',
    `state`,
    `year`,
    tempc
FROM
    state_climate
;