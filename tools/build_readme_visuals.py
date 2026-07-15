from __future__ import annotations

from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reports" / "readme_main_showcase"

BG = "#f7f7f5"
PAPER = "#ffffff"
INK = "#17202b"
MUTED = "#657080"
LINE = "#d7dce2"
BLUE = "#3568a8"
BLUE_LIGHT = "#eaf1f8"
GOLD = "#b28a2d"
GOLD_LIGHT = "#f6f0df"
ORANGE = "#c9693c"
ORANGE_LIGHT = "#f8ebe5"
GREEN = "#3e8069"
GREEN_LIGHT = "#e7f1ed"
RED = "#a64d45"
RED_LIGHT = "#f6e9e7"


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


def box(ax, x, y, w, h, face=PAPER, edge=LINE, radius=0.012, linewidth=1.2):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.004,rounding_size={radius}",
        transform=ax.transAxes,
        facecolor=face,
        edgecolor=edge,
        linewidth=linewidth,
    )
    ax.add_patch(patch)
    return patch


def save(fig, name: str) -> None:
    fig.savefig(OUTPUT / name, dpi=180, facecolor=BG, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)


def draw_system_overview() -> None:
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.045, 0.935, "Adaptive parameter optimisation research system", fontsize=29, fontweight="bold")
    ax.text(
        0.045,
        0.895,
        "Selected view of a larger project built around traceable data, causal timing and tests that can reject a candidate",
        fontsize=13.5,
        color=MUTED,
    )

    scale_cards = [
        ("~500 GB", "research workspace", BLUE, BLUE_LIGHT),
        ("~5 days", "continuous cloud compute", GOLD, GOLD_LIGHT),
        ("second and minute data", "multiple markets and timeframes", GREEN, GREEN_LIGHT),
    ]
    card_x = [0.045, 0.36, 0.675]
    for x, (value, label, color, light) in zip(card_x, scale_cards):
        box(ax, x, 0.775, 0.28, 0.085, face=light, edge=color, radius=0.01)
        value_size = 16.5 if value == "second and minute data" else 18
        ax.text(x + 0.018, 0.825, value, fontsize=value_size, fontweight="bold", color=color, va="center")
        ax.text(x + 0.018, 0.793, label, fontsize=10.5, color=MUTED, va="center")

    stages = [
        ("DATA", "Official archives\nChecksums and timestamps\nGap and bar validation", BLUE, BLUE_LIGHT),
        ("SEARCH", "Reusable caches\nDeterministic IDs\nRestartable stages", GOLD, GOLD_LIGHT),
        ("SIMULATION", "Causal signal timing\nCosts and fill stress\nShared cash replay", ORANGE, ORANGE_LIGHT),
        ("VALIDATION", "Neighbour surfaces\nSeparate time windows\nRisk and concentration", GREEN, GREEN_LIGHT),
        ("DECISION", "Frozen configurations\nBurned evaluation periods\nPromote, revise or reject", BLUE, BLUE_LIGHT),
    ]
    xs = [0.045, 0.235, 0.425, 0.615, 0.805]
    for index, (x, stage) in enumerate(zip(xs, stages)):
        title, detail, color, light = stage
        box(ax, x, 0.42, 0.15, 0.255, face=PAPER, edge=LINE, radius=0.012)
        box(ax, x + 0.012, 0.615, 0.126, 0.045, face=light, edge=color, radius=0.008)
        ax.text(x + 0.075, 0.637, title, fontsize=11, fontweight="bold", color=color, ha="center", va="center")
        ax.text(x + 0.075, 0.575, detail, fontsize=9.4, color=INK, ha="center", va="top", linespacing=1.65)
        if index < len(stages) - 1:
            ax.annotate(
                "",
                xy=(xs[index + 1] - 0.008, 0.548),
                xytext=(x + 0.158, 0.548),
                xycoords=ax.transAxes,
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.6),
            )

    ax.text(0.045, 0.35, "The problems that forced the system to change", fontsize=14.5, fontweight="bold")
    problems = [
        ("Data gaps", "Invalidate features until a full window exists"),
        ("Future information", "Shift features to their true availability time"),
        ("Lucky optima", "Compare surfaces instead of one point"),
        ("Optimistic fills", "Stress fills, fees and slippage"),
        ("Imaginary capital", "Replay full, partial and skipped funding"),
    ]
    for x, (problem, response) in zip(xs, problems):
        ax.plot([x + 0.006, x + 0.006], [0.195, 0.302], transform=ax.transAxes, color=ORANGE, lw=3)
        ax.text(x + 0.018, 0.292, problem, fontsize=11.5, fontweight="bold", va="top")
        ax.text(x + 0.018, 0.255, fill(response, width=25), fontsize=8.7, color=MUTED, va="top", linespacing=1.35)

    ax.text(
        0.045,
        0.105,
        "The difficult part was not producing a high return. It was making every result traceable, causal and easy to reject when the evidence changed.",
        fontsize=12.5,
        color=INK,
    )
    save(fig, "06_public_research_loop.png")


def draw_problem_map() -> None:
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.04, 0.945, "Problems that changed the research process", fontsize=29, fontweight="bold")
    ax.text(
        0.04,
        0.905,
        "Each issue became a permanent test in the pipeline instead of a footnote after the result",
        fontsize=13.5,
        color=MUTED,
    )

    columns = [(0.04, 0.26, "PROBLEM FOUND"), (0.335, 0.26, "WHY IT MATTERED"), (0.63, 0.33, "WHAT CHANGED")]
    for x, width, title in columns:
        ax.text(x, 0.845, title, fontsize=11.5, fontweight="bold", color=MUTED)
        ax.plot([x, x + width], [0.83, 0.83], transform=ax.transAxes, color=LINE, lw=1.3)

    rows = [
        ("Feature available too early", "Future information entered decisions", "Availability shift and raw signal regeneration", RED, RED_LIGHT),
        ("One grid winner dominated", "A large search rewarded chance", "Neighbour surfaces and separate time windows", GOLD, GOLD_LIGHT),
        ("Touched limit counted as a fill", "Execution looked more certain than it was", "Fill overshoot, fee and slippage stress", ORANGE, ORANGE_LIGHT),
        ("Event equity hid open losses", "Drawdown was understated", "Minute mark to market and low price envelope", BLUE, BLUE_LIGHT),
        ("Standalone signals shared imaginary cash", "The combined return could not be funded", "Full, partial and skipped allocation replay", GREEN, GREEN_LIGHT),
        ("Selected history stayed attractive", "The evidence still did not generalise", "Frozen future window and candidate rejection", RED, RED_LIGHT),
    ]
    y_values = [0.745, 0.64, 0.535, 0.43, 0.325, 0.22]
    for y, row in zip(y_values, rows):
        problem, impact, change, color, light = row
        box(ax, 0.04, y - 0.055, 0.26, 0.082, face=light, edge=color, radius=0.008)
        ax.text(
            0.055,
            y - 0.012,
            fill(problem, width=31),
            fontsize=10.3,
            fontweight="bold",
            color=INK,
            va="center",
            linespacing=1.15,
        )
        box(ax, 0.335, y - 0.055, 0.26, 0.082, face=PAPER, edge=LINE, radius=0.008)
        ax.text(0.35, y - 0.012, fill(impact, width=33), fontsize=10.0, color=INK, va="center", linespacing=1.15)
        box(ax, 0.63, y - 0.055, 0.33, 0.082, face=PAPER, edge=color, radius=0.008)
        ax.text(
            0.645,
            y - 0.012,
            fill(change, width=43),
            fontsize=10.0,
            fontweight="bold",
            color=color,
            va="center",
            linespacing=1.15,
        )
        ax.annotate("", xy=(0.328, y - 0.012), xytext=(0.307, y - 0.012), xycoords=ax.transAxes,
                    arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.4))
        ax.annotate("", xy=(0.623, y - 0.012), xytext=(0.602, y - 0.012), xycoords=ax.transAxes,
                    arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.4))

    box(ax, 0.04, 0.07, 0.92, 0.075, face=RED_LIGHT, edge=RED, radius=0.01)
    ax.text(0.06, 0.107, "Decision", fontsize=12.5, fontweight="bold", color=RED, va="center")
    ax.text(
        0.135,
        0.107,
        "The corrected candidate failed the clean future test and was rejected for deployment.",
        fontsize=12.5,
        color=INK,
        va="center",
    )
    save(fig, "07_public_robustness_gates.png")


def draw_audit_path() -> None:
    fig, ax = plt.subplots(figsize=(16, 7.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.045, 0.92, "Causal audit and decision path", fontsize=29, fontweight="bold")
    ax.text(
        0.045,
        0.865,
        "Exact reproduction was used as a control. It was not treated as evidence that the original timing was correct.",
        fontsize=13.5,
        color=MUTED,
    )

    stages = [
        ("1", "Exact reproduction", "PASS", "Recovered original\nbehaviour from raw\nmarket data", GREEN, GREEN_LIGHT),
        ("2", "Availability audit", "ISSUE FOUND", "A feature appeared\nbefore its inputs\nexisted", RED, RED_LIGHT),
        ("3", "Causal regeneration", "PASS", "Moved the feature to\nits first valid\ntimestamp", GREEN, GREEN_LIGHT),
        ("4", "Candidate frozen", "PASS", "No changes after the\nlater window was\nopened", GREEN, GREEN_LIGHT),
        ("5", "Future only test", "FAIL", "The corrected candidate\nfailed its predefined\ngate", RED, RED_LIGHT),
        ("6", "Deployment decision", "REJECT", "Research continues\nwithout promoting\nthe candidate", RED, RED_LIGHT),
    ]
    xs = [0.042, 0.195, 0.348, 0.501, 0.654, 0.807]
    y = 0.39
    ax.plot([0.075, 0.925], [y + 0.19, y + 0.19], transform=ax.transAxes, color=LINE, lw=4, zorder=0)
    for index, (x, stage) in enumerate(zip(xs, stages)):
        number, title, status, detail, color, light = stage
        ax.scatter([x + 0.065], [y + 0.19], transform=ax.transAxes, s=520, color=color, edgecolor=BG, linewidth=3, zorder=3)
        ax.text(x + 0.065, y + 0.19, number, fontsize=11, fontweight="bold", color=PAPER, ha="center", va="center", zorder=4)
        box(ax, x, y - 0.09, 0.14, 0.23, face=PAPER, edge=LINE, radius=0.01)
        ax.text(x + 0.07, y + 0.09, title, fontsize=9.7, fontweight="bold", ha="center", va="center")
        box(ax, x + 0.03, y + 0.01, 0.08, 0.04, face=light, edge=color, radius=0.007)
        ax.text(x + 0.07, y + 0.03, status, fontsize=8.6, fontweight="bold", color=color, ha="center", va="center")
        ax.text(x + 0.07, y - 0.025, detail, fontsize=8.1, color=MUTED, ha="center", va="top", linespacing=1.25)

    box(ax, 0.045, 0.095, 0.905, 0.1, face=BLUE_LIGHT, edge=BLUE, radius=0.01)
    ax.text(
        0.065,
        0.145,
        "Main lesson: reproducing a backtest proves that the code path can be recovered.\nIt does not prove that the information set was available in real time.",
        fontsize=11.2,
        color=INK,
        va="center",
        linespacing=1.35,
    )
    save(fig, "08_causal_audit_path.png")


def main() -> None:
    setup()
    draw_system_overview()
    draw_problem_map()
    draw_audit_path()


if __name__ == "__main__":
    main()
