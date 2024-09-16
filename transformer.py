from bs4 import BeautifulSoup
from openpyxl import Workbook
from typing import List, Dict, Any


def parse_html_contents(html_contents: List[str]) -> List[Dict[str, Any]]:
    data = []

    for html_content in html_contents:
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')

        headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]

        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) >= len(headers):
                row_data = {}
                for header, col in zip(headers, cols):
                    row_data[header] = col.get_text(strip=True)
                data.append(row_data)

    return data


def get_winner_loser_summary(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    yearly_stats = {}

    for item in data:
        year = item['Year']
        team_name = item['Team Name']
        wins = int(item['Wins'])

        if year not in yearly_stats:
            yearly_stats[year] = {'winner': {'team': team_name, 'wins': wins},
                                  'loser': {'team': team_name, 'wins': wins}}

        if wins > yearly_stats[year]['winner']['wins']:
            yearly_stats[year]['winner'] = {'team': team_name, 'wins': wins}
        elif wins < yearly_stats[year]['loser']['wins']:
            yearly_stats[year]['loser'] = {'team': team_name, 'wins': wins}

    summary = []
    for year, stats in yearly_stats.items():
        summary.append({
            'Year': year,
            'Winner': stats['winner']['team'],
            'Winner Num. of Wins': stats['winner']['wins'],
            'Loser': stats['loser']['team'],
            'Loser Num. of Wins': stats['loser']['wins']
        })

    return summary


def transform_data_to_excel(html_contents: List[str]):
    data = parse_html_contents(html_contents)
    if not data:
        raise ValueError("No data found to write to Excel")

    workbook = Workbook()

    # Create Sheet 1: NHL Stats 1990-2011
    sheet1 = workbook.active
    sheet1.title = "NHL Stats 1990-2011"

    if data:
        headers = list(data[0].keys())
        sheet1.append(headers)

        for item in data:
            sheet1.append([item.get(header, '') for header in headers])

    # Create Sheet 2: Winner and Loser per Year
    sheet2 = workbook.create_sheet(title="Winner and Loser per Year")
    summary_data = get_winner_loser_summary(data)

    if summary_data:
        summary_headers = list(summary_data[0].keys())
        sheet2.append(summary_headers)

        for item in summary_data:
            sheet2.append([item.get(header, '') for header in summary_headers])

    workbook.save("hockey_stats.xlsx")
