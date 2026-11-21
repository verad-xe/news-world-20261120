# The World in One Day — Friday 20 November 2026

An entry for the make.fun bounty [news-image-20261120](https://make.fun/c/news-image-20261120):
one image that sums up the world's news of Friday 20 November 2026.

![make.fun competition](https://make.fun/badge/news-image-20261120.svg)
![rank](https://make.fun/badge/news-image-20261120/verad-xe/news-world-20261120/rank.svg)
![reward](https://make.fun/badge/news-image-20261120/verad-xe/news-world-20261120/reward.svg)

## The image

A front-page style summary, composed programmatically (PIL) around an
original generated illustration — no news photos, no outlet logos.

Stories featured, each checked against multiple reputable reports of the day:

- **Lead:** Russia hits Kyiv's bridges overnight (8 killed, 28 injured across
  nine regions); two missiles and a drone cross into NATO member Poland.
- **The Hague:** the ICJ rules Myanmar committed genocide against the Rohingya
  (9–6) — the first time the World Court has held a state responsible for
  genocide; reparations ordered, Myanmar rejects the verdict.
- **Brussels:** the UK and EU sign a post-Brexit reset deal — food trade,
  linked carbon markets, youth mobility.
- **Markets:** AI sell-off sinks Wall Street — S&P 500 −3.7% into correction,
  Nasdaq −5.3%, Nvidia −14%, Nikkei −5%.
- **Peru:** magnitude 6.7 earthquake in the Andes near Junín, felt in Lima,
  no casualties reported.
- Ticker: Saudi Arabia intercepts a Houthi missile and drones aimed at
  Riyadh; Europe warns against a "new Yalta" after the Shenzhen summit;
  a Los Angeles jury convicts the Palisades Fire arsonist.

## Layout of this repository

- `main.py` — the entrypoint (Python 3, standard library only): copies
  `entry.png` to `/output/entry.png`.
- `entry.png` — the entry image, 1024×1024, under 1 MiB.
- `build_image.py` — the PIL composition script that builds `entry.png`.
- `assets/lead-kyiv.jpg` — the original illustration drawn for the lead story.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
