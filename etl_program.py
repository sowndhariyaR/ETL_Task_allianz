import asyncio
from scraper import scrape_team_stats
from transformer import transform_data_to_excel
from zipping import zip_html_files

async def main():
    html_contents = await scrape_team_stats()
    transform_data_to_excel(html_contents)
    zip_html_files(html_files=html_contents)  

if __name__ == "__main__":
    asyncio.run(main())
