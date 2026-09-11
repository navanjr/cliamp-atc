# cliamp-atc

One **[cliamp](https://github.com/bjarneo/cliamp)** playlist of live ATC: Miami plus a few busy US hubs.

Streams are [LiveATC.net](https://www.liveatc.net/) Icecast mounts. Not affiliated with LiveATC. Personal listening only; follow their [terms](https://www.liveatc.net/).

cliamp has no ATC provider plugin. Two ways to see the feeds:

**Radio pane (`R`)** — `radios.toml`. Each frequency is its own station (Enter plays that one stream).

**Local Playlists (change SRC off Radio)** — `playlists/Live ATC.toml`. One playlist, all frequencies; `>` / `<` skip Tower → Approach → ATIS. In the player, Tab to **SRC** and switch from Radio to Local Playlists, or `p` for the playlist manager.

## Install

```sh
mkdir -p ~/.config/cliamp/playlists
curl -fsSL https://raw.githubusercontent.com/navanjr/cliamp-atc/main/radios.toml \
  -o ~/.config/cliamp/radios.toml
curl -fsSL https://raw.githubusercontent.com/navanjr/cliamp-atc/main/playlists/Live%20ATC.toml \
  -o ~/.config/cliamp/playlists/"Live ATC.toml"
```

Restart cliamp (or `Ctrl+R` on Radio). Radio → **Stations** lists the feeds. SRC → Local Playlists → **Live ATC** is the combined queue.

Optional subsets: `florida.toml`, `atis.toml`, `us-hubs.toml`.

One-shot:

```sh
cliamp https://raw.githubusercontent.com/navanjr/cliamp-atc/main/playlists/atc.m3u
```

## Why old URLs said Stopped / 404

LiveATC feeder names are not `kmia_app`. Current Miami audio is on mounts like `kmia3_twr` and `kmia3_app_12485`. This repo only lists mounts that returned `audio/mpeg` when last checked.

Center/ARTCC (ZMA, etc.) uses sector-specific mount names that change often; none of the short names (`zma`, `zma_ctr`) were live. Add a sector from the airport page on liveatc.net when you have a working mount.

## License

Playlist files are [MIT](LICENSE). LiveATC audio remains LiveATC.net's.
