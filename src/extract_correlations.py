from bs4 import BeautifulSoup, Comment


def get_correlations_pages_by_html(html):
    soup = BeautifulSoup(html, "html.parser")

    body = soup.find("body").find("div", {"class": "content"})
    top_layer_center_tags = [child for child in body.children if child.name == "center"]
    first_center_tag = top_layer_center_tags[0]  # noqa


def extract_correlation(html):
    soup = BeautifulSoup(html, "html.parser")

    body = soup.find("body").find("div", {"class": "content"})

    start_table_of_data_comment = body.find(
        string=lambda text: isinstance(text, Comment) and "Start Table of Data" in text
    )
    table = start_table_of_data_comment.find_next_sibling("div")

    table_data = []
    for row in table.find_all("tr"):
        row_data = []
        for cell in row.find_all("td"):
            row_data.append(cell.text)
        table_data.append(row_data)

    data = {
        "time": table_data[0][1:],
        "line1": {"label": table_data[1][0], "data": table_data[1][1:]},
        "line2": {"label": table_data[2][0], "data": table_data[2][1:]},
    }

    return data
