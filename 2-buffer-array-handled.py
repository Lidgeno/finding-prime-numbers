from time import time
begin_time = time()
current_time = round(begin_time)

# 24s for 10 mille
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
prime_limit = []
#buffer_numbers = [] '''but if it is c malloc'''
buffer_numbers = [0]*max_range
# * (depassement_max_fixe+ round(max_range*depassement_max_float))
#for i in range(1,depassement_max_fixe+ round(max_range*depassement_max_float)):
#    buffer_numbers.append(0)

# for each number in requested range
for i in range(3,max_range+1,2):
    # we only prove that a number is not prime
    prime = True

    # buffer was too slow, plan is to use the ~1 over calculation/prime/number
    '''
    if i in buffer_numbers:
        prime = False
        buffer_numbers.remove(i)
    else:
    '''
    if(i==buffer_numbers[0]):
        prime = False
        counter_organize_array = 0
        while(buffer_numbers[counter_organize_array] != 0):
            buffer_numbers[counter_organize_array]= buffer_numbers[counter_organize_array+1]
            counter_organize_array += 1
    else:
        # for each prime number 2 excluded
        for j in range(1, prime_counter):
            if(prime_list[j]**2 > i):
                break
            # multiply with other numbers until limit is reached
            for k in range(prime_limit[j],i,2):
                if(2*round(k/2)==k):
                    print("warning: ",k)
                    break
                # until result is over i
                temp_result = k * prime_list[j]
                if(i < temp_result and temp_result < max_range):
                    # keep record k or use buffer to store over-result

                    # buffer was too slow
                    #buffer_numbers.append(temp_result)
                    prime_limit[j] = k+2
                    counter_organize_array = 0
                    # we should add a test of lenght of array for each while but let's not
                    while(temp_result > buffer_numbers[counter_organize_array] and buffer_numbers[counter_organize_array] != 0 ):
                        if(temp_result == buffer_numbers[counter_organize_array]):
                            break
                        counter_organize_array += 1
                    while(buffer_numbers[counter_organize_array] != 0):
                        if(temp_result == buffer_numbers[counter_organize_array]):
                            break
                        temp_stored = buffer_numbers[counter_organize_array]
                        buffer_numbers[counter_organize_array] = temp_result
                        temp_result = temp_stored
                        counter_organize_array += 1
                    if(temp_result != buffer_numbers[counter_organize_array]):
                        buffer_numbers[counter_organize_array] = temp_result

                    # next time, this prime will skip useless calculations
                    # prime_limit[j] = k
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
print(buffer_numbers)
print(prime_list)
print(prime_counter)
print(time()-begin_time)
