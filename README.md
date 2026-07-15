# Adaptive Parameter Optimisation Algorithm

This repository is the public part of a larger private research project I have been working on for months. The private project is about building and stress testing adaptive trading systems. The public version is deliberately not a copyable strategy. It is meant to show the research process, the diagnostics, the mistakes I tried to avoid and the way I think about turning a rough trading idea into something that can actually be tested.

The project started from a simple problem. A fixed mean reversion setup can look good in one market and then fall apart as soon as costs, exits or the market regime change. So instead of asking whether one manually chosen parameter set worked, I started asking whether the system could research the market first. That means looking across many possible settings, finding regions that behave consistently, checking whether the result survives neighbouring parameters, and then asking if the trade logic still makes sense after realistic costs and worse execution assumptions.

I am not publishing the exact private strategy, selected parameters, search domains, sleeve structure, execution rules, live setup or final candidate details. That is where the edge would be. What I am publishing is the research layer around it: how I approach parameter search, how I think about overfitting, what kind of diagnostics I built, and what I learned from trying to make the process less fragile.

![Public research loop](reports/readme_main_showcase/06_public_research_loop.png)

The most important idea in the project is that the useful object is not one perfect parameter point. A single point can be luck, especially if the search space is large enough. I care more about parameter islands. By that I mean areas where nearby settings behave in a similar way. If a candidate only works at one tiny coordinate and collapses immediately around it, I do not trust it. If a wider region keeps working after the assumptions are stressed, it becomes more interesting.

This changed how I looked at the whole problem. The hard part was not only coding a backtest. The hard part was stopping the research process from fooling me. Every extra parameter, timeframe, symbol, filter or exit rule gives the search more chances to find something that looks amazing by accident. So I started treating the search itself as something that needs controls. I wanted to see the shape of the result, not only the best row in a table.

![Public robustness gates](reports/readme_main_showcase/07_public_robustness_gates.png)

The private version goes much further than a fixed moving average test, but the public explanation stays high level on purpose. Conceptually, the system studies how price behaves relative to a changing reference point, how often similar setups historically resolved well, how long successful and failed trades usually took, and how much of the result survives after costs and execution assumptions are made worse. It also has to deal with a problem that becomes very real once several signals compete for the same capital: sometimes the best decision is not just whether a signal is good, but whether it is better than another signal already using the money.

That last part taught me a lot. A strategy can have many promising signals and still waste capital if the allocation logic is weak. A trade can be a good signal but a bad use of capital at that moment. A time stop can protect against large downside in one case and cut a later winner in another. A beautiful equity curve can depend too much on one regime, one symbol or one cluster of trades. Those are the kinds of issues I wanted the research process to expose instead of hiding.

The public visuals use simplified or older examples to show the concept without revealing the private candidate. The dense surface below is useful because it makes the search space visible. It lets you see whether the result looks like a broader region or a sharp isolated spike.

<p align="center">
  <img src="reports/dense_parameter_surface_xagusd/XAGUSD_sum_net_pct_dense_contour_map.png" alt="Dense parameter contour map" width="850">
</p>

There is also an interactive version of the parameter surface here:

[Open the interactive parameter surface](https://romanmski.github.io/Adaptive_Parameter_Optimisation_Algorithm/visuals/xagusd_parameter_surface.html)

Another thing I learned is that exits deserve as much attention as entries. Some bad looking trades were not bad because the signal was useless. They were bad because the exit logic did not match the path that followed. Other trades looked promising but only because the assumed fill was too generous. That pushed me toward checking holding time distributions, successful and failed trade paths, take profit behaviour, drawdown and cost sensitivity instead of only looking at final return.

<p align="center">
  <img src="reports/readme_main_showcase/03_best_vs_worst_actual_trade_story.png" alt="Best and worst trade examples" width="850">
</p>

I also wanted the project to show negative evidence. If a workflow only shows the market where it worked best, it is not very useful. The cross market diagnostics are there because a research process should be able to say no. A setup failing somewhere is not embarrassing if it helps define where the idea is fragile.

<p align="center">
  <img src="reports/readme_main_showcase/04_cross_market_result_by_symbol.png" alt="Cross market result by symbol" width="850">
</p>

The risk diagnostics are part of the same idea. I do not want to judge a candidate only by one headline return number. I want to know how it behaved through drawdowns, how sensitive it was to costs, whether the profit factor still made sense, and whether the result depended too heavily on one market condition. This is also why the private project keeps separate run artifacts and audit notes. If I cannot reconstruct why a result happened, I do not want to trust it.

<p align="center">
  <img src="reports/readme_main_showcase/05_risk_diagnostics_by_symbol.png" alt="Risk diagnostics by symbol" width="850">
</p>

For recruiters or anyone reading this as a portfolio project, the main point is not that this repository contains a ready to run trading bot. It does not. The useful signal is that I can take a messy idea, break it into testable parts, build visual diagnostics, think about overfitting and execution realism, and keep improving the research process when the first version is too naive.

The project also changed how I think about quantitative research. I became much more skeptical of clean backtests, isolated winners and results that only look good because of one period. I learned to care more about neighbour stability, cost stress, drawdown shape, skipped opportunities, capital competition and whether a candidate can be regenerated from new data without looking into the future. That is the part I want this public repository to show.

This is not financial advice and it should not be read as proof of future profitability. It is a redacted research showcase for an ongoing private project.

The stack behind the public work is mainly Python, pandas, NumPy, matplotlib, Plotly, parameter surface analysis, backtest diagnostics, statistical testing, stress testing and research visualization.
