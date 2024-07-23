#This file stores functions used in the application

def import_json(path) :
    """
    Imports json files and saves them as python dictionaries

    Arguments:
    -> path of the json file
    
    Returns:
    A python dictionary
    """
    import json
    
    json_file = path
    with open(json_file, 'r', encoding = 'utf-8') as data_entry:
        converted_data_entry = json.load(data_entry)
        
    return converted_data_entry


def filter_benchmark(dataset, filter_crits) :
    
    """
    Filters out the subset of data dedicated for benchmark purposes.
    Filtering criterions are determined by user in a survey and stored as a JSON file.
    
    Arguments :
    -> dataset (DataFrame) : a pandas DataFrame storing data from large_dataset.xlsx.
    -> filter_crits (dict) : a python dictionary derived from a JSON file dict [str, str, str, float, float]
    
    Returns:
    DataFrame : a pandas dataframe with filtered
    """
    
    dataset = dataset.copy()
    
    voivodship = filter_crits['filters']['Voivodship']
    industry = filter_crits['filters']['Industry']
    job_type = filter_crits['filters']['Job Type']
    lower_bound = filter_crits['filters']['Fill_Rate_lower_bound']
    upper_bound = filter_crits['filters']['Fill_Rate_upper_bound']
    
    filtered_dataset = dataset.query('\
                    Voivodship == @voivodship and \
                    Industry == @industry and \
                    Job_Type == @job_type and \
                    Fill_Rate > @lower_bound and Fill_Rate < @upper_bound \
                    ')
    
    return filtered_dataset
    

def zero_to_hundred(min_val, max_val, value):
    """
    Performs Min-Max scaling (next multipled by 100) on a single column and transforms the values to the [0, 100] interval.
    
    Arguments:
    column (Series): A pandas Series representing a single numerical feature.
    
    Returns:
    Series: A new Series with scaled values.
    """
    if min_val == max_val:
        scaled_value = 100
        return scaled_value
    else:
        scaled_value = ((value - min_val) / (max_val - min_val)) * 100
        return scaled_value


def benefits_to_one(paid_meals, sport_card, medical_care) :
    """
    Transforms 3 binary features into one categorical.
    
    Arguments : 
    3 binary values
    
    Returns : 
    1 categorical value
    """
    
    benefit = None
    
    #Possible benefits' combinations
    if (paid_meals == 0 and sport_card == 0 and medical_care == 0):
        benefit = 'No benefits'
        
    elif (paid_meals == 1 and sport_card == 0 and medical_care == 0):
        benefit = 'One benefit'
    elif (paid_meals == 0 and sport_card == 1 and medical_care == 0):
        benefit = 'One benefit'
    elif (paid_meals == 0 and sport_card == 0 and medical_care == 1):
        benefit = 'One benefit'
        
    elif (paid_meals == 1 and sport_card == 1 and medical_care == 0):
        benefit = 'Two benefits'
    elif (sport_card == 1 and paid_meals == 0 and medical_care == 1):
        benefit = 'Two benefits'
    elif (medical_care == 0 and paid_meals == 1 and sport_card == 1):
        benefit = 'Two benefits'
        
    elif (paid_meals == 1 and sport_card == 1 and medical_care == 1):
        benefit = 'All benefits'
    
    return benefit


def contract_length_intervals(contract_length) :
    """
    Maps a discrete value (or a string, in case of 'Indefinite' value) to a categorical label

    Arguments :
    discrete or string
    
    Returns :
    categorical label
    """
    if contract_length == 'Indefinite' :
        contract_length = 25
    
    contract_length = int(contract_length)
    
    interval = None
    
    if contract_length <= 6 :
        interval = 'up to 6 months'
    elif contract_length <= 12 :
        interval = 'more than 6 and up to 12 months'
    elif contract_length <= 24 :
        interval = 'more than 12 and up to 24 months'
    else :
        interval = 'more than 24 months or indefinite'
        
    return interval
