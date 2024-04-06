from src.download_html import download_and_save_html
from src.extract_correlations import extract_correlation
from src.plotter import plot_correlation
from src.storage import save_correlation


def single_correlation():
    url = (
        "https://www.tylervigen.com/spurious/correlation/2455_final-match-score-difference-in-the-volkswagen"
        "-challenger-set_correlates-with_the-number-of-outdoor-power-equipment-mechanics-in-pennsylvania"
    )
    file_id = url.split("/")[-1].split("_")[0]
    file_name = url.split("/")[-1]  # noqa: F841
    path, html = download_and_save_html(
        url, filename=f"{file_id}.html", return_file_as_content=True
    )

    if path is None or html is None:
        print("Failed to download and save HTML content")
        return None

    if data := extract_correlation(html):
        save_correlation(file_id, data)
        plot_correlation(data)
    else:
        print("Failed to extract correlation data")


def all_correlations():
    # 1. Download main page HTML (https://www.tylervigen.com/spurious-correlations)
    # 2. Extract all links of the correlations pages
    # 3. For each link:
    #     3.1. Download and save HTML
    #     3.2. Extract correlation data
    #     3.3. Save correlation data
    # 4. Go to next page and repeat

    pass


if __name__ == "__main__":
    single_correlation()
