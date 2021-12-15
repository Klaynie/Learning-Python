SELECT
    b.*,
    (b.price - CAST(discount AS REAL)) * b.quantity AS order_total_after_discount
FROM
    bakery b;