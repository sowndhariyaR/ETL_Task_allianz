import asyncio
from scraper import scrape_team_stats
from transformer import transform_data_to_excel
from zipping import zip_html_files

async def main():
    # Scrape all pages
    html_contents = await scrape_team_stats()

    # Transform and save data to Excel
    transform_data_to_excel(html_contents)

    # Zip HTML files
    zip_html_files(html_files=html_contents)  # Pass html_contents as positional argument

if __name__ == "__main__":
    asyncio.run(main())
