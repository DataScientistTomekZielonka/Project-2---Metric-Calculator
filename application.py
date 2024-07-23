import streamlit as st
import json
import pandas as pd
from constants import (
                       VOIVODSHIP_LIST,
                       INDUSTRY_LIST,
                       JOB_TYPE_LIST,
                       CONTRACT_TYPE_DICT,
                       SHIFTS_DICT,
                       OVERTIME_DICT,
                       BRAND_RECOGNITION_DICT,
                       RECRUITMENT_DIFFICULTY_DICT,
                       EMPLOYEE_SATISFACTION_DICT
)
from metric import outcome

#----------SETTINGS----------
page_title = "Job Order's Performance Metric Calculator"
page_icon = ":bar_chart:" #emoji : https://wwww.webfx.com/tools/emoji-cheat-sheet/
layout = "wide"

min_bonus = 0
min_salary = 4225
contract_length_options = list(range(1, 37)) + ["Indefinite"]

st.set_page_config(page_title = page_title, page_icon = page_icon, layout = layout)
st.title(page_title + " " + page_icon)

st.sidebar.write("                                 ")

st.header("Job order's survey")
with st.form("survey_form", clear_on_submit = False):
    col1, col2, col3 = st.columns(3)
    
    voivodship = col1.selectbox("Select Voivodship:", VOIVODSHIP_LIST)   
    industry = col2.selectbox("Select Industry:", INDUSTRY_LIST)   
    job_type = col3.selectbox("Select Job Type:", JOB_TYPE_LIST)   
    salary = col1.number_input("Enter a monthly salary: ", min_value = min_salary, step = 10)         
    bonus = col2.number_input("Enter a monthly bonus:", min_value = min_bonus, step = 10) 
    benefits = col3.multiselect("What benefits do you offer?", ['meals', 'sport card', 'medical care'])   
    contract_type = col1.selectbox("Select contract type: ", CONTRACT_TYPE_DICT.keys())    
    contract_length = col2.selectbox("Select contract length:", contract_length_options)   
    shifts = col1.selectbox("Select shift's info: ", SHIFTS_DICT.keys())    
    overtime = col2.selectbox("Select overtime's info: ", OVERTIME_DICT.keys())   
    brand = col1.selectbox("Select brand's recognition: ", BRAND_RECOGNITION_DICT.keys())
    recruitment = col2.selectbox("Select recruitment's difficulty: ", RECRUITMENT_DIFFICULTY_DICT.keys())  
    satisfaction = col1.selectbox("Select employee's satisfaction: ", EMPLOYEE_SATISFACTION_DICT.keys())
    fill_rate = col2.slider("Select the desired fill rate range for benchmark :", value = [0.00, 1.00])
    
    filters_df = pd.DataFrame({
        "Filters" : ['Voivodship', 'Industry', 'Job Type', 'Fill Rate Lower Bound', 'Fill Rate Upper Bound'],
        "Values" : [voivodship, industry, job_type, fill_rate[0], fill_rate[1]]
    })
    
    col3.header("Selected benchmark criterions")
    col3.write(filters_df)
    
    submit_survey = st.form_submit_button("Save Survey")
    if submit_survey : 
        st.write("Form submitted! Now, computing the results... Check the sidebar for detailed metrics.")

        benefits_dict = { "paid_meals": 0, "sport_card": 0, "medical_care": 0 }
        benefits_map = {
            "meals": "paid_meals",
            "sport card": "sport_card",
            "medical care": "medical_care"
        }
        
        for benefit in benefits:
            if benefit in benefits_map:
                benefits_dict[benefits_map[benefit]] = 1
        
        # Dictionary structure for JSON survey output
        job_order_data = {
            "job_order": {
                "Voivodship": voivodship,
                "Industry": industry,
                "Job Type": job_type,
                "Salary": salary,
                "Bonus": bonus,
                "Benefits": benefits_dict,
                "Contract Length": contract_length,
                "Contract Type": contract_type,
                "Brand Recognition": brand,
                "Recruitment Difficulty": recruitment,
                "Shifts": shifts,
                "Overtime": overtime,
                "Employee Satisfaction": satisfaction
            }
        }
        
        # Writing to a JSON file
        with open('survey_input.json', 'w') as json_file:
            json.dump(job_order_data, json_file, indent = 4)

        st.success("Survey data saved to JSON file successfully.")
        
        # Dictionary structure for JSON filters output
        filter_input_data = {
            "filters": {
                "Voivodship": voivodship,
                "Industry": industry,
                "Job Type": job_type,
                "Fill_Rate_lower_bound": fill_rate[0],
                "Fill_Rate_upper_bound": fill_rate[1],
            }
        }
        
        # Writing to a JSON file
        with open('filters_input.json', 'w') as json_file:
            json.dump(filter_input_data, json_file, indent = 4)
        
        # Performing calculations
        benchmark_df, metric, length = outcome()
        
        scorings = pd.DataFrame(benchmark_df)
        scorings.columns = ['Scores']
        scorings.index.name = 'Features'
        
        # Presenting the results
        # Since the survey form occupies more space than results it will be displayed in the main window, while results in the sidebar
        st.sidebar.title("Results")
        st.sidebar.text("Scores may range from 0 to 100.")
        st.sidebar.metric(label = "Overall Score :", value = metric)
        st.sidebar.dataframe(scorings)      
        st.sidebar.write("Benchmark made upon", length, "samples.")
        st.sidebar.caption("If benchmark size = 0, there is no data to become a goundtruth base for benchmark. Change filtering criterions.")
        st.sidebar.caption("Hitting 100 means that there is no better score - keep in mind that it doesn't mean that any competitor didn't reach the same level.")
