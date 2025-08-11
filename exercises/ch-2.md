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

Analysis: Wrong! A large sample size reduces the risk of overfitting, it does not increase it. Moreover,
          An inflexible method could still perform poorly on an extremely large dataset because perhaps
          the model of the data truly isn't described easily, like linearly, and so your inflexible 
          approach will always have a bias in being inflexible to the subtleties demanded by the data.

**1b**

Question: What if the number of predictors is extremely large, and the number of observations is small, would a flexible
or an inflexible statistical learning method perform better? The p >> n scenario. 

Answer: A large number of predictors. A high dimension data set. A small number of observations of this high dimension data set. What does this imply? This is hard again. Let's start with a low sample data. The problem with flexible methods on low sample data is that they are too eager to fit. They will think they found the holy truth of the data when you've just given them the tip of the iceberg. Intuitively, an inflexible model might be preferable here. Sure, it would be way off in the future, but it takes a more moderate approach when trying to model the data. Think of a line peircing straight in the middle of two independent clusters - it's about equal distance to each. We know it isn't great but we know we've been reasonable. On the topic of a very high number of predictors. Conceptually we might visualize this as a vector with a high number of components. A flexible model might try to create some complicated truth from the sample size, diving into the correlation between the predictors in each sample and striving to create some representation of the behavior that could be very frail actually if only a single new sample was added, it's predictors would cause the whole model to be re-done, AKA variance. The flexible model would obsess over the predictors available and "waste energy" trying to create the perfect fit. 

Analysis: Intution here is correct. Work on the statistical terminology more.

**1c**

Question: ... the relationship between the predictors and the response is highly non-linear?
Answer: We would try a flexible model and want to train it with large sample size to avoid overfitting. 
Analysis: Correct. An inflexible model would underfit and perform poorly.

**1d**

Question: ... the variance of the error terms, is extremely high? 
Answer: The variance is already very high to begin with. How do we correct for that? If the variance is high, this means 
        that any given predictor might be.. way off from the mean. Consider if we had a small sample size.
        We don't want to overfit a piece of data that could potentially already be way far off from the expected observation. This variance, this default variance, it must be coming from somewhere. I am suggesting that the 
        predictors themselves are less reliable because of the default high variance. But is that reasonable? Perhaps 
        the variance is some constant based on factors that have nothing to do with the predictors, e.g. our predictors are age and location and the variance is day of the week. No correlation. 

        That leaves us with this. Will an inflexible or flexible model combat an innate high variance more? 
        A flexible model will perform better here and help level out some of the variance, broadly speaking.
Analysis: Wrong! An inflexible model is better here. The flexible model will overfit the varied data. The inflexible
          model has low variance so doesn't contribute to the variance problem. Generally if you have a variance 
          problem, don't use a flexible model and introduce more variability. 
          On the matter of our predictors being influenced by high noise aka ϵ. Well, the predictors are not, 
          but the outcome aka F(x) is. And it's randomly influenced too, if ϵ is high then there is a higher chance 
          that our F(x) output will be jumpy, sporadic.. variable. Using a flexible model is not a smart move here.


***For all problems in 2. Explain whether they are a classification problem or regression problem. 
Indicate whether we are most interested in inference or prediction. 
Provide n and p.***

**2a** 

This is a regression problem. CEO salary is quantitative which implies regression.

This is an inference problem. We want to know how one or more predictors impacts the result.

n = 500
p = {profit, # of employees, industry, CEO salary}.count = 4



