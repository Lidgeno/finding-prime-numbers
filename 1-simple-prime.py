from time import time
begin_time = time()
current_time = round(begin_time)

# 33s for 1 million
max_range = 1000000
prime = False

# imo improve calculation by ~2
prime_list = [2]
prime_counter = 1
prime_limit = [max_range]

# for each number in requested range
for i in range(3,max_range+1,2):
    # we only prove that a number is not prime
    prime = True

    # for each prime number 2 excluded
    for j in range(1, prime_counter):
        if(prime_list[j]**2 > i):
            break
            
        # multiply with other numbers until limit is reached
        for k in range(prime_limit[j],i):
            # until result is over i
            temp_result = k * prime_list[j]
            
            if(i < temp_result):
                # keep record k or use buffer to store over-result
                # buffer was too slow
                # next time, this prime will skip useless calculations
                prime_limit[j] = k
                break
            # if i has been calculated, then it's not a prime number
            elif(i == k * prime_list[j]):
                prime = False
                # reset for j loop
                j = prime_counter+1
                break
                
    # show progress
    if( current_time+1 < time()):
        print(100*i/max_range)
        current_time = time()

    if(prime):
        prime_list.append(i)
        # to avoid repetition as in a*b and b*a
        prime_limit.append(i)
        prime_counter += 1

# display results
print(prime_list)
print(prime_counter)
print(time()-begin_time)
