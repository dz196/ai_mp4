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
    # Your code ends here 
    _raise_not_defined()
    return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
    features=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    _raise_not_defined()
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
conditional_cs_true = [] #Log of conditional probabilities for True
conditional_cs_false = [] #Log of conditional probabilities for False
def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    global prior_cs
    global conditional_cs_true
    global conditional_cs_false
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
    print(num_instances)
    n = len(data)

    prior_distribution = []

    for i in range(0, len(num_instances)):
        prior_distribution.append(math.log(float(num_instances[i]) / n))

    #print("Prior Distribution: " + str(prior_distribution))
    prior_cs = prior_distribution   

    #Conditional probabilities of features given each label y; y can be 0-9----------------------------------------

    #K value for smoothing
    k = .0000000000000001

    cond_prob_true = [[[0.0 for r in range(width)] for y in range(height)] for z in range(10)] #Initialize to counts of zero
    cond_prob_false = [[[0.0 for r in range(width)] for y in range(height)] for z in range(10)]
    
    #When a feature is true, increment the pixel by 1 for respective label
    for example in range(0,int(num_examples)):
        label_num = label[example]
        for row in range(0, height):
            for col in range(0, width):
                if (features[example][row][col] == True):
                   cond_prob_true[label_num][row][col] += 1
                else:
                    cond_prob_false[label_num][row][col] += 1

    #Divide the previous by the number of instances of each label
    for label_num in range(0,10):
        for row in range(0, height):
            for col in range(0, width):
                cond_prob_true[label_num][row][col] = math.log((cond_prob_true[label_num][row][col] + k) /(float(num_instances[label_num]) + 2*k))
                cond_prob_false[label_num][row][col] = math.log((cond_prob_false[label_num][row][col] + k) /(float(num_instances[label_num]) + 2*k))


    #print(cond_prob_true[0])
    #print(cond_prob_false[0])
    conditional_cs_true = cond_prob_true
    conditional_cs_false = cond_prob_false
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
    for label in range(0,len(conditional_cs_true)):
        for row in range(0, len(features)):
            for col in range(0, len(features)):
                if features[row][col] == True:
                    sums[label] += conditional_cs_true[label][row][col]
                else:
                    sums[label] += conditional_cs_false[label][row][col]
    max = float("-inf")
    for i in range(0, len(sums)):
        if (sums[i] > max):
            max = sums[i]
            predicted = i
    # Your code ends here 
    return predicted

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):

    predicted=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    for i in range(0, len(data)):
        feature = feature_extractor(data[i], width, height)
        predicted.append(compute_class(feature))
    # Your code ends here 

    return predicted







        
    
