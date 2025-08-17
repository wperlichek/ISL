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





