# Enter python virtual env and install required packages

python -m venv venv
source venv/bin/activate

pip install numpy flake8 pandas matplotlib seaborn
alias norminette=flake8

# Exit virtual env

deactivate

# Subject

This project invites us to manipulate data and represent it in the shape of figures.
You will find several programs in the exercises directory. Each of them gives specific
insights on how data is spread.
We have a sample of 1600 students, with a corresponding Hogwarts Houses (there are 4 houses in total).
We also have information about each student, and access to the student's scores per course
(there are 12 courses in total).

# 1st program: describe

First, the program exercises/describe.py gives statistics for all students per house.
We have the number of student per house, and:

The standard deviation - a measure of the amount of variation or dispersion in a set
of values. It quantifies how much the values in a dataset deviate from the mean (average)
of the dataset. It is the squared value of the variance.

Minimum and maximum scores per house

Quartiles - dividing a dataset into four equal parts. Quartiles provide information
about the spread and distribution of data.
There are three main quartiles:
First Quartile (Q1): Also known as the lower quartile, it divides the lowest 25% of
the data from the rest
Second Quartile (Q2): This is the median of the dataset, dividing it into two halves.
Third Quartile (Q3): Also known as the upper quartile, it gives the value under which
we have 75% of data in ascending order.

Running this first program, we find out that Gryffindor has 75% of its students overall
scores above ~86000, vs ~54000 for Hufflepuff and Ravenclaw, and a low ~1800 for Slytherin.
Comparing houses' 1st quartile, we notice that 25% of students in Slytherin have a score
under ~ -35000, which is low compared to other houses. The median of the Slytherin house
is negative as compared with other houses' medians which are positive.
Gryffindor shows a median that is significantly lower then that of Hufflepuff and Ravenclaw,
despite 75% of students in this house have very high scores.
The minimum score of Hufflepuff is lower than that of Ravenclaw, and more significantly
of that of Slytherin and Gryffindor. The maximum score of Hufflepuff is also the highest.
The standard deviation of Gryffindor and Slytherin is relatively equal, unveiling
a comparable and relatively weak deviation of scores from the mean for each house, whereas
the dispertion of scores in Ravenclaw and Hufflepuff is higher, as the minimum and maximum
scores values tend to show.

# 2nd program: histogram

Running this program will output a figure that allows to answer the question:
Which Hogwarts course has a homogeneous score distribution between all four houses?
From resulting bars chart, we notice that the gap is the lowest for the course
n°10 (Care of Magical Creatures). We barely see some very small gaps among the 4
houses when changing the scale of scores with ylim set between -1000 and 1000.

# 3rd program: scatter plot

Here we have the 13 courses and a representation of the dispertion of scores,
which are normalized to stand between -1 and 1. It is quite difficult to identify
two similar features.
A pairplot would give a clearer picture of features, and which of those features
would be determinant when assessing which house the student would go in.

# 4th program: pair plot (colored scatter plot matrix)

From the matrix we can see scatter plots showing in which area are located
the scores of the 4 Hogwarts Houses.
It is quite clear in wich course the various houses tend to show upper or
lower scores. For instance, we can see that Gryffindor students are good
at flying as compared to all other houses.
When we look at the curves in the diagonal, we can also see that there is a
very small area shared between the blue curve and all other curves,
which means flying would be a differantiating feature.
By contrast, Gryffindor shows weak scores in courses Transfiguration and
Hisory of Magic. Finally, the diagonal curves for Divination show that
Divination is a differentiating feature, where low scores are associated to Slytherin.

# 5th and 6th programs: train model and predict

There are 2 programs. The first one - logreg_train - searches for the
minimum squared error from a linear regression perspective, and doing so,
computes an array of thetas as weights and a single theta as bias.
The program writes thetas' values in a csv file, so they can be used
by the prediction program.
Logreg_predict uses linear regression equation y = wx + b and it makes
a sigmoid function out of it. The sigmoid function is a mathematical function
that maps any real-valued number to a value between 0 and 1.
It is defined by the formula 1 / 1 + e \*\* -z where z = wx + b.
When z is positive the result approaches 1, whereas when it is negative,
the result approaches 0.
For each of the students from the dataset "test", we compute a probability
between 0 and 0.5 based on the 13 scores (normalized scores: between -1 and 1)
multiplied by the corresponding 13 weights (13 computed weights for
each of the 4 houses), and we add the bias. Doing so we get a (400, 4)
dataframe of predictions.
Then, we get the highest prediction value at a specific index and we associate
the corresponding house to the student.
The pairplot output from the test dataset shows same trends as the pairplot
output from the train dataset.
