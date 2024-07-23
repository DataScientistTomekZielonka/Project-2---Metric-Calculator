# Job Order's Performance Metric Calculator

# Business Objective :
We want a tool showing how the customers job offer we are processing is attractive on the local market.
Job offers consider blue collar jobs only and are always submitted in bulk per order (i.e. 20 posts).

# Challenges :
1. Due to the data migration delays, necessary data is unavailable.
2. Business can deliver sample of data, yet :
    - sample is to small (c.1000 data entries)
    - sample is lacking 'fill rate' feature, which is one of the filtering keys

# Proposed approach :
1. Until real data is available, in order to start developing the tool, simulate data with the following steps :
    - use bootstrap sampling on sample of data in order to generate dataset large enough
    - use Monte Carlo simulation to simulate 'fill rate' based on domain expertise delivered by Business

# Description :
1. This program calculates metrics determining, how attractive customer's job offer is on the local market.
2. Data describing local market's conditions is filtered out from historical data of other job offers that have been realized by the company (HR Agency).
3. Benchmark data is filtered by 'voivodship', 'industry', 'job type, and 'fill rate'.
4. 'Fill rate' describes in what extent a job order was fullfilled by the HR Agency (i.e. if out 0f 20 posts, 15 where fullfilled, the fill rate = 0.75).
5. Infut and filtered data is transformed into [0, 100] interval using MIN_MAX*100 formula what allows benchmarking.
6. Overall Score is based on waged arithmetical mean, where all wages add up to 1.

# Extrainfo :
1. Original data could not be presented therefore was simulated via small_dataset_nb.ipynb and next saved into small_dataset.xlsx.
2. Simulated dataset was 'replicated' into a large one via large_dataset_nb.ipynb and next saved into large_dataset.xlsx. 
