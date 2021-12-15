SELECT
    STRFTIME('%d', b.order_date) AS `day`,
    COUNT(*) AS number_of_orders
FROM
    bakery b
GROUP BY
    STRFTIME('%d', b.order_date)
ORDER BY
    COUNT(*) DESC;