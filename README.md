# Hockey Team Stats ETL
## Overview

This project extracts hockey team statistics from the website [https://www.scrapethissite.com/pages/forms/]  processes the data, and produces two main outputs:

1. **A ZIP file** containing all original HTML files collected from the site, named `1.html`, `2.html`, etc.
2. **An Excel file** named `hockey_stats.xlsx` with two sheets:
   - **"NHL Stats 1990-2011"**: Contains all scraped rows in the order they appear on the website.
   - **"Winner and Loser per Year"**: Provides a summary of the team with the most wins and the team with the least wins per year.

## Step-by-Step Execution

 1. Clone the Repository

Clone the repository to your local machine. Open your terminal or command prompt and run:

```sh
git clone <repository_url>
cd <repository_directory>

 2. Set Up a Virtual Environment
python -m venv venv
venv\Scripts\activate

 3. Install Dependencies
#pip install -r requirements.txt

 4. Run the ETL Process
#python etl_program.py

 5. Run Tests 
#pytest
