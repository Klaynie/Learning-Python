"""
Ann watched a TV program about health and learned that it is recommended to sleep at least AAA hours per day. Oversleeping is also unhealthy and you should not sleep more than BBB hours. Now, Ann sleeps HHH hours per day.

Check if Ann's sleep schedule complies with the requirements of that TV program.

The input format:

The input comprises three strings with variables in the following order: A, B , H.

A is always less than or equal to B.

The output format:

If Ann sleeps less than A hours, output "Deficiency", if she sleeps more than B hours, output "Excess".

If H lies between A and B, print "Normal".
"""

hours_a, hours_b, hours_h = int(input()), int(input()), int(input())

if hours_h < hours_a:
    print("Deficiency")
elif hours_h > hours_b:
    print("Excess")
else:
    print("Normal")