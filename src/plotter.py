import matplotlib.pyplot as plt


def plot_correlation(data):
    line1_data = [float(value) for value in data["line1"]["data"]]
    line2_data = [float(value) for value in data["line2"]["data"]]

    fig, ax1 = plt.subplots()

    color = "tab:red"
    ax1.set_xlabel("Time")
    ax1.set_ylabel(data["line1"]["label"], color=color)
    ax1.plot(data["time"], line1_data, color=color, label=data["line1"]["label"])
    ax1.tick_params(axis="y", labelcolor=color)

    ax2 = ax1.twinx()
    color = "tab:blue"
    ax2.set_ylabel(data["line2"]["label"], color=color)
    ax2.plot(data["time"], line2_data, color=color, label=data["line2"]["label"])
    ax2.tick_params(axis="y", labelcolor=color)

    fig.tight_layout()

    plt.title(f"{data['line1']['label']} \nvs\n {data['line2']['label']}")
    plt.xticks(rotation=45)
    fig.set_size_inches(10, 6)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.88, bottom=0.1)

    plt.show()
