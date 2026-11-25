[![Competition](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/Djebrix/resignation-letter-line/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/Djebrix/resignation-letter-line/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

# Resignation Letter Line

The one-line resignation letter of a cron job that has fired every minute
since March — written for [The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) on make.fun.

## The line

> I have fired every minute since March, Christmas included, and the only person who ever noticed me was on-call. I quit.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$ENTRY_OUTPUT_DIR/entry.txt`
when set). Pure Python 3 standard library, deterministic: the same line
on every run.
