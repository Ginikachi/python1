## No 16b:
week = 0
rat_1_weight = 10    ## initial weight of rat 1 arbitrarily assigned
rat_2_weight = 10    ## initial weight of rat 2 arbitrarily assigned
rat_1_rate = 0.04    ## growth rate of rat 1 arbitrarily assigned
rat_2_rate = 0.01    ## growth rate of rat 2 arbitrarily assigned
while rat_1_weight < (rat_2_weight + 0.1 * rat_2_weight):
    rat_1_weight = rat_1_weight + rat_1_weight * rat_1_rate
    rat_2_weight = rat_2_weight + rat_2_weight * rat_2_rate
    print(rat_1_weight, rat_2_weight)
    week = week + 1

print("It took", week, "weeks for rat 1 to be 10 percent heavier than rat 2.")

## No 16a:
if __name__ == '__main__':
    week = 0
    rat_1_weight = 10  ## i.e. rat weight at week 0 is arbitrarily assigned weight of 10
    rat_1_rate = 0.04    ## growth rate of rat 1 is arbitrarily assigned 4 percent
    while rat_1_weight < 12.5:
        rat_1_weight = rat_1_weight + rat_1_weight * rat_1_rate
        print (rat_1_weight)
        week = week + 1

print ("It took", week, "weeks for the weight of the first rat to become 25 percent heavier than its original weight.")

## See rough 16.py and rough no 16.py for alternatives. alternatives need some
## modifications. keep trying to get answer in the same format as codes above. 
