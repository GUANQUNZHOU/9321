# 9321-ass3
Our assignment uses Flask for the backend. To start our assignment run the following in terminal
```shell
python3 a3.py 
```
Then accessing it via a web browser via the link http://127.0.0.1/8332 (8332 might not be neccessary depending on the computer

## File Structure
```bash
.
├── a3.py                           # The backend of our website (paths to different HTML pages)
├── processed.cleveland.data        # Given data set
│   ├── templates                   # HTML files
│   ├── static                      # CSS and Images
├── read.py                         # Generation of graphs by age and sex for part 1
├── feature_selection.py            # The various algorithms for selecting features in part 2
├── q3.py                           # Our training model and logistic regression algorithm for part 3
└── bonus_part.py                   # Clustering of all 11 attributes by target for bonus part
```

## Web Page Structure
The front page contains a summary of what we have done and the general way we approached the three parts. To reach the specific parts
of each page, check out the part 1, part 2 and part 3 tabs on the top right.

#### Part 1
We have made a graph of all 11 attributes, grouped by age and sex. We have decided to use different types of charts
depending on the type of data the attribute contains. To view each of the graphs, with a description for each one please click on each of the
boxes. 

Specifically in [read.py](read.py). The functions
``` python
def generate_dictionary_ST(df, attributes, name)
def generate_dictionary(df, attributes, name)
def plot_dictionary(d, name,attributes)
```
are the main functions used in creating a graph segregated by age and sex by creating separate dataframes for each combination
of age and sex.

#### Part 2
We have displayed the ranking of attributes based on several different methods. The tables shows the ranking in order of how closely
related the attribute is to the target attribute.

Specifically in [feature_selection.py](feature_selection.py). The functions
``` python
def univariate(df1_clean)
```
Contains the core logic of our chi squared method on our given data set. This gives a list of rankings in the end which we display
via a table.

#### Part 3
A form is presented which allows the user to enter 13 attributes. When the form is sent it goes to a3.py. 
In which we get the data from the user in the form of a dictionary. We also grab the list generated from feature selection
for the rankings of each attribute. With both the ranking list of attributes and dictionary of input values we run the following
functions

[q3.py](q3.py)
``` python
 def accuracy_selection(rankings):
```
This is where we train our model. So in this logic we trained our dataset for 2 features first and incremented each try. In each increment
we applied. We applied cross validation when training the model (as seen by sklearn.cross()))
```python
def log_reg(data, label, inputs=False)
```
in order to get the accuracy results for each subsequence of features. This is used to generate the accuracy graph that is shown
after clicking the predict button.

Finally we apply
```python3
def predict(rankings,inputs)
```
Where predict will use logmodel.predict() on our dictionary of data from the user to predict the likelihood of heart disease which is displayed on the same page as the graph.

#### Bonus
In our bonus part we display our cluster. The logic for our clustering can be found in 
[bonus_part](bonus_part.py). This is where we applied k means for our clustering. Then we applied PCA to reduce the dimensions of our data to two. So that we are able to produce a visualisation.



