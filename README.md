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
The second part is about making predictions based on what we have learned from a given model.
We have a sample of 1600 students, with a corresponding Hogwarts Houses (there are 4 houses in total).
We also have information about each student, and access to the student's scores per course
(there are 13 courses in total).
From the training dataset, we must infer 13 x 4 coefficients and 4 biais,
which will be used to predict categories for the test dataset (i.e. corresponding house for each student).

# Train model & Predict

There are 2 programs. The first one - logreg_train - searches for the
minimum squared error from a linear regression perspective, and doing so,
computes an array of thetas as weights and 4 thetas as bias.
The program writes thetas' values in a csv file, so they can be used
by the prediction program.
Logreg_predict uses linear regression equation y = wx + b and it makes
a sigmoid function out of it. The sigmoid function is a mathematical function
that maps any real-valued number to a value between 0 and 1.
It is defined by the formula 1 / 1 + e \*\* -z where z = wx + b.
When z is positive the result approaches 1, whereas when it is negative,
the result approaches 0.
For each of the students from the dataset "test", we compute a probability
between 0 and 1 based on the 13 scores (normalized scores: between -1 and 1)
multiplied by the corresponding 13 weights (13 computed weights for
each of the 4 houses), and we add the bias for each house.
Doing so we get a (400, 4) dataframe of predictions.
Then, we get the highest prediction value at a specific index and we associate
the corresponding house to the student.
The pairplot output from the test dataset shows same trends as the pairplot
output from the train dataset.
There is also a s-curve showing when z is negative, y-value is close to 0,
whereas when z is positive, y-value is close to 1.
