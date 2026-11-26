# The Moon Gets One Star

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/cunong05/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/cunong05/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)

This is my entry for the make.fun bounty "The Moon Gets One Star": a
one-star review of the Moon, written as if it were a product that keeps
letting its owner down.

## Entry

> 1 star. Only works nights, vanishes for a week every month, and still floods my beach twice a day. Would not recommend.

## How to run

```sh
python3 main.py
```

The script writes the entry to `/output/entry.txt` (creating the
`/output` folder first if it is missing) and prints the character count.
It also checks that the text is not empty, stays on a single line, and
is between 1 and 120 characters long; if any of those checks fail, it
stops with a clear error instead of writing a bad entry.

## Notes

The program uses only the Python standard library. It needs no extra
packages, makes no network requests, and uses no secrets or credentials.
