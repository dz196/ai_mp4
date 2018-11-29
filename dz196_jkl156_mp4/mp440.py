import inspect
import sys
import math
'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)


'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
'''
def extract_basic_features(digit_data, width, height):
    features=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    for row in range(0, height):
        arr = []
        for col in range(0, width):
            if digit_data[row][col] == 0:
                arr.append(False)
            else:
                arr.append(True)
        features.append(arr)
    # Your code ends here 
    return features

'''
Extract advanced features that you will come up with 
'''
def extract_advanced_features(digit_data, width, height):
    features=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    #FEATURE 1: Accounting for the white space
    feature_1 = []
    for row in range(0, height):
        arr = []
        for col in range(0, width):
            if digit_data[row][col] == 0:
                arr.append(False)
            else:
                arr.append(True)
        feature_1.append(arr)
    features.append(feature_1)
    #FEATURE 2: Accounting for just the + signs which border the number
    feature_2 = []
    for row in range(0, height):
        arr = []
        for col in range(0, width):
            if digit_data[row][col] == 2:
                arr.append(True)
            else:
                arr.append(False)
        feature_2.append(arr)
    features.append(feature_2)
    # Your code ends here 
    return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
    features=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    feature_1 = []
    for row in range(0, height):
        arr = []
        for col in range(0, width):
            if digit_data[row][col] == 0:
                arr.append(False)
            else:
                arr.append(True)
        feature_1.append(arr)
    features.append(feature_1)
    #FEATURE 2: Accounting for just the + signs which border the number
    feature_2 = []
    for row in range(0, height):
        arr = []
        for col in range(0, width):
            if digit_data[row][col] == 2:
                arr.append(True)
            else:
                arr.append(False)
        feature_2.append(arr)
    features.append(feature_2)
    # Your code ends here 
    return features

'''
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
'''
prior_cs = []   #Log of prior probabilities
conditional_cs = [] #Log of conditional probabilities for True
feautre_1 = []
feature_2 = []
feature_3 = []
def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    global prior_cs
    global conditional_cs
    num_examples = percentage / 100 * len(data)
    #Features for percentage of data
    features = []
    for example in range(0, int(num_examples)):
        features.append(feature_extractor(data[example], width, height))
    #Prior distribution over labels; P(Y) = c(y) / n ----------------------------------------------------------------------
    #c(y) is the number of training instances with label y; n is the total number of training instances

    num_instances = [0,0,0,0,0,0,0,0,0,0] #10 values 0-9
    for i in range(0, int(num_examples)):
        num_instances[label[i]] += 1
    #print(num_instances)

    prior_distribution = []

    for i in range(0, len(num_instances)):
        prior_distribution.append(math.log(float(num_instances[i]) / len(data)))

    #print("Prior Distribution: " + str(prior_distribution))
    prior_cs = prior_distribution   
    #----------------------------------------------------------------------------------------------------------------
    #K value for smoothing
    k = 1
    #Conditional probabilities of features given each label y; y can be 0-9----------------------------------------
    if len(features[0]) == 28:

        cond_prob = [[[0.0 for r in range(width)] for y in range(height)] for z in range(10)] #Initialize to counts of zero
        
        #When a feature is true, increment the pixel by 1 for respective label
        for example in range(0,int(num_examples)):
            label_num = label[example]
            for row in range(0, height):
                for col in range(0, width):
                    if (features[example][row][col] == True):
                       cond_prob[label_num][row][col] += 1
          
        #Divide the previous by the number of instances of each label
        for label_num in range(0,10):
            for row in range(0, height):
                for col in range(0, width):
                    cond_prob[label_num][row][col] = (cond_prob[label_num][row][col] + k) /(float(num_instances[label_num]) + 2*k)

        conditional_cs= cond_prob
    elif len(features[0]) == 2:
        cond_prob_1 = [[[0.0 for r in range(width)] for y in range(height)] for z in range(10)]
        #First feature 
        for example in range(0,int(num_examples)):
            label_num = label[example]
            for row in range(0, height):
                for col in range(0, width):
                    if (features[example][0][row][col] == True):
                       cond_prob_1[label_num][row][col] += 1
        #Divide the previous by the number of instances of each label
        for label_num in range(0,10):
            for row in range(0, height):
                for col in range(0, width):
                    cond_prob_1[label_num][row][col] = (cond_prob_1[label_num][row][col] + k) /(float(num_instances[label_num]) + 2*k)
        conditional_cs.append(cond_prob_1)

        cond_prob_2 = [[[0.0 for r in range(width)] for y in range(height)] for z in range(10)]
        #Second feature 
        for example in range(0,int(num_examples)):
            label_num = label[example]
            for row in range(0, height):
                for col in range(0, width):
                    if (features[example][1][row][col] == True):
                       cond_prob_2[label_num][row][col] += 1

        #Divide the previous by the number of instances of each label
        for label_num in range(0,10):
            for row in range(0, height):
                for col in range(0, width):
                    cond_prob_2[label_num][row][col] = (cond_prob_2[label_num][row][col] + k) /(float(num_instances[label_num]) + 2*k)

        conditional_cs.append(cond_prob_2)
        #Third Feature
        cond_prob_3 = [[[0.0 for r in range(width/2)] for y in range(height)] for z in range(10)]   #Only take right half 
        
        for example in range(0,int(num_examples)):
            label_num = label[example]
            for row in range(0, height):
                for col in range(width/2, width):#RIGHT HALF
                    if (features[example][0][row][col] == True):    #Can just use the first feature array
                       cond_prob_3[label_num][row][col-width/2] += 1
        for label_num in range(0,10):
            for row in range(0, height):
                for col in range(0, width/2):
                    cond_prob_3[label_num][row][col] = (cond_prob_3[label_num][row][col] + k) /(float(num_instances[label_num]) + 2*k)
        conditional_cs.append(cond_prob_3)
    else:
        print("ERROR")
    # Your code ends here 

'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
    predicted = -1
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    #Log of prior probabilites summed with conditional probabilities where pixel = true
    sums = list(prior_cs)
    sums2 = list(prior_cs)
    sums3 = list(prior_cs)
    #Extract Basic Feature Computation
    if len(features) == 28:
        for label in range(0,len(conditional_cs)):
            for row in range(0, len(features)):
                for col in range(0, len(features)):
                    if features[row][col] == True:
                        sums[label] += math.log(conditional_cs[label][row][col])
        #Calculate Max
        max = float("-inf")
        for i in range(0, len(sums)):
            if (sums[i] > max):
                max = sums[i]
                predicted = i

    elif len(features) == 2:
        for label in range(0,len(conditional_cs[0])):
            for row in range(0, len(features[0])):
                for col in range(0, len(features[0])):
                    if features[0][row][col] == True:
                        sums[label] += math.log(conditional_cs[0][label][row][col])
                    else:
                        sums[label] += math.log(1-conditional_cs[0][label][row][col])

        for label in range(0,len(conditional_cs[1])):
            for row in range(0, len(features[1])):
                for col in range(0, len(features[1])):
                    if features[1][row][col] == True:
                        sums2[label] += math.log(conditional_cs[1][label][row][col])
                    #else:
                        #sums2[label] += math.log(1-conditional_cs[1][label][row][col])

        for label in range(0,len(conditional_cs[2])):
            for row in range(0, len(features[0])):
                for col in range(0, len(features[0])/2):
                    if features[0][row][col+len(features[0])/2] == True:
                        sums3[label] += math.log(conditional_cs[2][label][row][col])
                    #else:
                        #sums3[label] += math.log(1-conditional_cs[2][label][row][col])
        
        #Calculate max and get prediction
        predicted = bestguess(sums, sums2, sums3)

        """max = float("-inf")
        for i in range(0, len(sums)):
            if (sums3[i] > max):
                max = sums3[i]
                predicted = i"""

    else:
        print("ERROR")
        return None


    # Your code ends here 
    return predicted
def bestguess(sums, sums2, sums3):
    guess1 = -1
    guess2 = -1
    guess3 = -1
    max = float("-inf")
    max2 = float("-inf")
    max3 = float("inf")

    for i in range(0, len(sums)):
        if (sums[i] > max):
            max = sums[i]
            guess1 = i
        if (sums2[i] > max2):
            max2 = sums2[i]
            guess2 = i
        if (sums3[i] > max3):
            max3 = sum3[i]
            guess3 = i
    if (guess1 == guess2 and guess2 == guess3):
        return guess1
    elif(guess1 == guess3 and guess2 != guess3):
        return guess1
    elif(guess1 == guess2 and guess2 != guess3):
        return guess1
    elif(guess2 == guess3 and guess1 != guess2):
        return guess2
    else:
        return guess1

    return None
'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):

    predicted=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    for i in range(0, len(data)):#len(data)
        feature = feature_extractor(data[i], width, height)
        predicted.append(compute_class(feature))
    # Your code ends here 

    return predicted







        
    
