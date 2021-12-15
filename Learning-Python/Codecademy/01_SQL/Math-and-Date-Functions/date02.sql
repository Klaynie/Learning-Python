SELECT
    b.*,
    DATETIME(b.order_date, 'start of day', '+2 days', '+7 hours') AS pickup_time
FROM
    bakery b;