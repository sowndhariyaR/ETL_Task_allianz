import pytest
from transformer import parse_html_contents, get_winner_loser_summary

# Sample HTML content for testing
html_contents = [
    """
    <html>
    <body>
    <table>
        <tr>
            <th>Team Name</th>
            <th>Year</th>
            <th>Wins</th>
            <th>Losses</th>
            <th>OT Losses</th>
            <th>Win %</th>
            <th>Goals For (GF)</th>
            <th>Goals Against (GA)</th>
            <th>+ / -</th>
        </tr>
        <tr class="team">
            <td>Team A</td>
            <td>1990</td>
            <td>20</td>
            <td>30</td>
            <td>10</td>
            <td>0.400</td>
            <td>150</td>
            <td>200</td>
            <td>-50</td>
        </tr>
        <tr class="team">
            <td>Team B</td>
            <td>1990</td>
            <td>25</td>
            <td>25</td>
            <td>5</td>
            <td>0.500</td>
            <td>160</td>
            <td>180</td>
            <td>-20</td>
        </tr>
        <tr class="team">
            <td>Team C</td>
            <td>1991</td>
            <td>15</td>
            <td>35</td>
            <td>5</td>
            <td>0.300</td>
            <td>140</td>
            <td>210</td>
            <td>-70</td>
        </tr>
        <tr class="team">
            <td>Team D</td>
            <td>1991</td>
            <td>30</td>
            <td>20</td>
            <td>5</td>
            <td>0.600</td>
            <td>170</td>
            <td>150</td>
            <td>20</td>
        </tr>
    </table>
    </body>
    </html>
    """
]

def test_parse_html_contents():
    expected_data = [
        {'Team Name': 'Team A', 'Year': '1990', 'Wins': '20', 'Losses': '30', 'OT Losses': '10', 'Win %': '0.400', 'Goals For (GF)': '150', 'Goals Against (GA)': '200', '+ / -': '-50'},
        {'Team Name': 'Team B', 'Year': '1990', 'Wins': '25', 'Losses': '25', 'OT Losses': '5', 'Win %': '0.500', 'Goals For (GF)': '160', 'Goals Against (GA)': '180', '+ / -': '-20'},
        {'Team Name': 'Team C', 'Year': '1991', 'Wins': '15', 'Losses': '35', 'OT Losses': '5', 'Win %': '0.300', 'Goals For (GF)': '140', 'Goals Against (GA)': '210', '+ / -': '-70'},
        {'Team Name': 'Team D', 'Year': '1991', 'Wins': '30', 'Losses': '20', 'OT Losses': '5', 'Win %': '0.600', 'Goals For (GF)': '170', 'Goals Against (GA)': '150', '+ / -': '20'}
    ]
    data = parse_html_contents(html_contents)
    assert data == expected_data

def test_get_winner_loser_summary():
    parsed_data = [
        {'Team Name': 'Team A', 'Year': '1990', 'Wins': '20', 'Losses': '30', 'OT Losses': '10', 'Win %': '0.400', 'Goals For (GF)': '150', 'Goals Against (GA)': '200', '+ / -': '-50'},
        {'Team Name': 'Team B', 'Year': '1990', 'Wins': '25', 'Losses': '25', 'OT Losses': '5', 'Win %': '0.500', 'Goals For (GF)': '160', 'Goals Against (GA)': '180', '+ / -': '-20'},
        {'Team Name': 'Team C', 'Year': '1991', 'Wins': '15', 'Losses': '35', 'OT Losses': '5', 'Win %': '0.300', 'Goals For (GF)': '140', 'Goals Against (GA)': '210', '+ / -': '-70'},
        {'Team Name': 'Team D', 'Year': '1991', 'Wins': '30', 'Losses': '20', 'OT Losses': '5', 'Win %': '0.600', 'Goals For (GF)': '170', 'Goals Against (GA)': '150', '+ / -': '20'}
    ]
    expected_summary = [
        {'Year': '1990', 'Winner': 'Team B', 'Winner Num. of Wins': 25, 'Loser': 'Team A', 'Loser Num. of Wins': 20},
        {'Year': '1991', 'Winner': 'Team D', 'Winner Num. of Wins': 30, 'Loser': 'Team C', 'Loser Num. of Wins': 15}
    ]
    summary = get_winner_loser_summary(parsed_data)
    assert summary == expected_summary

