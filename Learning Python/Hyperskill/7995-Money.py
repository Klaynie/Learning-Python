"""
Emilia is working in a bank and she has data about some transactions. The transactions are given as a list of tuples named transactions where 
the first element of the tuple is the account id and the second — the sum spent in the transaction.

Help Emilia turn this data into a dictionary where a key is an account id and its value is the list of the money spent in transactions. 
The sums of money on this list should be in their original order!

The new dictionary should be named transaction_dict, create it but don't print anything, we'll check it ourselves.
For example, transaction_dict may look like this {546: [987.65]}. The value of the key 546 should be [987.65] because 
the account with the id 546 made only one transaction.

Note, that you can import any modules if necessary!
"""
from collections import defaultdict

transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

total_transactions_list_dict = defaultdict(list)

for transaction in enumerate(transactions):
    total_transactions_list_dict.setdefault(transaction[1][0], []).append(transaction[1][1])

print(total_transactions_list_dict.items())