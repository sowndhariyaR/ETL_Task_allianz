import zipfile
from typing import List

def zip_html_files(zip_filename: str = 'html_files.zip', html_files: List[str] = None):
    if html_files is None:
        raise ValueError("No HTML files to zip")

    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for i, html_content in enumerate(html_files, start=1):
            file_name = f"{i}.html"
            zipf.writestr(file_name, html_content)


#
# import zipfile
# from typing import List, Tuple
#
# def zip_html_files(zip_filename: str, html_files: List[Tuple[str, str]]):
#     with zipfile.ZipFile(zip_filename, 'w') as zipf:
#         for file_name, html_content in html_files:
#             # Ensure html_content is a string and encode it to bytes
#             zipf.writestr(file_name, html_content.encode('utf-8'))
