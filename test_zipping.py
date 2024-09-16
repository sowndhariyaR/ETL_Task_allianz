import os
import zipfile
import pytest
from zipping import zip_html_files

def test_zip_html_files():
    # Prepare sample HTML content
    sample_htmls = [
        '<html><body>Page 1</body></html>',
        '<html><body>Page 2</body></html>'
    ]
    zip_filename = 'test_html_files.zip'

    # Call the function to test
    zip_html_files(zip_filename, sample_htmls)

    # Assert the zip file is created
    assert os.path.exists(zip_filename), "Zip file was not created"

    # Assert the contents of the zip file
    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        # Check that both files are in the zip
        assert '1.html' in zip_file.namelist()
        assert '2.html' in zip_file.namelist()

        # Optionally, you can also check the content of the files
        with zip_file.open('1.html') as file:
            assert file.read().decode('utf-8') == '<html><body>Page 1</body></html>'

        with zip_file.open('2.html') as file:
            assert file.read().decode('utf-8') == '<html><body>Page 2</body></html>'

    # Clean up
    os.remove(zip_filename)

if __name__ == '__main__':
    pytest.main()
