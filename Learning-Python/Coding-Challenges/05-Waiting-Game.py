import random
import time


def waiting_game():
    time_to_wait = random.randint(1, 10)
    print(f"Your target time is {time_to_wait} seconds")
    input("---Press Enter to Begin---")
    begin = time.time()
    input(f"...Press Enter again after {time_to_wait} seconds...")
    end = time.time()
    elapsed_time = end - begin
    print(f"Elapsed time: {elapsed_time:0.3f} seconds")
    if elapsed_time > time_to_wait:
        print(f"{elapsed_time - time_to_wait:0.3f} seconds too slow")
    elif elapsed_time < time_to_wait:
        print(f"{time_to_wait - elapsed_time:0.3f} seconds too fast")
    else:
        print("Right on time!")


waiting_game()