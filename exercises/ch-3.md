### Conceptual 

1. 

__Describe the null hypotheses to which the p-values given in Table 3.4
correspond. Explain what conclusions you can draw based on these
p-values. Your explanation should be phrased in terms of sales, TV,
radio, and newspaper, rather than in terms of the coefficients of the
linear model.__

Conclusion: The data shows it is highly unlikely that devoting money towards TV or Radio will NOT lead
to an increase in sales. For newspaper, the data is inconclusive. If we want to make more sales, advertising in either TV or Radio will help us. Until we analyze the data more, 
we should choose either TV or Radio but not both, as we don't understand their relationship when together yet. If we need to make a decision on TV vs Radio, the data suggests that radio will have a stronger increase in sales.

Intercept p-value: Very low, reject the null hypothesis that there is not a base, default amount of sales irrespective of advertising

TV p-value: Very low, reject the null hypothesis that increasing TV advertising does not lead to increase in sales

radio p-value: Very low, reject the null hyptothesis that increasing radio advertising does not lead to increase in sales

newspaper p-value: Very high, fail to accept the null hypothesis, increasing just newspaper sales does not increase sales


Analysis: 
- NEVER "accept" the null hypothesis. We "fail to reject" it. 
- My thinking about the coefficients is shallow - just because one has a higher coefficient than the other, it does not mean that's where surely the money should go. If the budgets 
AKA units of both were same, then that would be true. If they were closer, we'd need 
to consider their ranges, but in the case here they are so close that we can pretty confidently
choose the one with the highest coefficient.
- Interaction effect is valid but be careful when answering the question. You can model TV vs others by holding them constant and still get answer for "should we spend on both" if they are not run simultaneuosly and thus not subject to the interaction effect. That being said, 
it seems the data shown presumed that it was an additive effect and no interaction.

2. Carefully explain the differences between KNN classifier and KNN regression methods.

KNN classifer: We classify some qualitative predictor by checking K neighbors next to it. 
               The neighbor which has the most count is what our predictor is classified as.

KNN regression: We try to fit a non-linear model by using KNN regression which has less
                innate bias than normal linear regression. A non-parametric method.
                We find where f(x) lands and then take the average of the K neighbors 
                around it, that becomes the estimate for f(x) in KNN. 

Key differences: 
    - KNN classifier doesn't use an average of the K neighbors, KNN regression does
    - KNN regression is quantitative - we're trying to model the function

Analysis:
    - Pretty much correct. Obvious addition: classifer vs regression problem, each has own use


**3a**

x1 = GPA

x2 = IQ

X3 = Level (1 for college, 0 for high school)

x4 = Interaction between GPA and IQ 

x5 = Interaction between GPA and Level

Response = starting salary after graduation (in thousands of dollars)

Suppose we use least squares to fit the model, and get:

b0 = 50 (intercept)

b1 = 20 (GPA)

b2 = .07 (IQ)

b3 = 35 (Level)

b4 = .01 (IQ and GPA)

b5 = -10 (GPA and Level)

$\hat{f}(x) = 50 + 20x_1 + 0.07x_2 + 35x_3 + 0.01(x_1 \cdot x_2) - 10(x_1 \cdot x_3)$

Where the variables are interpreted as:

* $x_1$: GPA
* $x_2$: IQ
* $x_3$: Education Level (0 = High School, 1 = College)
* $(x_1 \cdot x_2)$: Interaction between GPA and IQ
* $(x_1 \cdot x_3)$: Interaction between GPA and Education Level


Analysis of the function behavior: 
- Everyone has a default 
starting salary of 50 no matter if they went to college or not.

- You get a small boost to your starting salary the higher the product of your GPA and IQ is (small boost, it's not significant compared to other factors).

- Generally, IQ has a positive impact on your starting salary. 

- If you did not go to college, you are not subject a GPA penalty that college grads have. College grads actually have a small decrease in starting salary 
that scales with their GPA, higher GPA = greater decrease in starting salary,
which is puzzling

- However, college grads get the biggest boost to their income potential too. This invididual predictor (not considering any other interaction effects) is the single strongest predictor of starting salary 

- GPA, too, is a strong predictor of starting salary - this is true if you went to college or not. Even more, high school students with a high GPA don't get punished by the interaction effect by GPA and education level like college students do, so high school students in particular should try to get a high GPA if they want a good starting salary out of high school.

True or false: For a fixed value of IQ and GPA, high school graduates earn
more, on average, than college graduates?

ANSWER: FALSE

RATIONALE: The high school grad needs to have a very high GPA and then they will make more

True of false: For a fixed value of IQ and GPA, college graduates earn
more, on average, than high school graduates.

ANSWER: FALSE

RATIONALE:  This is an absolute statement. We know for high GPAs this isn't true. This must be false.

True of false: For a fixed value of IQ and GPA, high school graduates earn
more, on average, than college graduates provided that the
GPA is high enough.

ANSWER: TRUE

RATIONALE: Proof by opposite of below

True or false: For a fixed value of IQ and GPA, college graduates earn
more, on average, than high school graduates provided that
the GPA is high enough.

ANSWER: FALSE

RATIONALE: A college graduate who has a really high GPA could lose to a high school grad with a very high GPA because the high school grad would get all the benefit of x1 without the penalty of the interaction effect. 


**3b**

Predict the salary of a college graduate with IQ of 110 and a
GPA of 4.0.

Answer:

50 + 20(4.0) + .07(110) + 35(1) + .01 (4.0 * 110) - 10 (4.0 * 1) = ~137


**3c**

False. It doesn't mean that there is no evidence for the effect, it just means thats the effect itself is small. We would need to look at the p-value to examine the evidence for this interaction event, AKA what is the chance we would see this interaction event by random chance. If less than some threshold, then we reject the null hypothesis that there is no interaction effet between GPA and IQ. 


**4a**

n = 100 observations 
1 predictor, 1 response

Y = b0 + b1x + b2x^2 + b3x^3 + E

Suppose true relationship is linear.

Would we expect the RSS for the linear regression and also the RSS for the cubic regression. 

Question: Would we expect one to be lower than the other, would be expect them to be the same, or is there not enough info to tell? Justify your answer.

Answer: 

        On the training set:

            Cubic regression: 
            We expect the cubic regression model to be flexible and adapt to the observations. However, with only 100 observations, it might not be enough
            for the flexible cubic regression to adhere to the linear model. To be confident that the cubic regression could fit, we need a lot higher observations.

            Linear regression: 
            If the true relationship is linear, then the linear regression will perform well. It will not suffer the bias penalty it will have on 
            non-linear models and thus in only 100 observations should closely match the true relationship. 
            
        1 predictor and 1 response is a simple setup. It gives us hope that the cubic regression might actually perform better than we think. 
        Still, _linear regression in 100 observations should have a lower RSS than the cubic regression_ because it won't suffer from a bias 
        or variance penalty. The cubic regression will be "catching up" while the linear regression will be fine-tuning the model and possibly
        approaching the true relationship quicker in 100 observations. 
        
        It's close... It could largely depend on the data. E.g. if the data patterns are consistent (standard deviation is low) then perhaps the cubic regression
        could be about the same as the linear regression. Still, the cubic regression has to overcome making a non-linear function linear... it will always have that
        hurdle...

**4b**

On test data, we expect the linear regression to have a lower RSS. The cubic regression could have mastered the training set in 100 observations, but it shows high variance - if presented with test data that say has outliers, it will perform much more poorly than the linear regression and have a higher RSS.

**4c**

If the true relationship is not linear, but we don't know how far, it's hard to say, there is not enough information to tell. 
Practically we could start with a linear regression and see how it performs. If it performs poorly, we switch to the cubic regression. 

A linear model has a default bias that is a penalty on any non-linear model. With 100 observations, the cubic regression would probably
perform better (have a lower RSS) than the linear regression.

**4d**

I would expect the cubic regression to perform better than the linear regression on test data. 
It will have adhered to the non-linear model better and suffer from less bias. 
The linear regression could have not even made much progress on the model after 100 observations if the model is non-linear enough, whereas 100 
training observations could produce good progress for the cubic regression. 


**4-Analysis**

**4a** WRONG. For the TRAINING set, the more flexible model will have an RSS <= less flexible model. The non-linear model can simply set coefficients to 0 if it needs and also it could find non-zero values for some coefficients (it has more) that allow it to fit the set better.

**4b** Correct

**4c** Correct

**4d** Not nuanced enough. The correct answer depends on degree on non-linearity. If the non-linearity is small, the linear model will win because the cubic model will have
        higher variance from the training set. The linear models bias would not hurt as much as the variance. Conversely, if the non-linear model is highly non-linear
        the bias penalty will be too great for the linear model. So it depends. This is about the bias-variance tradeoff.

