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
Gryffindor shows a median that is significantly lower then that of Hufflepuff and Ravenclaw.
The 4 houses' standard deviation is relatively equal, unveiling a comparable deviation
of scores from the mean for each house.

# 2nd program: histogram

Running this program will output a figure that allows to answer the question:
Which Hogwarts course has a homogeneous score distribution between all four houses?
From resulting bars chart, we notice that the gap is the lowest for the course
n°10 (Care of Magical Creatures). We barely see some very small gaps among the 4
houses when changing the scale of scores with ylim set between -1000 and 1000.

# 3rd program: scatter plot

There is no surprise here as we have Slytherin with the lowest overall scores.
The spread - std deviation - is comparable among the four houses.

# 4th program: pair plot (colored scatter plot matrix)

From the figures we can see that the red curve (Hufflepuff) tends to be high.
Ravenclaw (gray) also has a high curve for all courses.
The green curve (Slytherin) tends to be the smallest, smaller than the blue curve (Gryffindor).
Indeed, we saw that the median of scores for Hufflepuff and Ravenclaw students
are higher than that of Gryffindor, and the median for Gryffindor is significantly higher
than that of Slytherin.
