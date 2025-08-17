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


3. 

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

f(x) = 50 + 20x1 + .07x2 = 35x3 + .01x4 - 10x5

True or false:  For a fixed value of IQ and GPA, high school graduates earn
more, on average, than college graduates?

FALSE: We see the level coefficient is 35. If the person went to college, 
their level is 1, thus the coefficient of 35 applies. If not it's always 0
so the coefficient does not apply.

True of false:  For a fixed value of IQ and GPA, college graduates earn
more, on average, than high school graduates.

