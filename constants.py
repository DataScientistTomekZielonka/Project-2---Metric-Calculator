#This file is storing all constants and listings that are used across the application.

VOIVODSHIP_LIST = [
    'Małopolskie',
    'Śląskie',
    'Lubuskie',
    'Wielkopolskie',
    'Zachodniopomorskie',
    'Dolnośląskie',
    'Opolskie',
    'Kujawsko-Pomorskie',
    'Pomorskie',
    'Warmińsko-Mazurskie',
    'Łódzkie',
    'Świętokrzyskie',
    'Lubelskie',
    'Podkarpackie',
    'Podlaskie',
    'Mazowieckie',
]

INDUSTRY_LIST = [
    'Manufacturing',
    'Warehousing',
    'Others'
]

JOB_TYPE_LIST = [
    'Forklift operators, internal logistics operators, etc.',
    'Machine operators, fitters, etc.',
    'Packers, pickers, sorters, etc.',
    'Production workers, production operator, etc.',
    'Specialists, e.g. turners, welders, electricians etc.',
    'Warehousment, warehouse workers, etc.'
]

BENEFITS_DICT = {
    'No benefits' : 0,
    'One benefit' : 1,
    'Two benefits' : 2,
    'All benefits' : 3
}

CONTRACT_LENGTH_DICT = {
    'up to 6 months' : 0,
    'more than 6 and up to 12 months' : 1,
    'more than 12 and up to 24 months' : 2,
    'more than 24 months or indefinite' : 3
}

CONTRACT_TYPE_DICT = {
    'Contract work' : 0, 
    'Mandate contract' : 1,
    'Contract of employment' : 2
}

BRAND_RECOGNITION_DICT = {
    'Very weak' : 0,
    'Weak' : 1,
    'Moderate' : 2,
    'Strong' : 3,
    'Very strong' : 4
}

RECRUITMENT_DIFFICULTY_DICT = {
    'Very difficult' : 0,
    'Difficult' : 1,
    'Normal' : 2,
    'Easy' : 3,
    'Very easy' : 4
}

SHIFTS_DICT = {
    'Two 12hrs shifts' : 0,
    'Three 8hrs shifts' : 1,
    'Two 8hrs shifts' : 2,
    'One 8hrs shift' : 3
}

OVERTIME_DICT = {
    'Regular overtime' : 0,
    'Ocassional overtime' : 1,
    'No overtime' : 2
}

EMPLOYEE_SATISFACTION_DICT = {
    'Very low' : 0,
    'Rather low' : 1,
    'Moderate' : 2,
    'Rather high' : 3,
    'Very high' : 4
}

METRIC_WAGES_DICT = {
    'Salary' : 0.25,
    'Bonus' : 0.05,
    'Benefits': 0.05,
    'Contract Length' : 0.10,
    'Contract Type' : 0.10,
    'Brand Recognition' : 0.05,
    'Recruitment Difficulty' : 0.05,
    'Shifts' : 0.10,
    'Overtime' : 0.10,
    'Employee Satisfaction' : 0.15   
}

#Sum of metric's wages must always add up to 1.

if __name__ == "__main__" :
    print(f'Sum of METRIC wages = {sum(METRIC_WAGES_DICT.values())}')