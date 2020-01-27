def right_justify(value_in_tx):
    max_len = 70
    value_out_tx = (max_len-len(value_in_tx))*' '+value_in_tx
    print(value_out_tx)

right_justify('allen')
right_justify('Spam'*4)