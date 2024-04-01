import pandas as pd

from matplotlib import pyplot as plt


# TODO: how bad is this interface? Yes
# take a figure and axis as input, default to None
# return the figure and axis and user can call show on the figure
def plot_x_by_y_at_b(
    df: pd.DataFrame,
    x,
    b,
    y,
    markers=[".", "x", "+", "3", "_", "s", "o", "p"],
    colors=[
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ],
):
    """
    plot x by y for different values of b
    each group is plotted in a separate subplot in a single row
    """

    num_groups = len(df[b].dropna().unique())
    fig, ax = plt.subplots(1, num_groups, figsize=(16, 4))

    ylim = (df[y].min(), df[y].max())
    ylim = (
        ylim[0] - abs(ylim[0]) * 0.05,
        ylim[1] + abs(ylim[1]) * 0.05,
    )

    xlim = (df[x].min(), df[x].max())
    xlim = (
        xlim[0] - abs(xlim[0]) * 0.05,
        xlim[1] + abs(xlim[1]) * 0.05,
    )

    for idx, (b_val, sub_df) in enumerate(df[[y, x, b]].groupby(b)):
        sub_df.plot(
            ax=ax[idx],
            c=colors[idx],
            kind="scatter",
            marker=markers[idx],
            x=x,
            y=y,
            label=f"{b}={b_val}",
            alpha=0.7,
            grid=True,
            ylim=ylim,
            xlim=xlim,
        )
        if idx:
            ax[idx].axes.get_yaxis().set_label_text("")
    fig.suptitle(f"{y} vs {x} @ {b}")
    fig.show()
