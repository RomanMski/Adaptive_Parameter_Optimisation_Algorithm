from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reports" / "readme_main_showcase"

BG = "#f4f6f8"
PAPER = "#ffffff"
INK = "#14202b"
MUTED = "#62707d"
LINE = "#d8dfe5"
NAVY = "#173b57"
BLUE = "#2f6f9f"
BLUE_LIGHT = "#e8f0f6"
TEAL = "#287f78"
TEAL_LIGHT = "#e5f1ef"
GOLD = "#b78627"
GOLD_LIGHT = "#f5efdf"
CORAL = "#c45f47"
CORAL_LIGHT = "#f7eae6"
GREY_LIGHT = "#edf0f2"


def setup() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "figure.facecolor": BG,
            "axes.facecolor": BG,
            "text.color": INK,
        }
    )


def rounded_box(
    ax,
    x: float,
    y: float,
    width: float,
    height: float,
    face: str = PAPER,
    edge: str = LINE,
    radius: float = 0.008,
    linewidth: float = 1.2,
    zorder: int = 1,
):
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle=f"round,pad=0.004,rounding_size={radius}",
        transform=ax.transAxes,
        facecolor=face,
        edgecolor=edge,
        linewidth=linewidth,
        zorder=zorder,
    )
    ax.add_patch(patch)
    return patch


def arrow(ax, x1: float, y1: float, x2: float, y2: float, color: str = MUTED, width: float = 1.6) -> None:
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        xycoords=ax.transAxes,
        arrowprops=dict(arrowstyle="->", color=color, lw=width, shrinkA=0, shrinkB=0),
        zorder=5,
    )


def save(fig, name: str) -> None:
    fig.savefig(OUTPUT / name, dpi=190, facecolor=BG, bbox_inches="tight", pad_inches=0.16)
    plt.close(fig)


def draw_system_overview() -> None:
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.045, 0.935, "Adaptive portfolio research system", fontsize=29, fontweight="bold")
    ax.text(
        0.045,
        0.892,
        "Many specialised setups, one evidence standard and one shared pool of capital",
        fontsize=14,
        color=MUTED,
    )
    ax.text(
        0.955,
        0.926,
        "PUBLIC SYSTEM MAP",
        fontsize=10.5,
        fontweight="bold",
        color=BLUE,
        ha="right",
    )
    ax.text(
        0.045,
        0.835,
        "RESEARCH SCALE     ~500 GB workspace   |   ~5 days of cloud compute   |   second and minute data",
        fontsize=10.5,
        fontweight="bold",
        color=MUTED,
    )

    rounded_box(ax, 0.035, 0.19, 0.93, 0.60, face=PAPER, edge=LINE, radius=0.012)
    dividers = [0.285, 0.535, 0.735]
    for x in dividers:
        ax.plot([x, x], [0.24, 0.74], transform=ax.transAxes, color=LINE, lw=1.2)

    ax.text(0.06, 0.74, "SETUP LIBRARY", fontsize=10.5, fontweight="bold", color=BLUE)
    ax.text(0.06, 0.704, "Independent sleeves\nwith frozen identities", fontsize=9.6, color=INK, va="top", linespacing=1.3)

    sleeve_rows = [
        ("A", "market and horizon", BLUE, BLUE_LIGHT),
        ("B", "factor combination", TEAL, TEAL_LIGHT),
        ("C", "decision and risk rules", GOLD, GOLD_LIGHT),
        ("...", "more candidate setups", CORAL, CORAL_LIGHT),
    ]
    sleeve_y = [0.59, 0.505, 0.42, 0.335]
    for y, (letter, label, color, light) in zip(sleeve_y, sleeve_rows):
        rounded_box(ax, 0.06, y, 0.19, 0.064, face=light, edge=color, radius=0.006, linewidth=1.1)
        ax.text(0.079, y + 0.032, letter, fontsize=11, fontweight="bold", color=color, va="center")
        ax.text(0.111, y + 0.032, label, fontsize=9.8, color=INK, va="center")

    ax.text(0.31, 0.74, "EVIDENCE AVAILABLE NOW", fontsize=10.5, fontweight="bold", color=TEAL)
    ax.text(0.31, 0.704, "Only information known\nat the decision time", fontsize=9.6, color=INK, va="top", linespacing=1.3)
    evidence_rows = [
        ("Comparable completed setups", BLUE),
        ("Sample support and outcomes", TEAL),
        ("Current market context", GOLD),
        ("Costs and execution quality", CORAL),
        ("Current cash and exposure", NAVY),
    ]
    evidence_y = [0.61, 0.537, 0.464, 0.391, 0.318]
    for y, (label, color) in zip(evidence_y, evidence_rows):
        ax.scatter([0.324], [y], transform=ax.transAxes, s=115, color=color, edgecolor=PAPER, linewidth=1.2, zorder=3)
        ax.text(0.346, y, label, fontsize=10.2, va="center", color=INK)
        ax.plot([0.315, 0.505], [y - 0.031, y - 0.031], transform=ax.transAxes, color=LINE, lw=0.8)

    ax.text(0.56, 0.74, "CONFIDENCE GATE", fontsize=10.5, fontweight="bold", color=GOLD)
    ax.text(0.56, 0.704, "Evidence, not certainty", fontsize=9.6, color=INK, va="top")
    ax.plot([0.59, 0.59], [0.327, 0.618], transform=ax.transAxes, color=LINE, lw=5, solid_capstyle="round")
    gate_points = [
        (0.595, "HIGH", TEAL, "eligible"),
        (0.485, "MEDIUM", GOLD, "review"),
        (0.375, "WEAK", CORAL, "reject"),
    ]
    for y, level, color, action in gate_points:
        ax.scatter([0.59], [y], transform=ax.transAxes, s=330, color=color, edgecolor=PAPER, linewidth=2.2, zorder=4)
        ax.text(0.622, y + 0.008, level, fontsize=10.3, fontweight="bold", color=color, va="center")
        ax.text(0.622, y - 0.022, action, fontsize=9.1, color=MUTED, va="center")

    ax.text(0.76, 0.74, "ONE CAPITAL POOL", fontsize=10.5, fontweight="bold", color=NAVY)
    ax.text(0.76, 0.704, "Qualified setups compete\nfor the same cash", fontsize=9.6, color=INK, va="top", linespacing=1.3)
    rounded_box(ax, 0.765, 0.335, 0.15, 0.285, face=GREY_LIGHT, edge=LINE, radius=0.006)
    capital_blocks = [
        (0.526, 0.09, TEAL, "SLEEVE A", "FULL"),
        (0.451, 0.07, BLUE, "SLEEVE B", "PARTIAL"),
        (0.36, 0.085, PAPER, "CASH", "AVAILABLE"),
    ]
    for y, height, color, title, state in capital_blocks:
        face = color if color != PAPER else PAPER
        edge = color if color != PAPER else LINE
        rounded_box(ax, 0.778, y, 0.124, height, face=face, edge=edge, radius=0.004, linewidth=1.0, zorder=3)
        text_color = PAPER if color != PAPER else MUTED
        ax.text(0.79, y + height * 0.61, title, fontsize=8.7, fontweight="bold", color=text_color, va="center")
        ax.text(0.89, y + height * 0.61, state, fontsize=7.7, color=text_color, va="center", ha="right")
    rounded_box(ax, 0.765, 0.265, 0.15, 0.055, face=CORAL_LIGHT, edge=CORAL, radius=0.005)
    ax.text(0.778, 0.292, "SLEEVE C", fontsize=8.7, fontweight="bold", color=CORAL, va="center")
    ax.text(0.902, 0.292, "SKIPPED", fontsize=7.7, color=CORAL, ha="right", va="center")

    arrow(ax, 0.258, 0.508, 0.278, 0.508)
    arrow(ax, 0.508, 0.508, 0.528, 0.508)
    arrow(ax, 0.708, 0.508, 0.728, 0.508)

    rounded_box(ax, 0.035, 0.052, 0.93, 0.102, face=NAVY, edge=NAVY, radius=0.008)
    ax.text(
        0.5,
        0.103,
        "The main question is not which rule once had the highest return.\nIt is which opportunity deserves scarce capital now.",
        fontsize=12.2,
        fontweight="bold",
        color=PAPER,
        ha="center",
        va="center",
    )
    save(fig, "06_public_research_loop.png")


def draw_capital_replay() -> None:
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.045, 0.935, "One capital pool changes the backtest", fontsize=29, fontweight="bold")
    ax.text(
        0.045,
        0.892,
        "Standalone tests can reuse the same money. A portfolio replay has to decide what can actually be funded.",
        fontsize=14,
        color=MUTED,
    )

    panels = [
        (0.04, 0.285, 0.43, 0.52, "ISOLATED VIEW", "Every sleeve assumes the cash is free"),
        (0.53, 0.285, 0.43, 0.52, "SHARED PORTFOLIO REPLAY", "Every decision changes what remains available"),
    ]
    for x, y, width, height, title, subtitle in panels:
        rounded_box(ax, x, y, width, height, face=PAPER, edge=LINE, radius=0.012)
        ax.text(x + 0.025, y + height - 0.055, title, fontsize=10.5, fontweight="bold", color=BLUE)
        ax.text(x + 0.025, y + height - 0.092, subtitle, fontsize=10.4, color=INK)

    timeline_start = 0.095
    timeline_end = 0.435
    row_y = [0.635, 0.535, 0.435]
    row_labels = ["SLEEVE A", "SLEEVE B", "SLEEVE C"]
    intervals = [(0.13, 0.34, TEAL), (0.19, 0.405, BLUE), (0.255, 0.445, GOLD)]
    for y, label, (start, end, color) in zip(row_y, row_labels, intervals):
        ax.text(0.065, y, label, fontsize=9.3, fontweight="bold", color=MUTED, va="center")
        ax.plot([timeline_start, timeline_end], [y, y], transform=ax.transAxes, color=LINE, lw=2, zorder=2)
        rounded_box(ax, start, y - 0.025, end - start, 0.05, face=color, edge=color, radius=0.006, zorder=3)
        ax.text((start + end) / 2, y, "ASSUMES FULL CASH", fontsize=8.1, fontweight="bold", color=PAPER, ha="center", va="center")
    ax.text(0.065, 0.335, "The active periods overlap, so the same capital is counted several times.", fontsize=9.8, color=CORAL)

    right_start = 0.585
    right_end = 0.925
    right_rows = [0.655, 0.565, 0.475, 0.385]
    for y, label in zip(right_rows, ["A", "B", "C", "D"]):
        ax.text(0.557, y, label, fontsize=9.7, fontweight="bold", color=MUTED, va="center")
        ax.plot([right_start, right_end], [y, y], transform=ax.transAxes, color=LINE, lw=2, zorder=2)

    replay_intervals = [
        (0.607, 0.76, right_rows[0], TEAL, "FULL"),
        (0.67, 0.79, right_rows[1], BLUE, "PARTIAL"),
        (0.73, 0.80, right_rows[2], CORAL_LIGHT, "SKIPPED"),
        (0.797, 0.91, right_rows[3], GOLD, "FULL"),
    ]
    for start, end, y, color, label in replay_intervals:
        edge = CORAL if label == "SKIPPED" else color
        text_color = CORAL if label == "SKIPPED" else PAPER
        rounded_box(ax, start, y - 0.025, end - start, 0.05, face=color, edge=edge, radius=0.006, zorder=3)
        ax.text((start + end) / 2, y, label, fontsize=8.3, fontweight="bold", color=text_color, ha="center", va="center")

    event_x = [0.607, 0.67, 0.73, 0.797, 0.91]
    event_labels = ["A opens", "B arrives", "C arrives", "A closes\nD opens", "D closes"]
    for x, label in zip(event_x, event_labels):
        ax.plot([x, x], [0.365, 0.70], transform=ax.transAxes, color=LINE, lw=0.8, linestyle=(0, (2, 3)), zorder=2)
        ax.text(x, 0.335, label, fontsize=7.7, color=MUTED, ha="center", va="top", linespacing=1.15)

    rounded_box(ax, 0.04, 0.075, 0.92, 0.145, face=NAVY, edge=NAVY, radius=0.01)
    bottom_items = [
        (0.075, "FUNDING STATE", "Full, partial or skipped"),
        (0.365, "OPPORTUNITY COST", "What unavailable cash prevented"),
        (0.66, "PORTFOLIO RISK", "Cash and open exposure through time"),
    ]
    for index, (x, title, detail) in enumerate(bottom_items):
        if index:
            ax.plot([x - 0.03, x - 0.03], [0.105, 0.19], transform=ax.transAxes, color="#416078", lw=1.2)
        ax.text(x, 0.171, title, fontsize=9.5, fontweight="bold", color="#8dc7c1")
        ax.text(x, 0.125, detail, fontsize=10.5, color=PAPER)
    save(fig, "07_public_capital_replay.png")


def draw_audit_path() -> None:
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.045, 0.935, "The audit that changed the project", fontsize=29, fontweight="bold")
    ax.text(
        0.045,
        0.892,
        "The original result could be reproduced exactly. That still did not make the information timing valid.",
        fontsize=14,
        color=MUTED,
    )

    rounded_box(ax, 0.04, 0.43, 0.92, 0.37, face=PAPER, edge=LINE, radius=0.012)
    ax.text(0.065, 0.748, "ONE AGGREGATED BAR", fontsize=10.5, fontweight="bold", color=BLUE)
    ax.text(0.065, 0.712, "The timestamp said the feature was ready at the start. Its final input only existed at the close.", fontsize=10.7, color=INK)

    start_x = 0.12
    decision_x = 0.39
    close_x = 0.82
    line_y = 0.565
    ax.plot([start_x, close_x], [line_y, line_y], transform=ax.transAxes, color=LINE, lw=7, solid_capstyle="round")
    points = [
        (start_x, "BAR OPENS", "feature labelled\navailable", BLUE),
        (decision_x, "DECISION", "signal reads\nthe feature", GOLD),
        (close_x, "BAR CLOSES", "final input now\nexists", TEAL),
    ]
    for x, title, detail, color in points:
        ax.scatter([x], [line_y], transform=ax.transAxes, s=520, color=color, edgecolor=PAPER, linewidth=2.6, zorder=4)
        ax.text(x, line_y - 0.075, title, fontsize=9.4, fontweight="bold", color=color, ha="center")
        ax.text(x, line_y - 0.11, detail, fontsize=8.8, color=MUTED, ha="center", va="top", linespacing=1.25)

    ax.annotate(
        "",
        xy=(decision_x + 0.015, line_y + 0.035),
        xytext=(close_x - 0.015, line_y + 0.035),
        xycoords=ax.transAxes,
        arrowprops=dict(arrowstyle="->", color=CORAL, lw=2.4, connectionstyle="arc3,rad=0.28"),
    )
    ax.text(
        0.61,
        0.683,
        "future close leaked back into an earlier decision",
        fontsize=10.2,
        fontweight="bold",
        color=CORAL,
        ha="center",
        bbox=dict(facecolor=PAPER, edgecolor="none", pad=2.0),
    )

    stage_y = 0.245
    stage_x = [0.055, 0.24, 0.425, 0.61, 0.795]
    stages = [
        ("EXACT REPRODUCTION", "PASS", TEAL_LIGHT, TEAL),
        ("TIMING AUDIT", "ISSUE FOUND", CORAL_LIGHT, CORAL),
        ("CAUSAL REBUILD", "PASS", TEAL_LIGHT, TEAL),
        ("FROZEN FUTURE TEST", "FAIL", CORAL_LIGHT, CORAL),
        ("DEPLOYMENT", "REJECT", CORAL_LIGHT, CORAL),
    ]
    for index, (x, stage) in enumerate(zip(stage_x, stages)):
        title, status, light, color = stage
        rounded_box(ax, x, stage_y, 0.15, 0.105, face=light, edge=color, radius=0.006)
        ax.text(x + 0.075, stage_y + 0.068, title, fontsize=8.2, fontweight="bold", color=INK, ha="center", va="center")
        ax.text(x + 0.075, stage_y + 0.032, status, fontsize=9.4, fontweight="bold", color=color, ha="center", va="center")
        if index < len(stage_x) - 1:
            arrow(ax, x + 0.155, stage_y + 0.053, stage_x[index + 1] - 0.008, stage_y + 0.053, width=1.4)

    rounded_box(ax, 0.04, 0.075, 0.92, 0.095, face=NAVY, edge=NAVY, radius=0.008)
    ax.text(
        0.5,
        0.122,
        "A reproducible backtest can still be invalid when one timestamp gives the model information too early.",
        fontsize=13.3,
        fontweight="bold",
        color=PAPER,
        ha="center",
        va="center",
    )
    save(fig, "08_causal_audit_path.png")


def draw_search_landscape() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(16, 7.8))
    fig.subplots_adjust(left=0.055, right=0.96, top=0.69, bottom=0.18, wspace=0.18)
    fig.suptitle("Why the highest score was not enough", x=0.055, y=0.965, ha="left", fontsize=29, fontweight="bold")
    fig.text(
        0.055,
        0.855,
        "A sharp winner can be an accident of the search. A wider region has more support when nearby choices behave similarly.",
        fontsize=14,
        color=MUTED,
    )
    fig.text(0.95, 0.952, "CONCEPTUAL ILLUSTRATION", ha="right", fontsize=10, fontweight="bold", color=BLUE)

    x = np.linspace(-3.0, 3.0, 260)
    y = np.linspace(-3.0, 3.0, 260)
    xx, yy = np.meshgrid(x, y)
    fragile = np.exp(-(((xx - 0.85) / 0.28) ** 2 + ((yy + 0.2) / 0.22) ** 2))
    fragile += 0.20 * np.exp(-(((xx + 1.35) / 1.1) ** 2 + ((yy - 0.9) / 0.9) ** 2))
    stable = 0.83 * np.exp(-(((xx - 0.2) / 1.35) ** 2 + ((yy + 0.05) / 1.05) ** 2))
    stable += 0.13 * np.exp(-(((xx + 1.4) / 0.8) ** 2 + ((yy - 1.35) / 0.7) ** 2))
    cmap = LinearSegmentedColormap.from_list("research", ["#edf1f4", "#c7dce8", "#6fa4bd", "#2f6f9f", "#173b57"])

    panels = [
        (axes[0], fragile, "FRAGILE WINNER", "One exceptional point with little neighbour support", (0.85, -0.2), CORAL),
        (axes[1], stable, "STABLE REGION", "A wider area that survives small changes", (0.2, -0.05), TEAL),
    ]
    for ax, surface, title, subtitle, point, accent in panels:
        ax.set_facecolor(PAPER)
        ax.contourf(xx, yy, surface, levels=14, cmap=cmap)
        ax.contour(xx, yy, surface, levels=8, colors=PAPER, linewidths=0.55, alpha=0.55)
        ax.scatter([point[0]], [point[1]], s=180, color=accent, edgecolor=PAPER, linewidth=2.2, zorder=5)
        ax.text(0.04, 1.08, title, transform=ax.transAxes, fontsize=11, fontweight="bold", color=accent)
        ax.text(0.04, 1.025, subtitle, transform=ax.transAxes, fontsize=10.2, color=INK)
        ax.set_xlabel("research dimension 1", fontsize=9.5, color=MUTED)
        ax.set_ylabel("research dimension 2", fontsize=9.5, color=MUTED)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(LINE)
            spine.set_linewidth(1.1)

    fig.text(
        0.5,
        0.075,
        "I stopped asking only for the best point and started asking whether the surrounding evidence survived.",
        fontsize=13.2,
        fontweight="bold",
        color=INK,
        ha="center",
    )
    save(fig, "09_public_search_landscape.png")


def main() -> None:
    setup()
    draw_system_overview()
    draw_capital_replay()
    draw_audit_path()
    draw_search_landscape()


if __name__ == "__main__":
    main()
