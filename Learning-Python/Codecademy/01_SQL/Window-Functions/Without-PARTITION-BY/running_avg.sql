SELECT month,
  change_in_followers,
  ROUND(AVG(change_in_followers) OVER (
    ORDER BY month
  ), 2) AS running_total
FROM social_media
WHERE username = 'instagram';