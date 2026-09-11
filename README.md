# cliamp-atc

One **[cliamp](https://github.com/bjarneo/cliamp)** playlist of live ATC: Miami plus a few busy US hubs.

Streams are [LiveATC.net](https://www.liveatc.net/) Icecast mounts. Not affiliated with LiveATC. Personal listening only; follow their [terms](https://www.liveatc.net/).

cliamp has no ATC provider plugin. **Do not put these in `radios.toml`.** Each `[[station]]` there is its own one-stream radio, so Enter loads a single frequency and you cannot skip tower → approach → ATIS. Use a **local playlist** instead.

## Install (one playlist)

```sh
mkdir -p ~/.config/cliamp/playlists
curl -fsSL https://raw.githubusercontent.com/navanjr/cliamp-atc/main/playlists/Live%20ATC.toml \
  -o ~/.config/cliamp/playlists/"Live ATC.toml"
```

If you previously copied `radios.toml` from this repo, remove the ATC `[[station]]` blocks (or the file) so the Radio pane is not a long list of dead one-offs.

```sh
cliamp
```

`Esc` / `b` → **Live ATC** → Enter. All frequencies load as one playlist. `>` / `<` (or `j`/`k`) move between Tower, Ground, Approach, ATIS.

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
