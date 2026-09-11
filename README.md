# cliamp-atc

Curated **live air-traffic-control** streams for [cliamp](https://github.com/bjarneo/cliamp).

Streams come from [LiveATC.net](https://www.liveatc.net/) Icecast mounts (`d.liveatc.net`). This repo is not affiliated with LiveATC. Audio is theirs; use it for personal listening and follow their [terms](https://www.liveatc.net/).

cliamp has no third-party "ATC provider" plugin. This is a **Radio stations file** plus **TOML/M3U playlists** you can load in cliamp.

## Quick start

### Radio provider (`R` in cliamp)

```sh
mkdir -p ~/.config/cliamp
curl -fsSL https://raw.githubusercontent.com/navanjr/cliamp-atc/main/radios.toml \
  -o ~/.config/cliamp/radios.toml
cliamp --provider radio
```

Stations show under **Stations** next to the built-in cliamp radio. If you already have a `radios.toml`, merge the `[[station]]` blocks instead of overwriting.

### Local playlists (`Esc` / `b` in cliamp)

```sh
mkdir -p ~/.config/cliamp/playlists
curl -fsSL https://raw.githubusercontent.com/navanjr/cliamp-atc/main/playlists/atc.toml \
  -o ~/.config/cliamp/playlists/atc.toml
cliamp
```

Regional copies:

| File | Contents |
| --- | --- |
| `playlists/atc.toml` | Everything in this repo |
| `playlists/florida.toml` | KMIA, KFLL, KPBI, KMCO (TWR/APP/GND, ATIS, ZMA/ZJX) |
| `playlists/atis.toml` | ATIS loops |
| `playlists/center.toml` | ARTCC / Center |
| `playlists/us-hubs.toml` | Busy US Class B towers/approach (+ ATIS) |
| `playlists/international.toml` | Heathrow, Schiphol, Pearson, Vancouver |

Each track is a live Icecast URL with `realtime = true` so cliamp reconnects after pause.

### One-shot M3U

```sh
cliamp https://raw.githubusercontent.com/navanjr/cliamp-atc/main/playlists/atc.m3u
```

## Stream URLs

Official LiveATC listener format (Icecast on port 80):

```
http://d.liveatc.net/{mount}
```

Example: `http://d.liveatc.net/kmia_app`

Mount names change when LiveATC retitles a feed. If a station 404s, check the airport page on liveatc.net and update the mount.

## License

Playlist files in this repo are [MIT](LICENSE). LiveATC audio remains LiveATC.net's.
