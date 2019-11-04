from gplearn.genetic import SymbolicClassifier
# Last revised in 1991
with open(r"breast-cancer-wisconsin.data") as classifier_file:
    classifier_data = classifier_file.readlines()

# Variation of inputs sourced for breast cancer detection
attributes = ["Clump Thickness", "Uniformity of Cell Size",
              "Uniformity of Cell Shape", "Marginal Adhesion",
              "Single Epithelial Cell Size", "Bare Nuclei",
              "Bland Chromatin", "Normal Nucleoli", "Mitoses"]
values = []
benign = []
count = 1
# Reads all values from the given dataset
for line in classifier_data:
    # Comma separated file
    data = line.split(',')

    # row is a one dimensional array that represents one persons data
    row = []
    # Nine different attributes to be read
    for i in range(1, 10):
        # Missing attributes are replaced with -1
        x = int(data[i]) if data[i] != "?" else -1
        # Add data values to the temporary array after accounting for missing information
        row.append(x)

    values.append(row)
    # As according to the documentation if the last value is a 2 then the person is known to have a benign tumor
    if int(data[10]) == 2:
        # Not cancerous
        benign.append("benign")
    else:
        # Is cancerous
        benign.append("malignant")


classifier = SymbolicClassifier(
    # Prevents 'bloat' used for large programs when evolution is increasing the size of the program with an
    # insignificant increase in fitness
    parsimony_coefficient=.01,
    # The list of attributes names, used in producing the final equation
    feature_names=attributes,
    # Displays each evolutionary state and fitness after each tournament is run
    # Note: If commented the user will need to be patient before final results are displayed
    verbose=1,
    # Stops the program early if the criteria is met. This is to prevent long computation time for minimal gain
    stopping_criteria=0.15,
    # When the population is 500 = ~85% 1000 = ~90% 2000 = ~95%
    population_size=2000,
    # basic functions are all that is required the inclusion of log functions provides roughly 5% increase in fitness
    function_set={"mul", "div", "add", "sub", "log"}
    )

# The first 400 values in the file are trained and tested against the first 400 known values to be benign
classifier.fit(values[:400], benign[:400])
# Returns the accuracy as a percentage from the fitness function
print("Accuracy: " + (classifier.score(values[:400], benign[:400])*100).__str__() + "%")
# Returns the function that achieves the above fitness to be entered into a tree in a breadth first fashion
print("Function: " + str(classifier._program))
