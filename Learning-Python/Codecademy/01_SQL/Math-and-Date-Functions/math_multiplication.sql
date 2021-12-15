SELECT
    b.*,
    b.price * b.quantity AS order_total
FROM
    bakery b;