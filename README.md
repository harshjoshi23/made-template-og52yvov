# Methods of Advanced Data Engineering 

# Analysis of COVID-19 Case Rates in Correctional Facilities vs. State Trends

## Overview
This project, part of the Methods of Advanced Data Engineering (MADE WS2024/25) course. It explores COVID-19 case rates among inmates and officers within correctional facilities compared to broader state trends. The study employs detailed datasets to examine internal dynamics and their implications for public health strategies.

## Repository Structure
- `/data`: Data files used in the analysis.
- `/src`: Source code for data processing and analysis.
- `/project`: Contains the final report and any presentation materials.
  - `analysis-report.pdf`: The comprehensive final analysis report.
  - `/slides`: Contains presentation slides.

## Data Description
This project utilizes several datasets from state public health databases, focusing on:
- `facilities.csv`: Details about COVID-19 cases and deaths among inmates and officers.
- `systems.csv`: Data on health infrastructure and measures within correctional facilities.
- `us_data.csv`: Broader epidemiological data for the United States.
- `us_states.csv`: State-specific COVID-19 data on cases and deaths.

Data is sourced from verified public health records and adheres to open data licenses, allowing academic use while ensuring compliance with legal requirements. Detailed terms of the licensing are available on the New York Times website.

## Methodology
The analysis involves:
- Aggregating COVID-19 case data by state and facility.
- Standardizing data to case rates per 100,000 population for consistent comparisons.
- Using SQL for data management and Python for statistical analysis to explore correlations and trends.

## Results and Analysis
- **Correlation Matrix and Heatmap**: Analyzes relationships between different COVID-19 case rates within correctional environments and statewide.
- **Time Series Analysis**: Examines the progression of cases over time in states most affected by the pandemic.
- **Comparative Case Rates**: Between inmates and officers to highlight disparities and potential risk factors.
- **Facility to State Case Ratio**: Discusses the localized nature of outbreaks and their impact relative to state trends.

## Conclusions
The findings underscore significant disparities in COVID-19 impacts within correctional facilities compared to state-wide data, highlighting the urgent need for targeted health interventions and informed public health strategies.

## How to Use
1. Clone the repository.
2. Navigate to the `/src` directory to run analysis scripts.
3. View `analysis-report.pdf` for a detailed report on findings.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions
Contributions are welcome via pull requests. Please fork the repository and propose your changes.

## Contact
For further information or queries, please contact:
- **Harshvardhan Joshi**
- Email: [Harshvardhan.Joshi@fau.de]

Feel free to star this repository if you find it useful for your research or if it helped in understanding the impact of COVID-19 within correctional settings!
