**1a**

Flexible statistical learning method: Adapts to training data closer. More subject to variance

Inflexible statistical learning method: Tries best it can to adapt to training data. More subject to bias.

Performance: If given test data it hasn't seen before, how close is this models output to the expected output?

Sample size: Count of independent data sets used in some process, like training or testing

Predictor: Like a variable or parameter. Some quality of the data that could be different among each data set in the sample.

Question: If the sample size (n) is extremely large, and the number of predictors (p) is small, which learning method will have better performance, a flexible or inflexible method and why?

Answer: The actual correct answer here is probably "it depends." Every data set is different. However, 
        broadly speaking, with an extremely large sample size, we'd expect the outliers to have less of an impact 
        because of the CLT. Therefore, an inflexible method might be preferable here. Perhaps something linear
        that appoximates the vast amount of data. The worry with a flexible model is that it will overfit the vast
        amount of data, it will "memorize the data", and becomes too specific to that very large data set and doesn't
        embrace the subtle, underlying pattern of the data, making it perform weaker on new data sets.