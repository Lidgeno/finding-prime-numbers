from time import time
begin_time = time()
current_time = round(begin_time)

# 33s for 1 million
max_range = 10000
prime = False

# array oversize atteint pour value = 274 (24113) + 1/10 , 7 + 2/10
if(max_range < 24113):
    depassement_max_fixe = 7
    depassement_max_float = 2/10
    #int *prime_list = malloc (sizeof(int)*(7+round(i/5)));
    #int *prime_limit = malloc (sizeof(int)*(7+round(i/5)));
else:
    depassement_max_fixe = 274
    depassement_max_float = 1/10
    #int *prime_list = malloc (sizeof(int)*(274+round(i/10)));
    #int *prime_limit = malloc (sizeof(int)*(274+round(i/10)));

# imo improve calculation by ~2
prime_list = [2]
prime_counter = 1
prime_limit = [max_range]

buffer_numbers = []


# for each number in requested range
for i in range(3,max_range+1,2):
    # we only prove that a number is not prime
    prime = True

    # buffer was too slow, plan is to use the ~1 over calculation/prime/number
    if i in buffer_numbers:
        prime = False
        buffer_numbers.remove(i)
    else:
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
                    prime_limit[j] = k+1
                    buffer_numbers.append(temp_result)

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
        #'''
        if(prime_counter - round(i*depassement_max_float) > depassement_max_fixe):
            depassement_max = prime_counter -round(i*depassement_max_float)
            print("depassement: "+str(depassement_max)+" "+str(i))
        #'''

# display results
print(prime_list)
print(prime_counter)
print(time()-begin_time)
