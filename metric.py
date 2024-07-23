#Main function for metrics' calculation

def outcome() :

    import pandas as pd
    import numpy as np
    import os
    import sys

    #os.chdir('C:/Projects/dev_test')
    #sys.path.append('C:/Projects')

    from constants import METRIC_WAGES_DICT

    from constants import (
        BENEFITS_DICT,
        CONTRACT_LENGTH_DICT,
        CONTRACT_TYPE_DICT,
        BRAND_RECOGNITION_DICT,
        RECRUITMENT_DIFFICULTY_DICT,
        SHIFTS_DICT,
        OVERTIME_DICT,
        EMPLOYEE_SATISFACTION_DICT
    )

    from functions import (
        import_json,
        filter_benchmark,
        benefits_to_one,
        contract_length_intervals,
        zero_to_hundred
    )

    #Importing the source dataset
    input_df = pd.read_excel('Datasets/large_dataset.xlsx')


    #Importing the filtering criterions
    filter_criterions = import_json('filters_input.json')

    #Importing the survey entry
    survey_entry = import_json('survey_input.json')

    #Transforming dictionary into a 1-row of dataframe
    survey_df = pd.DataFrame(
        data = survey_entry['job_order'].values(),
        index = survey_entry['job_order'].keys(),
        columns = ['Values']
        )

    benefits_list = list(survey_entry['job_order']['Benefits'].values())

    survey_df['Values'].loc['Benefits'] = benefits_to_one(benefits_list[0], benefits_list[1], benefits_list[2])

    survey_df = survey_df.transpose()

    #Filtering the source dataset for benchmark entries
    filter_df = filter_benchmark(input_df, filter_criterions)
    filter_df.rename(columns = {'Job_Type' : 'Job Type'}, inplace = True)

    #Adding survey input to benchmark dataframe and removing filtering columns (not needed in metrics formulas)
    #benchmark_df = filter_df.append(survey_df, ignore_index = True).drop(columns = ['Voivodship', 'Industry', 'Job Type','Fill_Rate'], axis = 1)
    benchmark_df = pd.concat([filter_df, survey_df], ignore_index = True).drop(columns = ['Voivodship', 'Industry', 'Job Type','Fill_Rate'], axis = 1)

    #
    for i in range(len(benchmark_df)) :
        benchmark_df['Contract Length'].loc[i] = contract_length_intervals(benchmark_df['Contract Length'].loc[i])

    mappings = [
        BENEFITS_DICT,
        CONTRACT_LENGTH_DICT,
        CONTRACT_TYPE_DICT,
        BRAND_RECOGNITION_DICT,
        RECRUITMENT_DIFFICULTY_DICT,
        SHIFTS_DICT,
        OVERTIME_DICT,
        EMPLOYEE_SATISFACTION_DICT
    ]

    categoricals = [
        'Benefits',
        'Contract Length',
        'Contract Type',
        'Brand Recognition',
        'Recruitment Difficulty',
        'Shifts',
        'Overtime',
        'Employee Satisfaction'
    ]

    # Transformation
    for cat, mapping in zip(categoricals, mappings):
        benchmark_df[cat] = benchmark_df[cat].map(mapping)

    columns = benchmark_df.columns

    for column in columns:
        min_val = benchmark_df[column].min()
        max_val = benchmark_df[column].max()
        benchmark_df[column] = benchmark_df[column].apply(lambda x: zero_to_hundred(min_val, max_val, x))

    # Multiply the values in the last row of the DataFrame by the corresponding values in METRIC_WAGES_DICT
    benchmark_df = round(benchmark_df, 2)
    product = round(benchmark_df.iloc[-1] * pd.Series(METRIC_WAGES_DICT), 2)
    metric = round(product.sum(), 2)
        
    benchmark_df = benchmark_df.iloc[-1].transpose()
    benchmark_df.index.name = "Feature"
    benchmark_df.columns = ["Scores"]
    metric = round(product.sum(), 2)
        
    return benchmark_df, metric, len(filter_df)


