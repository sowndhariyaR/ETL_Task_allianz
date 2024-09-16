import zipfile
from typing import List

def zip_html_files(zip_filename: str = 'html_files.zip', html_files: List[str] = None):
    if html_files is None:
        raise ValueError("No HTML files to zip")

    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for i, html_content in enumerate(html_files, start=1):
            file_name = f"{i}.html"
            zipf.writestr(file_name, html_content)


