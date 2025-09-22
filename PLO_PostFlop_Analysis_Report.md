# PLO Post-Flop Analysis Report

## Executive Summary

This report analyzes Pot Limit Omaha post-flop scenarios across different board textures,
stack depths, and playing styles. The analysis compares win rates between Random, Tight,
and Aggressive strategies to understand how different factors affect post-flop performance.

## Methodology

- **Game Format**: Heads-up Pot Limit Omaha
- **Scenarios Tested**: 4 board texture types × 3 stack depths × 6 agent matchups
- **Hands per Scenario**: 1,000 hands
- **Win Rate Metric**: Big blinds won per 100 hands
- **Confidence Intervals**: 95% confidence level

## Board Texture Categories

1. **Dry Ace High**: A-high boards with disconnected low cards
2. **Wet Connected**: Connected boards with straight/flush possibilities
3. **Paired Board**: Boards with a pocket pair
4. **Flush Draw**: Three cards of the same suit

## Stack Depth Categories

- **Shallow (30BB)**: Short-stack play
- **Medium (100BB)**: Standard stack depth
- **Deep (200BB)**: Deep-stack play

## Results Summary

### Win Rates by Board Texture

| Board Type | Avg Win Rate (BB/100) | Std Dev | Sample Size |
|------------|----------------------|---------|-------------|
| Dry Ace High | 0.29 | 2.56 | 18 |
| Wet Connected | 0.12 | 2.18 | 18 |
| Paired Board | -0.48 | 2.83 | 18 |
| Flush Draw | 0.48 | 2.18 | 18 |

### Win Rates by Stack Depth

| Stack Depth | Avg Win Rate (BB/100) | Std Dev | Sample Size |
|-------------|----------------------|---------|-------------|
| Shallow 30Bb | 0.40 | 2.76 | 24 |
| Medium 100Bb | 0.05 | 1.85 | 24 |
| Deep 200Bb | -0.14 | 2.69 | 24 |

### Win Rates by Agent Matchup

| Matchup | Avg Win Rate (BB/100) | Std Dev | Sample Size |
|---------|----------------------|---------|-------------|
| Random vs Tight | 0.78 | 1.73 | 12 |
| Random vs Aggressive | -0.58 | 1.85 | 12 |
| Tight vs Random | -1.79 | 1.50 | 12 |
| Tight vs Aggressive | -1.86 | 2.07 | 12 |
| Aggressive vs Random | 1.67 | 1.77 | 12 |
| Aggressive vs Tight | 2.40 | 2.17 | 12 |

## Key Findings

- **Overall Win Rate Range**: -5.78 to 5.98 BB/100
- **Average Win Rate**: 0.10 BB/100
- **Standard Deviation**: 2.48 BB/100
- **Most Profitable Board Type**: Flush Draw (0.48 BB/100)
- **Least Profitable Board Type**: Paired Board (-0.48 BB/100)
- **Most Profitable Stack Depth**: Shallow 30Bb (0.40 BB/100)

## Detailed Results

| Scenario | Board | Stack | Matchup | Win Rate | Confidence Interval | Hands |
|----------|-------|-------|---------|----------|-------------------|-------|
| paired_board_shallow_30bb_Aggressive_vs_Tight | paired_board | shallow_30bb | Aggressive vs Tight | 5.98 | [5.05, 6.91] | 1000 |
| wet_connected_deep_200bb_Aggressive_vs_Tight | wet_connected | deep_200bb | Aggressive vs Tight | 5.65 | [4.72, 6.58] | 1000 |
| dry_ace_high_shallow_30bb_Random_vs_Tight | dry_ace_high | shallow_30bb | Random vs Tight | 4.42 | [3.49, 5.35] | 1000 |
| paired_board_deep_200bb_Aggressive_vs_Random | paired_board | deep_200bb | Aggressive vs Random | 4.00 | [3.07, 4.93] | 1000 |
| dry_ace_high_deep_200bb_Aggressive_vs_Tight | dry_ace_high | deep_200bb | Aggressive vs Tight | 3.79 | [2.86, 4.72] | 1000 |
| dry_ace_high_deep_200bb_Aggressive_vs_Random | dry_ace_high | deep_200bb | Aggressive vs Random | 3.77 | [2.84, 4.70] | 1000 |
| dry_ace_high_shallow_30bb_Aggressive_vs_Random | dry_ace_high | shallow_30bb | Aggressive vs Random | 3.73 | [2.80, 4.66] | 1000 |
| wet_connected_shallow_30bb_Aggressive_vs_Tight | wet_connected | shallow_30bb | Aggressive vs Tight | 3.65 | [2.72, 4.58] | 1000 |
| flush_draw_deep_200bb_Aggressive_vs_Tight | flush_draw | deep_200bb | Aggressive vs Tight | 3.51 | [2.58, 4.44] | 1000 |
| flush_draw_medium_100bb_Aggressive_vs_Random | flush_draw | medium_100bb | Aggressive vs Random | 3.05 | [2.12, 3.98] | 1000 |
| flush_draw_shallow_30bb_Random_vs_Tight | flush_draw | shallow_30bb | Random vs Tight | 2.87 | [1.94, 3.80] | 1000 |
| flush_draw_shallow_30bb_Aggressive_vs_Tight | flush_draw | shallow_30bb | Aggressive vs Tight | 2.68 | [1.75, 3.61] | 1000 |
| wet_connected_shallow_30bb_Aggressive_vs_Random | wet_connected | shallow_30bb | Aggressive vs Random | 2.54 | [1.61, 3.47] | 1000 |
| dry_ace_high_shallow_30bb_Aggressive_vs_Tight | dry_ace_high | shallow_30bb | Aggressive vs Tight | 2.48 | [1.55, 3.41] | 1000 |
| dry_ace_high_shallow_30bb_Random_vs_Aggressive | dry_ace_high | shallow_30bb | Random vs Aggressive | 2.27 | [1.34, 3.20] | 1000 |
| flush_draw_medium_100bb_Random_vs_Tight | flush_draw | medium_100bb | Random vs Tight | 2.09 | [1.16, 3.02] | 1000 |
| paired_board_medium_100bb_Random_vs_Tight | paired_board | medium_100bb | Random vs Tight | 1.89 | [0.96, 2.81] | 1000 |
| flush_draw_medium_100bb_Random_vs_Aggressive | flush_draw | medium_100bb | Random vs Aggressive | 1.84 | [0.91, 2.76] | 1000 |
| paired_board_medium_100bb_Aggressive_vs_Random | paired_board | medium_100bb | Aggressive vs Random | 1.82 | [0.89, 2.75] | 1000 |
| flush_draw_shallow_30bb_Aggressive_vs_Random | flush_draw | shallow_30bb | Aggressive vs Random | 1.65 | [0.72, 2.58] | 1000 |
| wet_connected_medium_100bb_Aggressive_vs_Random | wet_connected | medium_100bb | Aggressive vs Random | 1.31 | [0.38, 2.24] | 1000 |
| paired_board_deep_200bb_Aggressive_vs_Tight | paired_board | deep_200bb | Aggressive vs Tight | 1.09 | [0.16, 2.02] | 1000 |
| flush_draw_medium_100bb_Aggressive_vs_Tight | flush_draw | medium_100bb | Aggressive vs Tight | 0.98 | [0.05, 1.91] | 1000 |
| wet_connected_medium_100bb_Random_vs_Tight | wet_connected | medium_100bb | Random vs Tight | 0.74 | [-0.18, 1.67] | 1000 |
| flush_draw_medium_100bb_Tight_vs_Random | flush_draw | medium_100bb | Tight vs Random | 0.67 | [-0.26, 1.60] | 1000 |
| paired_board_medium_100bb_Random_vs_Aggressive | paired_board | medium_100bb | Random vs Aggressive | 0.65 | [-0.28, 1.58] | 1000 |
| wet_connected_medium_100bb_Aggressive_vs_Tight | wet_connected | medium_100bb | Aggressive vs Tight | 0.61 | [-0.32, 1.54] | 1000 |
| flush_draw_medium_100bb_Tight_vs_Aggressive | flush_draw | medium_100bb | Tight vs Aggressive | 0.61 | [-0.32, 1.54] | 1000 |
| wet_connected_medium_100bb_Random_vs_Aggressive | wet_connected | medium_100bb | Random vs Aggressive | 0.59 | [-0.34, 1.52] | 1000 |
| paired_board_shallow_30bb_Random_vs_Tight | paired_board | shallow_30bb | Random vs Tight | 0.59 | [-0.34, 1.52] | 1000 |
| wet_connected_deep_200bb_Aggressive_vs_Random | wet_connected | deep_200bb | Aggressive vs Random | 0.58 | [-0.35, 1.51] | 1000 |
| flush_draw_deep_200bb_Random_vs_Aggressive | flush_draw | deep_200bb | Random vs Aggressive | 0.49 | [-0.44, 1.42] | 1000 |
| dry_ace_high_medium_100bb_Random_vs_Aggressive | dry_ace_high | medium_100bb | Random vs Aggressive | 0.35 | [-0.58, 1.28] | 1000 |
| dry_ace_high_medium_100bb_Random_vs_Tight | dry_ace_high | medium_100bb | Random vs Tight | 0.15 | [-0.78, 1.08] | 1000 |
| wet_connected_medium_100bb_Tight_vs_Aggressive | wet_connected | medium_100bb | Tight vs Aggressive | -0.02 | [-0.95, 0.91] | 1000 |
| dry_ace_high_deep_200bb_Random_vs_Tight | dry_ace_high | deep_200bb | Random vs Tight | -0.04 | [-0.97, 0.89] | 1000 |
| dry_ace_high_medium_100bb_Tight_vs_Aggressive | dry_ace_high | medium_100bb | Tight vs Aggressive | -0.06 | [-0.99, 0.87] | 1000 |
| flush_draw_deep_200bb_Random_vs_Tight | flush_draw | deep_200bb | Random vs Tight | -0.15 | [-1.08, 0.78] | 1000 |
| paired_board_medium_100bb_Aggressive_vs_Tight | paired_board | medium_100bb | Aggressive vs Tight | -0.30 | [-1.23, 0.63] | 1000 |
| wet_connected_deep_200bb_Tight_vs_Random | wet_connected | deep_200bb | Tight vs Random | -0.30 | [-1.23, 0.63] | 1000 |
| dry_ace_high_medium_100bb_Aggressive_vs_Random | dry_ace_high | medium_100bb | Aggressive vs Random | -0.35 | [-1.28, 0.58] | 1000 |
| paired_board_deep_200bb_Random_vs_Tight | paired_board | deep_200bb | Random vs Tight | -0.36 | [-1.29, 0.57] | 1000 |
| wet_connected_deep_200bb_Random_vs_Tight | wet_connected | deep_200bb | Random vs Tight | -0.38 | [-1.31, 0.55] | 1000 |
| flush_draw_deep_200bb_Tight_vs_Random | flush_draw | deep_200bb | Tight vs Random | -0.38 | [-1.31, 0.55] | 1000 |
| wet_connected_shallow_30bb_Tight_vs_Aggressive | wet_connected | shallow_30bb | Tight vs Aggressive | -0.45 | [-1.38, 0.48] | 1000 |
| wet_connected_deep_200bb_Tight_vs_Aggressive | wet_connected | deep_200bb | Tight vs Aggressive | -0.46 | [-1.39, 0.47] | 1000 |
| flush_draw_deep_200bb_Aggressive_vs_Random | flush_draw | deep_200bb | Aggressive vs Random | -0.48 | [-1.41, 0.44] | 1000 |
| dry_ace_high_shallow_30bb_Tight_vs_Random | dry_ace_high | shallow_30bb | Tight vs Random | -0.51 | [-1.44, 0.42] | 1000 |
| dry_ace_high_shallow_30bb_Tight_vs_Aggressive | dry_ace_high | shallow_30bb | Tight vs Aggressive | -0.69 | [-1.62, 0.24] | 1000 |
| paired_board_shallow_30bb_Tight_vs_Random | paired_board | shallow_30bb | Tight vs Random | -0.71 | [-1.64, 0.22] | 1000 |
| paired_board_deep_200bb_Random_vs_Aggressive | paired_board | deep_200bb | Random vs Aggressive | -0.98 | [-1.91, -0.05] | 1000 |
| paired_board_shallow_30bb_Random_vs_Aggressive | paired_board | shallow_30bb | Random vs Aggressive | -1.23 | [-2.16, -0.30] | 1000 |
| flush_draw_shallow_30bb_Tight_vs_Random | flush_draw | shallow_30bb | Tight vs Random | -1.24 | [-2.17, -0.31] | 1000 |
| flush_draw_shallow_30bb_Tight_vs_Aggressive | flush_draw | shallow_30bb | Tight vs Aggressive | -1.26 | [-2.19, -0.33] | 1000 |
| dry_ace_high_medium_100bb_Aggressive_vs_Tight | dry_ace_high | medium_100bb | Aggressive vs Tight | -1.35 | [-2.28, -0.42] | 1000 |
| wet_connected_shallow_30bb_Random_vs_Aggressive | wet_connected | shallow_30bb | Random vs Aggressive | -1.43 | [-2.36, -0.50] | 1000 |
| paired_board_shallow_30bb_Aggressive_vs_Random | paired_board | shallow_30bb | Aggressive vs Random | -1.59 | [-2.52, -0.66] | 1000 |
| dry_ace_high_deep_200bb_Tight_vs_Aggressive | dry_ace_high | deep_200bb | Tight vs Aggressive | -1.71 | [-2.64, -0.78] | 1000 |
| wet_connected_shallow_30bb_Random_vs_Tight | wet_connected | shallow_30bb | Random vs Tight | -2.48 | [-3.41, -1.55] | 1000 |
| paired_board_deep_200bb_Tight_vs_Random | paired_board | deep_200bb | Tight vs Random | -2.50 | [-3.43, -1.57] | 1000 |
| wet_connected_deep_200bb_Random_vs_Aggressive | wet_connected | deep_200bb | Random vs Aggressive | -2.52 | [-3.45, -1.59] | 1000 |
| wet_connected_shallow_30bb_Tight_vs_Random | wet_connected | shallow_30bb | Tight vs Random | -2.61 | [-3.54, -1.68] | 1000 |
| wet_connected_medium_100bb_Tight_vs_Random | wet_connected | medium_100bb | Tight vs Random | -2.94 | [-3.86, -2.01] | 1000 |
| dry_ace_high_deep_200bb_Tight_vs_Random | dry_ace_high | deep_200bb | Tight vs Random | -3.06 | [-3.99, -2.13] | 1000 |
| flush_draw_shallow_30bb_Random_vs_Aggressive | flush_draw | shallow_30bb | Random vs Aggressive | -3.25 | [-4.18, -2.32] | 1000 |
| paired_board_medium_100bb_Tight_vs_Aggressive | paired_board | medium_100bb | Tight vs Aggressive | -3.25 | [-4.18, -2.32] | 1000 |
| dry_ace_high_deep_200bb_Random_vs_Aggressive | dry_ace_high | deep_200bb | Random vs Aggressive | -3.72 | [-4.65, -2.79] | 1000 |
| paired_board_medium_100bb_Tight_vs_Random | paired_board | medium_100bb | Tight vs Random | -3.77 | [-4.70, -2.84] | 1000 |
| paired_board_deep_200bb_Tight_vs_Aggressive | paired_board | deep_200bb | Tight vs Aggressive | -4.14 | [-5.07, -3.21] | 1000 |
| dry_ace_high_medium_100bb_Tight_vs_Random | dry_ace_high | medium_100bb | Tight vs Random | -4.18 | [-5.11, -3.25] | 1000 |
| flush_draw_deep_200bb_Tight_vs_Aggressive | flush_draw | deep_200bb | Tight vs Aggressive | -5.08 | [-6.01, -4.15] | 1000 |
| paired_board_shallow_30bb_Tight_vs_Aggressive | paired_board | shallow_30bb | Tight vs Aggressive | -5.78 | [-6.71, -4.85] | 1000 |

## Technical Notes

- Analysis performed using the PokerRL-Omaha framework
- Simple strategy agents used for comparison (Random, Tight, Aggressive)
- Win rates normalized to BB per 100 hands using EV_NORMALIZER
- Statistical significance calculated with 95% confidence intervals
