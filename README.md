# Enter python virtual env and install required packages

python -m venv venv
source venv/bin/activate

pip install numpy flake8 pandas matplotlib seaborn
alias norminette=flake8

# Exit virtual env

deactivate

# Definitions

Mean - La moyenne est la somme de toutes les valeurs divisée by le nombre de valeurs.
A utiliser quand les données sont symétriques et sans valeurs aberrantes, ou quand
on veut tenir compte de toutes les données.
Median - La médiane est la valeur qui se trouve au milieu d'un ensemble de données
classées par ordre croissant. Elle divise l'ensemble en deux parties égales.
A utiliser quand les données contiennent des valeurs extrêmes, ou quand on veut
connaître la valeur "typique" au centre.
Quartiles - Les quartiles divisent un ensemble de données ordonnées en quatre parties
égales de taille identique. Ils permettent de comprendre la distribution des données.
Q1 (Premier quartile ou quartile 25%):
25% des données sont inférieures ou égales à Q1
75% des données sont supérieures à Q1
Q2 - Median:
50% des données sont de chaque côté de cette valeur
Q3 (Troisième quartile ou quartile 75%):
75% des données sont inférieures ou égales à Q3
25% des données sont supérieures à Q3
Ils servent à comparer les performances (ex: étude de notes lors d'un examen), mais
aussi à détecter ce qui est normal ou exceptionnel: ce qui est très en-dessous de
Q1 ou très au-dessus de Q3 est inhabituel.
Variance - La variance mesure à quel point les valeurs d'un ensemble de données
s'écartent de la moyenne. Elle se calcule en faisant la moyenne des carrés des
écarts à la moyenne.
Standard deviation - la déviation standard ou écart type est simplement la
racine carrée de la variance. Elle a l'avantage d'être exprimée dans la même
unité que les données originales, ce qui la rend plus facile à interpréter.
Une variance/déviation standard faible indique que les données sont regroupées
près de la moyenne.
Une variance/déviation standard élevée indique que les données sont très dispersées.

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
