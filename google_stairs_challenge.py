# create a function that finds all combinations of partitions of n

# the idea is you find all permutations for the lowest to the highest
# every time you find a permutation that inculdes a number in the list, you can add all of
# that numbers permutations to the lower number. For example, 
#
# 4 = 3 + 1 = [3, 1]
# 8 = 4 + 4 = [4, 4]
# 8 = [4, 3, 1]
#
# this will need to be a recursive function that runs on every number added to a permutation.
# For example,
#
# 4 = 3 + 1 = [3, 1]
# 8 = 4 + 4 = [4, 4]
# 8 = [4, 3, 1]
# 20 = 12 + 8 = [12, 8]
# 20 = [12, 8, 3, 1]
# 40 = 20 + 20
# 40 = [20 + 12 + 8]
# 40 = [12, 8, 3, 1]
#
# The recursive function will need to run on the last number of the list of permutations and 
# save the results to an external object called permutations_tracker. The function will also need a function called job_handler, to
# make sure it is not running on a high and lower number symoltaniously.
#
# The find_permutations function will need...
# current_number        ->  the number we are checking all sums for
# 
# 1. find_permutations will first define a counter starting at 1.
# 2. find factorals will then loop from the counter to current_number
#   2a. resulting_factorals will equal a list of [(current_number - counter), counter]
#       for example,
#       current_number = 6
#       counter = 1
#       resulting_factorals = [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]
#   2b. when this process is finished, we run add_permutations(resulting_factorals)
#
# The add_permutations function will need...
# current_number        ->  the number we are checking all sums for
# resulting_factorals   ->  a list of the resulting factorals of a number
# 
# 1. add_permutations will loop through resulting_factorals
# 2. if the 1st of each item is larger than the second 
#       we add the permutation to new_resulting_factorals, 
# 3. if the 2nd number is larger than 2 (as there are no possible permutations for 1 or 2), we look up the number in permutations_tracker
# 4. if the number is in permutations_tracker, we loop though its permutations
#       if the first number in the permutation from the tracker is lower than the first number in the item
#       we add a duplicate item to new_resulting_factorals.
#       For example,
#    
#    current_number = 6
#    new_resulting_factorals = []  
#    resulting_factorals = [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]
#    [5, 1]     ->   5 is greater than 1         ->  new_resulting_factorals = [[5, 1]]
#                    1 is not greater than 2
#    [4, 2]     ->   4 is greater than 2         ->  new_resulting_factorals = [[5, 1], [4, 2]]
#                    2 is not greater than 2
#    [3, 3]     ->   3 is not greater than 3     -> new_resulting_factorals = [[5, 1], [4, 2]]
#                    3 is greater than 2         -> new_resulting_factorals = [[5, 1], [4, 2], [3, 2, 1]]
#    
#    new_resulting_factorals[current_number]   ->  new_resulting_factorals[6] = [[5, 1], [4, 2], [3, 2, 1]]
#    add_permutations returns True
#   back to find_permutations...
#   3.  find_permutations returns True
#
#   the job_handler function will need... 
#   n       ->      the max number of permutations we are looking for
#   
#   1. counter loops though 3 to n:
#      if find_permutations(n): counter = counter+1
#
#   return len(permutations_tracker[n])
#
# Optimisation Ideas...
#
# 1. After we have calculated the total number of permutatons, save the result as a number, as well as an array
#    Then calculate if we can use the number; for example,
#
#     With any number greater than n/2, the available factoral will be all available factorals +1
#     with n/2, the resulting number will be all available factorals
#     with any number smaller n/2, we will need to check
#
#     n = 20
#
#     [19, 1],  ->  1 has none
#     [18, 2],  ->  2 has none
#     [17, 3],  ->  3 has 1
#     [16, 4],  ->  4 has 1
#     [15, 5],  ->  5 has 2
#     [14, 6],  ->  6 has 3
#     [13, 7],  ->  7 has 4
#     [12, 8],  ->  8 has 5
#     [11, 9],  ->  9 has 7
#     [10, 10], ->  10 has 9
#
#     so we only need to loop over these items, to find permutations for item[1] where it's item[0] is
#     smaller than our item[0]. For example,    [9, 11] ->  [10, 1]     ->  10 is not less than 9, so no
#                                                       ->  [5, 4, 2]   ->  5 is less than 9, so yes
#     [9, 11],  
#     [8, 12], 
#     [7, 13], 
#     [6, 14], 
#     [5, 15], 
#     [4, 16], 
#     [3, 17], 
#     [2, 18], 
#     [1, 19]
#   ]
# 
# 2. We could save the smallest second permutation in the tracking object for quick access. For example,
#    
#    n = 14
#       
#    [5, 4, 3, 2] is the permutation with the smallest starting number. So we can save 5.

#    Now, when n = 20, if we get to item [6, 14], we can check to see if the smallest starting number is less than
#    item[0]. It is, so we move on to [5, 15], where the smallest permutation is [5, 4, 3, 2, 1]. The smallest starting
#    number is 5, which is not smaller than our item[0]. Here we can break the loop and safely assume all other numbers
#    aren't going to have resulting permutations.
#
# 3. Instead of creating a list of valid factorals, you make an object with each valid factoral per number, with all possible
#    factorals the number starts with. Then, when a number needs to know how many valid factoals it can add to make up that number, 
#    it can look at how many valid factoals that number has that start with a number smaller than it's first factoral number. For example,
#
#    Say n = 16 and we want to find 5/9, first we cycle up the numbers and when we get to 9...
# 
#     n = 9
#    
#    current perm_list = [
#       [8, 1], 
#       [7, 2], 
#       [6, 3], 
#       [6, 2, 1], 
#       [5, 4], 
#       [5, 3, 1], 
#       [4, 3, 2]
#     ]
#
#    new perm_list = {
#       8: 1,
#       7: 1,
#       6: 2,
#       5: 2,
#       4: 1
#      }
#    
#    now when we get to n = 16 and 5/9...
#
#    we cycle though the saved perms for 9, find any number smaller than 5 and add the possible perms to 5 in the object for 16. In this case,
#    we can see that 9 has one permutation starting with a number less than 5, which is 4. so for perm_tracker[16][5] = 1
#
#    doing this, will reduce the size of each object and the work of itterating though each one. n = 20 currenty looks like this...
#
#   [
#       [19, 1], 
#       [18, 2], 
#       [17, 3],[17, 2, 1], 
#       [16, 4], [16, 3, 1], 
#       [15, 5], [15, 4, 1], [15, 3, 2], 
#       [14, 6], [14, 5, 1], [14, 4, 2], [14, 3, 2, 1], 
#       [13, 7], [13, 6, 1], [13, 5, 2], [13, 4, 3], [13, 4, 2, 1],
#       [12, 8], [12, 7, 1], [12, 6, 2], [12, 5, 3], [12, 5, 2, 1], [12, 4, 3, 1], 
#       [11, 9], [11, 8, 1], [11, 7, 2], [11, 6, 3], [11, 6, 2, 1], [11, 5, 4], [11, 5, 3, 1], [11, 4, 3, 2], 
#       [10, 9, 1], [10, 8, 2], [10, 7, 3], [10, 7, 2, 1], [10, 6, 4], [10, 6, 3, 1], [10, 5, 4, 1], [10, 5, 3, 2], [10, 4, 3, 2, 1], 
#       [9, 8, 3], [9, 8, 2, 1], [9, 7, 4], [9, 7, 3, 1], [9, 6, 5], [9, 6, 4, 1], [9, 6, 3, 2], [9, 5, 4, 2], [9, 5, 3, 2, 1], 
#       [8, 7, 5], [8, 7, 4, 1], [8, 7, 3, 2], [8, 6, 5, 1], [8, 6, 4, 2], [8, 6, 3, 2, 1], [8, 5, 4, 3], [8, 5, 4, 2, 1], 
#       [7, 6, 5, 2], [7, 6, 4, 3], [7, 6, 4, 2, 1], [7, 5, 4, 3, 1], 
#       [6, 5, 4, 3, 2]
#   ]
#
#   whereas, now it will look like this...
#
#       6: 1
#       7: 4
#       8: 8
#       9: 9
#       10: 9
#       12: 6
#       11: 8
#       13: 5
#       14: 4
#       15: 3
#       16: 2
#       17: 2
#       18: 1
#       19: 1
#


def solution(n):

    #permutations_tracker
    permutations_tracker = {}

    #account for 1 and 2
    if n < 3: return 0
         
    #count up to and including n
    for current_number in range(3, n+1):

        #create a list of all two part factorals
        resulting_factorals = []

        #create an object for each number in count
        permutations_tracker[current_number] = {"total": 0}

        #loop from 1 to each number in count
        for counter in range(1, current_number):

            #add all resulting factorals to a list
            resulting_factorals.append([current_number - counter, counter])

        #loop through all factorals
        for dual_factoral in resulting_factorals:

            #if the first number of the factoral is bigger than the second, add it to approved factorals list unnder the number it starts with
            if dual_factoral[0] > dual_factoral[1]:

                #if number hasn't been tracked yet, create it
                permutations_tracker[current_number][dual_factoral[0]] = permutations_tracker[current_number].get(dual_factoral[0], 0) +1
                permutations_tracker[current_number]["total"] = permutations_tracker[current_number]["total"] +1

                #if that factoral is in the tracker
                if dual_factoral[1] in permutations_tracker:

                    #iterate though keys and values of that factoral
                    for longer_factoral_start, number_of_longer_factorals in permutations_tracker[dual_factoral[1]].items():

                        if longer_factoral_start != "total":

                            #add in all factorals for that number
                            permutations_tracker[current_number][dual_factoral[0]] = permutations_tracker[current_number][dual_factoral[0]] + number_of_longer_factorals
                            permutations_tracker[current_number]["total"] = permutations_tracker[current_number]["total"] + number_of_longer_factorals

            #if the first number of the factoral is bigger than the second, add it to approved factorals list unnder the number it starts with
            if dual_factoral[0] <= dual_factoral[1]:

                #if that factoral is in the tracker
                if dual_factoral[0] in permutations_tracker:

                    #iterate though keys and values of that factoral
                    for longer_factoral_start, number_of_longer_factorals in permutations_tracker[dual_factoral[1]].items():

                        if longer_factoral_start != "total":

                            #if the potential factoral starts with a number less than the the first number of the dual factoral
                            if longer_factoral_start < dual_factoral[0]:

                                #if dual_factoral[0] in permutations_tracker[current_number]:
                                permutations_tracker[current_number][dual_factoral[0]] = permutations_tracker[current_number].get(dual_factoral[0], 0) + number_of_longer_factorals
                                permutations_tracker[current_number]["total"] = permutations_tracker[current_number]["total"] + number_of_longer_factorals



    return permutations_tracker[n]["total"]

print(solution(200))