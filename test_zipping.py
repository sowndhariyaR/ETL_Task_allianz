import os
import zipfile
import pytest
from zipping import zip_html_files

def test_zip_html_files():
    sample_htmls = [
        '<html><body>Page 1</body></html>',
        '<html><body>Page 2</body></html>'
    ]
    zip_filename = 'test_html_files.zip'

    zip_html_files(zip_filename, sample_htmls)

    assert os.path.exists(zip_filename), "Zip file was not created"

    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        assert '1.html' in zip_file.namelist()
        assert '2.html' in zip_file.namelist()

        with zip_file.open('1.html') as file:
            assert file.read().decode('utf-8') == '<html><body>Page 1</body></html>'

        with zip_file.open('2.html') as file:
            assert file.read().decode('utf-8') == '<html><body>Page 2</body></html>'

    os.remove(zip_filename)

if __name__ == '__main__':
    pytest.main()
