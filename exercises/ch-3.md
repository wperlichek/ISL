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

**5**

5. Consider the fitted values that result from performing linear regression without an intercept. In this setting, the *i*-th fitted value takes the form
$$
\hat{y}_i = x_i \hat{\beta},
$$
where
$$
\hat{\beta} = \left( \sum_{i=1}^{n} x_i y_i \right) \bigg/ \left( \sum_{i'=1}^{n} x_{i'}^2 \right). \quad (3.38)
$$
Show that we can write
$$
\hat{y}_i = \sum_{i'=1}^{n} a_{i'} y_{i'}.
$$
What is $a_{i'}$?

*Note: We interpret this result by saying that the fitted values from linear regression are linear combinations of the response values.*

#### 1. Model Definition

The analysis starts with the model for linear regression without an intercept, where the fitted value `ŷ_i` is a direct product of the predictor `x_i` and the estimated coefficient `B_hat`.

* **Fitted Value (`ŷ_i`):**
    ```
    ŷ_i = x_i * B̂
    ```

* **Estimated Coefficient (`B̂`):**
    ```
    B̂ = (Σᵢ xᵢyᵢ) / (Σᵢ xᵢ²)
    ```

---

#### 2. Numerical Example

A specific example with `n=3` data points `(1,2), (2,3), (3,4)` was used to calculate `B̂`.

* **Calculate the sum of `xᵢyᵢ`:**
    ```
    Σᵢ xᵢyᵢ = (1 * 2) + (2 * 3) + (3 * 4)
           = 2 + 6 + 12
           = 20
    ```

* **Calculate the sum of `xᵢ²`:**
    ```
    Σᵢ xᵢ² = 1² + 2² + 3²
           = 1 + 4 + 9
           = 14
    ```

* **Solve for `B̂`:**
    ```
    B̂ = 20 / 14 ≈ 1.43
    ```

---

#### 3. Calculating a Fitted Value

Using the calculated `B̂`, a fitted value was predicted for a given `x`.

* **For `x = 4`:**
    ```
    ŷ = (4) * (1.43)
    ŷ = 5.72
    ```

---

#### 4. Exploring the General Form

The final part of the notes connects this process to the problem's goal: showing that the fitted value `ŷ_i` is a linear combination of the response values `yᵢ'`.

* **Target Form:**
    ```
    ŷᵢ = Σᵢ' aᵢ'yᵢ'
    ```
* **Question:** What is `aᵢ'`?

$$
a_{i'} = \frac{x_i x_{i'}}{\sum_{k=1}^{n} x_k^2}
$$

Of course. Here is a summary of the key takeaways from a linear algebra perspective.

### Summary: The Linear Algebra of Simple Regression

In simple linear regression without an intercept, we are working with three main vectors, each having `n` dimensions (one for each data point):

* **`y`**: The vector of actual, observed outcome values.  
    `y = (y₁, y₂, ..., yₙ)`

* **`x`**: The vector of predictor values.  
    `x = (x₁, x₂, ..., xₙ)`

* **`ŷ`**: The vector of our model's fitted (predicted) values.  
    `ŷ = (ŷ₁, ŷ₂, ..., ŷₙ)`

Here's what we learned about their relationship:

1.  **The Predictor Vector `x` Defines a Subspace:** All possible scalar multiples of the vector `x` form a line through the origin in n-dimensional space. This line is a one-dimensional subspace. Any vector that is a prediction of our model *must* lie on this line.

2.  **The Fitted Vector `ŷ` is a Projection:** The vector of actual outcomes, `y`, is a point somewhere in that n-dimensional space, and it almost certainly does not lie on the line defined by `x`. The goal of linear regression is to find the point on that line that is **closest** to our actual `y` vector. This closest point is the **orthogonal projection** of `y` onto the line spanned by `x`. This projection is our fitted vector, `ŷ`.

3.  **`ŷ` is a Linear Combination of `y`:** As you proved with the formula for `aᵢ'`, the calculation of this projection means that our final `ŷ` vector is a linear combination (a weighted sum) of the original `y` values. The weights (`aᵢ'`) ensure that the resulting vector lies perfectly on the line defined by `x`.

4.  **`ŷ` is Collinear with `x`:** Because `ŷ` lies on the line spanned by `x`, it must be a scalar multiple of `x`. This is the geometric meaning of the first equation you started with: `ŷ = β̂x`. The coefficient `β̂` is simply the scalar that stretches or shrinks the `x` vector to become the `ŷ` vector that is closest to `y`.

In short, linear regression takes your data vector `y` and finds its "shadow" (`ŷ`) on the "line" (`x`) defined by your predictor variable. This geometric view explains *why* the model is structured the way it is and reveals the fundamental constraints on its predictions.


Yes, that is **exactly** it.

You've just connected the specific application you worked on with its general mathematical name. This is a perfect link.

Let me break down the connection between your two statements:

1.  **"The problem I worked on was data fitting to the model..."**

    This is the **problem** or the **application**. Your goal was to find the best possible `β̂` so that the model's predictions (`ŷ = β̂x`) were as close as possible to the actual data (`y`). You were "fitting" the model to the data.

2.  **"So this is least squares?"**

    This is the **method** used to solve that problem. To find the "best fit," we need a mathematical definition for "best." The least squares method defines the best fit as the one that **minimizes the sum of the squared differences** between the actual values (`yᵢ`) and the fitted values (`ŷᵢ`).

    `Minimize: Σ(yᵢ - ŷᵢ)²`


This is least squares: https://textbooks.math.gatech.edu/ila/least-squares.html

The beautiful connection that you have been exploring is this:

* The **algebraic** process of minimizing that sum of squares is perfectly equivalent to the **geometric** process of finding the orthogonal projection of the vector **y** onto the subspace spanned by the vector **x**.

The link you found discusses the general problem from the linear algebra side: how to find the "least squares solution" to an inconsistent system of equations `Ax = b` (where there's no perfect solution). Their `b` is your `y`, and their `A` is your `x`. The solution is to find the projection of `b` onto the column space of `A`.

So, you are absolutely correct. The problem you worked on was an example of data fitting, and the fundamental mathematical engine you used to solve it—whether you view it as minimizing squared errors or as projecting vectors—is called the **method of least squares**.


Transcript notes from linear algebra: 

Hello everyone, and welcome to our lecture on the
lease squares problem. This is also related to
data fitting as we'll see. Remember where we were before. Last time, if I had a
matrix equation Ax = b, one or two things could happen. Either it was
consistent and we found an x that solved for
that mapped over to b, or it was inconsistent. Now, what happened if this matrix equation
was inconsistent? Well, we really didn't have much to do, so it was a full stop. We moved on and
said there's no x. Let's think about what this means in terms of the pictures. Now, we have some R^n and then A remember is the linear
transformation and maps to some other R^m. I'll just keep drawing
three space because I can. What's happening in
the inconsistent case is we have some subspace, that's our image, the image
of the transformation, and then we have some
vector x that's off of it. We have some vector B that
lies off of the image. All the x is in the domain
get mapped onto the image, and that's why nothing
gets mapped onto the b. This b here is not in the
image of our transformation. The matrix equation
would be inconsistent. But now we'd like
to do something more than just stop
and walk away. Our goal now is to find the x in the domain so that A of
x, the output vector, the one that lives in the
image somewhere down here, is the best approximation
to the given vector b. Now, of course, this
is all code for what, when we say best approximation, we really want the one that is the shortest distance to our vector b. Hopefully you can
see where this is going, and that's equivalent
to saying what? That the distance between the given vector b
and the vector Ax, remember that's the magnitude
of their difference, that this is minimized. Now, this is the
problem at hand. Find the x in the
domain that maps over inside of the image to Ax, but such that the distance
between the two is minimized, find that x in the domain. This is called the
least square problem. The vector x that minimizes this distance between the
given vector b and Ax, the output, is the
least squares solution. It's given a symbol. It's denoted,
depending on the book or choice you use as x*, or I've even seen x-hat. The hat, of course,
is a foreshadow of what's to come because clearly we're going
to use orthogonal projections onto the image here. That's what we want
to do next to come up with a formula or way to do this to find the
least squares solution. Let's do it. Let's actually
find this vector x. We'll call it x*. Given some matrix A, we'll say it's m*n, and we'll multiply it
against given vector b. We get both these two things. Are you ready? Again, Think of the picture.
What's going on here? We have a domain,
we have the map A, we have the co-domain,
we have the image, the output of this function, and we'll consider b
to live outside of the image so the matrix equation
Ax = b is inconsistent. Well, then what are
we going to do? We're going to let b-hat be the orthogonal projection
onto the image of A, of the vector b. In terms of pictures,
we take the shadow, we map it orthogonally down, and we have this b-hat. This is the projection
vector, and of course, it lives inside the
image, and therefore, since b-hat is inside
the image of A, the matrix equation of Ax =
b-hat is always consistent. What does that mean? Therefore, there
exists some vector, we're going to call it x-hat, inside of R^n inside the
domain with Ax-hat = b-hat. Also x-hat is doing its thing, it's somewhere
inside the domain, and this x-hat gets
mapped to b-hat. Remember this x-hat
is what we're calling the least
square solution. As another note, maybe it's unique or maybe
there's more than one. Maybe an entire line gets
mapped over to b-hat. We don't know this yet,
but there's some solution. There's at least one
vector that we can find. We know it exists.
Now, let's find it. The key observation
here is to note that b-Ax-hat is orthogonal
to the image of A. By construction, this
is at a right angle. It's dot product is zero. Therefore, remember,
the image of A is the span of the columns of A. Therefore, for any column, we'll say aj over our matrix A. Because they are orthogonal, aj. (b-Ax-hat) must equal 0. That's what it means
to be orthogonal. Let's rewrite this product as a matrix product so
we can work with it. Therefore, aj-transpose times
(b-Ax-hat) must equal 0. This is true for any column j, and I remember aj, the column of A^T. Well, this is a row of A^T. Therefore, since it's true for any column or any
row of a transpose, A^T*B- axz must be equal to 0. Let's distribute the A^Tz to get A^Tb- A^Tx hat equals zero. Last but not least, move
the right side over to get A^Tb is equal to A^Ta*x hat. This relationship between
A^T is the given vector B, helps us find this x hat. Remember, the goal is to
find x hat. Call it x star. Of course, to mix
up the notation. But the goal is to find
this least square solution. This equation is so important, it has a name and this is
called the normal equations. We'll say it's for Ax equal B. Because remember, A and
B here are always given. If you know A and you know B, you can find A^T, you can multiply it against B, and you can certainly find A^T. We'll do an example
a little bit later. Let's put this result down. Let's summarize the
result from last slide. This is actually a theorem
and it says the following, putting it all together here, the set of least square
solutions of Ax equals B, coincides with the non empty is always consistent solutions. There may be one, there
may be more than one of the normal equations given by A^T A(x) equals A^Tb. These formulas they look
a little scary at first, but let's go over
some easy cases, some special cases.
We'll say they're easy. The first case I
want to consider is, if Ax equals b, is
actually consistent. Remember, sometimes it's
consistent, sometimes it's not. All this theory applies in both. It's more interesting when it's inconsistent,
you get to say more. But what if like Ax equals b,
what does it actually mean? Well, of course that means that, b is actually inside
the image of A. In our picture, when I draw x on the left and I map it over, and I draw the image space of A, I used to draw a
b off the image. But now, it's some
vector inside there. Remember what the least
square solution is, it's the vector in the domain, the vector on the left that gets mapped to the
closest vector in B. Normally, it's the projection
of b under the image. But here, since B
is in the image, the projection is itself. In particular, if
it's consistent, the vector x, again, there might be more than one, is the least square solution. Hopefully, you see
that from a picture. Now, let's look at
the normal equation to actually see that. I start off with A^T
Ax is equal to A^Tb. But remember, we can
say something here about Ax equals to b,
this is consistent. I get A^T*b is equal to A^T*b. Of course that's true, but not very interesting. Again, in this one we wouldn't use these normal equations. They don't contradict anything, the normal equations are
certainly true in this case. But if it's consistent, we don't really use
the normal equations. We solve it using the ways that we've seen
prior in this course. But special case when
these formulas break down and they are a
little less scary. There's another
case though, that happens that's a little
more interesting. This happens if A^TA is
actually invertible. Now, let's talk about
this for a second. If A is n*m, nothing that requires
A to be a square. But it's transpose is reversed. That would mean that A^T is m*n. The product is
certainly defined. The two inside numbers match and notice what you get back. You get a nice square matrix, m*n. Therefore, we can
talk about invertibility. It's possible that this matrix is square matrix is invertible. In that case, let's rewrite
the normal equations. We have A^TAx equals A^T*b. What's an option that we can use when the matrix
is invertible? Well, we of course, can
multiply by the inverse. This gives you an
immediate formula for x. We multiply and left
by the inverse and we get A^TA inverse times A^Tb. You say this is gross, but you can calculate
all these things. You can calculate A^T, you can multiply it by b, you can calculate A^T*A, find its inverse,
multiply them together. This is a nice special case where I get an
immediate formula. Notice here in this
case, x is unique. The least square
solution is unique. One more super special case, it doesn't happen too
often but it could happen. What if the columns
of A are orthonormal? Well in that case as a reminder, one of the formulas
that we have is that A transpose A is the identity. This is true for any matrix
that has orthonormal columns. I don't know that A is square, I can't say that it's
an orthogonal matrix but if the columns
are orthonormal, then remember A
transpose A is I. When I write out the
normal equations, A transpose A*X= A transpose B. The first part just becomes the identity, what
am I left with? I get a much simpler, easier calculation than
the least square solution. The solution of my
normal equation is just A transpose times B. One matrix times a vector that's the easiest possible case,
of course it is not. I don't want to say normal because that word
is being over used. But of course, it's
not likely that the columns of A
will be orthonormal, but if they are, catch it, save yourself a lot of work
you can go right to this. The one that you're going
to see the most here. The one, the shortcut that we're going to look
for the most here, is when A transpose A, this nice square matrix
is in fact invertible, then I have a direct
formula using the normal equations to solve for my least square solution. It turns out it's a theorem,
and I'll use this again, TFAE, remember in math that means the
following are equivalent. We're going to find
out exactly when A transpose A is
invertible, A transpose A, nice square matrix,
even though A may not be if that's okay, here's when it's invertable. Turns out that A
transpose A is invertible when Ax equals B has a unique least
square solution for all B inside of RM and we saw that formula
on the last slide. Here just so I can
define things, let's let A be M by N. Two this is the one
we're going to use here columns of A are linearly independent that's
of course equivalent to saying that there's a pivot in every column of A we've seen
that relationship before. Now, a pivot in every
column of A well, that's equivalent to saying
that the kernel of A or the null space of A is
just the zero vector. The only solution Ax
equals zero is zero. Any one of these together imply that A transpose
A is invertible. This gives us a check to say, which form should we use before we look at the
normal equations? Just one thing to note here. Let's let W be the
span of V1 dot VM, we'll let this be a
basis inside of RN. We take A to be the matrix
with V1...VM as its columns. What do we know then? The
least square solution. Now remember these form
a basis V1 through VM. The columns are
linearly independent, so we know that there's
a unique solution. The least square solution
is given by the formula. We'll say X hat equals A transpose A inverse times A
transpose B after rewriting the normal equations
so what does this tell us remember
what the goal was here X hat lives in the domain and it was mapped to the
projection vector of B. We can put this all
together and say that the projection onto W of my vector B is
given by AX hat. But this of course
now is A times A transpose inverse
A transpose of B. This relates to
the projection of any vector B onto subspace W, where A is the matrix whose columns are the
basis vectors of. What this gives us is
another formula for the orthogonal projection
onto W. We can think of this as a map of T of any X over by A parentheses A transpose
A inverse A transpose. And all of this would
then be times X. Once again, we're seeing that the orthogonal projection has another decomposition here using the basis vectors of
W. What we saw though, with a lot of work, is we don't
work with just any basis. We tend to work with what? An orthonormal basis. Let's pretend for a second, we put in all the work we do, Ram Schmidt, if needed. If this basis is an
orthonormal basis, we have this nasty formula
here for the projection. But if it's an
orthonormal basis, what do we know about this? Well, then I know that a is A matrix whose columns
are orthonormal. Well, here it is again, that
property of those kind of matrices says that
A transpose A is just the identity
and you get back the simplified version for
the orthogonal projection. Here we're just projecting
any vector x onto the subspace W. This is
a linear transformation, but this entire middle term goes away and you
just get back A, A transpose x, which
we have seen before. That was the decomposition of the matrix for the
orthogonal projection. Again, you can see
why we like to work with orthonormal bases. They just make all our
nasty formulas a little bit simpler. Enough theory. Let's do an example
and we'll give you a specific A and a specific B. Let's find please. The least square solution
of the inconsistent system. I'm telling you
it's inconsistent, you can believe me
or you can check it but if you want, just check. Here, I'm going to have A via
nice three by two matrix. The first column is 4,0,1 and the second column
will be 0,2,1. The given vector B here
is going to be 2,0,1. Remember the fallback here is we're always going to
use the normal equations. A transpose A times x is
equal to A transpose b. Before we start going around
and just plugging these in, let's do some quick
simple checks. Just things to ask
ourself are we in the special case,
the nice case? The first check we
ask ourselves is one, does A have orthonormal columns? Remember, if that's the case, then A transpose A
becomes the identity, and this gets quite nice. But you can see very quickly, A does not have orthonormal
columns at all. Take the dot product here. You do get one,
but unfortunately, they're not normalized,
so I can't do that. The other check, of course, you'd ask yourself, is Ax
equal to b consistent? I told you in the
problem that it's not. Again, if I'm asking
you for least squares, this is usually almost too
easy a question to get asked so it'll almost
always be inconsistent. But hey, let's think about it. Then the other one you
want to ask yourself, is A transpose A invertible? Not every matrix is,
but maybe it is, and I can use the normal
equations and move it over. I have a theorem for that. That tells me it's invertible if the columns are
linearly independent. Hopefully you can look
at these two columns and see immediately that they're not scalar multiples of each
other and so that's a yes. What we're going to do now is we're going to
use the formula, move some things around here so my least square solution is going to be A
transpose A inverse, so move the whole left side
over times A transpose of b. This is the formula
that I'm going to use. I'm going to get one single
unique vector back and now it's just a matter of
plugging and chugging to get the matrices that I want. I know what A is,
so let's go get A transpose. A transpose says turn the
matrix on its side. The rows become the
columns 4,0 0,2 1,1. I would multiply this by
A to get A transpose A 4,0,1 0,2,1 times the
columns 4,0,1 0,2,1. You can work this
out, but just notice the size of the matrix
that we get back here. This matrix here
is two by three, a transpose and then A is
of course, three by two. I'm expecting a nice small two by two matrix back.
You can check. You get 17, 1 is the first row and then 1 and 5
as the second row. Nice two by two small matrix. What else do I need
for my formula? I need the inverse
now of A transpose A. Again, that actually work
through is not too bad. We have a formula for the
inverse of a two by two matrix. As a reminder, what is that? It is the determinant or one over the
determinant, I should say. You can check the
determinant turns out to be 84 so I get 1/84. As a reminder, you
switch the diagonal, so you put 5 and 17
are opposite spots and then let's negate -1 and -1. That's my entire left side here. I still need A transpose *B, so maybe I'll go off on
the side here and do that. A transpose we have
already worked out, and if you multiply it by B, you can check you should get back a different vector here. This just turns out to
be the Vector 19 and 11. My final least square
solution here, just a big plug and chug. The theory is actually
more interesting, at least in my opinion,
than the computation. But you have A transpose
A inverse times A transpose times b work
that all out, you get 1/84. 5, -1, -1,17*19,11. I'll spare you the work
here, but it turns out to be the vector 1,2. Again, remember what we found. This vector 1,2 in the domain is the vector that when
it gets mapped over, is the closest vector
inside of our three, the given vector B2,0,1. We call this our least
square solution. It's nice. It allows us to say
just a little more when the matrix equation, x=b is inconsistent,
which we like. This has great applications
to curves of best fit, to multilinear regressions,
and of course, data analysis. In general, I'll let those other courses
handle it there. But here I want to
introduce you to the theory and the
computations that go on when solving the
normal equations to find the least
square solution. Great job in this video.
I'll see you next time.


### The conceptual bridge (review)

### Conceptual Bridge: From a Formula to a Geometric Framework

The formula derived for $a_{i'}$ is not just an algebraic trick; it is the component-wise result of a powerful geometric process from linear algebra. This framework provides the deep intuition for the method of least squares.

We view our data as three vectors in an *n*-dimensional space ($ℝ^n$):

* **`y`**: The vector of actual, observed outcomes.
* **`x`**: The vector of predictor values.
* **`ŷ`**: The vector of our model's fitted (predicted) values.

The connection between the algebra and the geometry can be understood in these key steps:

1.  **The Predictor Vector `x` Defines a Subspace:** All possible scalar multiples of the vector `x` form a line through the origin. This line represents the entire universe of possible predictions for our model. Any valid prediction vector *must* lie on this line.

2.  **The Fitted Vector `ŷ` is a Projection:** The actual data vector `y` is a point in space that is likely not on the predictor's line. The core idea of **least squares** is to find the point on that line that is **closest** to our actual `y` vector. This closest point is the **orthogonal projection** of `y` onto the line spanned by `x`. This projection *is* our vector of fitted values, `ŷ`.

3.  **The `aᵢ'` Formula is the Projection in Action:** The formula you derived, $\hat{y}_i = \sum_{i'=1}^{n} a_{i'} y_{i'}$, shows exactly how to calculate this projection. It expresses each component of the fitted vector `ŷ` as a weighted sum (a linear combination) of the components of the original vector `y`. The weights, $a_{i'}$, are precisely structured to ensure the resulting vector `ŷ` lands perfectly on the line defined by `x`.

4.  **The Coefficient `β̂` is the Scaling Factor:** The simple model equation, `ŷ = β̂x`, confirms the geometric result. It states that the fitted vector `ŷ` is just a scaled version of the predictor vector `x` (they are collinear). The coefficient `β̂` is the specific scalar that stretches or shrinks `x` to become the correct projection.

In short, the statistical problem of **data fitting** is solved by the **method of least squares**, which is geometrically understood as the **orthogonal projection** of the outcome vector `y` onto the subspace defined by the predictor vector `x`.




