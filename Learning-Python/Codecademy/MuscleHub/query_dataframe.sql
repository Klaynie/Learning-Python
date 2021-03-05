SELECT  visits.first_name 
       ,visits.last_name 
       ,visits.gender 
       ,visits.email 
       ,visits.visit_date 
       ,fitness_tests.fitness_test_date 
       ,applications.application_date 
       ,purchases.purchase_date
FROM visits
LEFT JOIN fitness_tests
ON fitness_tests.first_name = visits.first_name AND fitness_tests.last_name = visits.last_name AND fitness_tests.email = visits.email
LEFT JOIN applications
ON applications.first_name = visits.first_name AND applications.last_name = visits.last_name AND applications.email = visits.email
LEFT JOIN purchases
ON purchases.first_name = visits.first_name AND purchases.last_name = visits.last_name AND purchases.email = visits.email
WHERE visits.visit_date >= '7-1-17'  