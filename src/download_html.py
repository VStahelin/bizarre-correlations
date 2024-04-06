import os
from datetime import datetime
import requests

HTML_FILES_PATH = "html_files/"
HTML_FILES_FOLDER_LIST = []


def download_html(url):
    try:
        html = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    return html


def save_html(html, filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{html.url.split('/')[-1]}-{timestamp}.html"
    path = HTML_FILES_PATH + filename
    with open(path, "w", encoding="utf-8") as file:
        file.write(html.text)
    return path


def get_html_files_list():
    global HTML_FILES_FOLDER_LIST
    HTML_FILES_FOLDER_LIST = os.listdir(HTML_FILES_PATH)
    return HTML_FILES_FOLDER_LIST


def check_html_file_exists(filename):
    if not HTML_FILES_FOLDER_LIST:
        get_html_files_list()

    if filename in HTML_FILES_FOLDER_LIST:
        return True
    return False


def download_and_save_html(
    url, filename=None, return_file_as_content=False, force_download=False
):
    """
    Download HTML content from the given URL and save it to a file.
    :param url: URL to download HTML content from
    :param filename: Name of the file to save the HTML content to
    :param return_file_as_content: If True, return the file content as well
    :param force_download: If True, download the HTML content even if the file already exists
    :return: (path, html_content) if return_file_as_content is True, else (path, None)
    """

    if filename is not None and check_html_file_exists(filename):
        print(f"File {filename} already exists")
        if not force_download:
            if return_file_as_content:
                with open(HTML_FILES_PATH + filename, "r", encoding="utf-8") as file:
                    return HTML_FILES_PATH + filename, str(file.read())
            return HTML_FILES_PATH + filename, None

    if check_html_file_exists(filename) and force_download:
        print(f"Force downloading the file {filename}")

    html = download_html(url)
    if html is not None:
        path = save_html(html, filename)
        if return_file_as_content:
            return path, html.text
        return path, None
    return None, None


if __name__ == "__main__":
    url = "https://www.tylervigen.com/spurious-correlations"
    filename = "spurious-correlations-page1.html"
    force_download = False
    return_file_as_content = True
    path, html = download_and_save_html(
        url, filename, return_file_as_content, force_download
    )
