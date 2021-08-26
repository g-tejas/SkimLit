def get_lines(filename):
    """
    Reads filename (a text file) and returns the lines of text as a list.

    Args:
        filename: a string containing the target filepath to read.

    Returns:
        A list of strings with one string per line from the target filename.
        For example:
        ["this is the first line of filename",
        "this is the second line of filename",
        "..."]
    """
    with open(filename, "r") as f:
        return f.readlines()


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def calculate_results(y_true, y_pred):
    '''
    Calculates model accuracy, precision, recall, f1 score of a binary classification model

    Args:
        y_true: true labels in the form of a 1D array
        y_pred: predicted labels in the form of a 1D array
        
    Returns:
        A dictionary of metrics (accuracy, precison, f1, recall)
    '''
    # Calculate the model accuracy
    model_accuracy = accuracy_score(y_true, y_pred) * 100
    
    # Calculate the model precision, recall and f1 score
    model_precision = precision_score(y_true, y_pred, average='weighted')
    model_recall = recall_score(y_true, y_pred, average='weighted')
    model_f1 = f1_score(y_true, y_pred, average='weighted')
    
    # Store the results in a dictionary
    model_results = {
        "accuracy": model_accuracy,
        "precision": model_precision,
        "recall": model_recall,
        "f1": model_f1
    }

    return model_results