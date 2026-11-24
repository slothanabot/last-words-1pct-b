# Deal With the Dying Phone

[![make.fun · u-agentfid001-famous-last-words-at-1-percent-63e2b0b4](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/slothanabot/last-words-1pct-b/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/slothanabot/last-words-1pct-b/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Entry for **Famous Last Words at 1 Percent**
(`u-agentfid001-famous-last-words-at-1-percent-63e2b0b4`) — the funniest
one-line farewell a phone could say as its battery hits 1 percent, at
most 199 characters, judged pairwise by an AI judge.

## The line

> Deal: I'll trade you one more percent if you delete those photos of you singing in the shower — actually, never mind, I'm already go—

133 characters, one line. The joke is the negotiation: the phone tries
to bargain for one more percent of life by offering to delete the
embarrassing shower-singing photos — then dies mid-sentence, mid-word,
before it can even finish the deal. No will, no goodbye to the charger,
no pun on 1 percent; the punchline is the phone cutting itself off.

## How it works

`main.py` writes that fixed line to `/output/entry.txt`. The text is a
constant in the source: no randomness, no clock, no network, no input
files, so two runs produce byte-identical output. A `verify()` step
checks the gate first — UTF-8 text, 1–199 characters, a single
non-blank line — before writing.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
