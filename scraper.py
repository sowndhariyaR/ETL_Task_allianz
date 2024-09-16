import aiohttp
import asyncio
from bs4 import BeautifulSoup
from typing import List

BASE_URL = 'https://www.scrapethissite.com/pages/forms/'

async def fetch_page(session: aiohttp.ClientSession, page_num: int) -> str:
    url = f"{BASE_URL}?page_num={page_num}"
    async with session.get(url) as response:
        return await response.text()

async def scrape_team_stats() -> List[str]:
    html_pages = []
    async with aiohttp.ClientSession() as session:
        page_num = 1
        while True:
            html = await fetch_page(session, page_num)
            soup = BeautifulSoup(html, 'html.parser')
            teams = soup.find_all('tr', class_='team')
            if not teams:
                break
            html_pages.append(html)
            page_num += 1
    return html_pages
