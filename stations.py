#!/usr/bin/env python3
"""Generate cliamp TOML/M3U from mounts that return audio/mpeg."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Verified 200 audio/mpeg on d.liveatc.net (VLC UA, follow redirects).
# Generic names like kmia_app 404; LiveATC uses feeder-suffixed mounts.
STATIONS = [
    # Miami — TWR / GND / APP / ATIS
    ("kmia3_twr", "KMIA Tower", "Miami International", ["florida"]),
    ("kmia3_gnd", "KMIA Ground", "Miami International", ["florida"]),
    ("kmia3_gnd2", "KMIA Ground South (9/27/30)", "Miami International", ["florida"]),
    ("kmia3_app_11945", "KMIA Approach 119.45", "Miami International", ["florida"]),
    ("kmia3_app_1205", "KMIA Approach/Departure 120.5", "Miami International", ["florida"]),
    ("kmia3_app_12485", "KMIA Approach 124.85", "Miami International", ["florida"]),
    ("kmia3_app_12575", "KMIA Approach 125.75", "Miami International", ["florida"]),
    ("kmia3_app_133775", "KMIA Approach KFLL 133.775", "Miami International", ["florida"]),
    ("kmia3_atis_arr", "KMIA ATIS Arrival", "Miami International", ["florida", "atis"]),
    # Other hubs that currently stream
    ("kjfk_twr", "KJFK Tower", "John F. Kennedy", ["us-hubs"]),
    ("kjfk9_s", "KJFK Ground/Tower", "John F. Kennedy", ["us-hubs"]),
    ("klga_twr", "KLGA Tower", "LaGuardia", ["us-hubs"]),
    ("kewr_twr", "KEWR Tower", "Newark Liberty", ["us-hubs"]),
    ("klax_twr", "KLAX Tower", "Los Angeles International", ["us-hubs"]),
    ("katl_twr", "KATL Tower", "Hartsfield-Jackson Atlanta", ["us-hubs"]),
    ("ksfo_twr", "KSFO Tower", "San Francisco International", ["us-hubs"]),
    ("ksfo_atis", "KSFO ATIS", "San Francisco International", ["atis", "us-hubs"]),
]


def url(mount: str) -> str:
    return f"http://d.liveatc.net/{mount}"


def genre(groups: list[str]) -> str:
    if "atis" in groups:
        return "ATIS"
    if "center" in groups:
        return "Center"
    return "ATC"


def toml_track(mount: str, title: str, artist: str, groups: list[str]) -> str:
    return "\n".join(
        [
            "[[track]]",
            f'path = "{url(mount)}"',
            f'title = "{title}"',
            f'artist = "{artist}"',
            'album = "Live ATC"',
            f'genre = "{genre(groups)}"',
            "realtime = true",
            "",
        ]
    )


def write_playlist(name: str, rows) -> None:
    (ROOT / "playlists" / f"{name}.toml").write_text(
        "".join(toml_track(*s) for s in rows)
    )


def main() -> None:
    playlists = ROOT / "playlists"
    playlists.mkdir(exist_ok=True)
    write_playlist("Live ATC", STATIONS)
    write_playlist("atc", STATIONS)
    write_playlist("florida", [s for s in STATIONS if "florida" in s[3]])
    write_playlist("atis", [s for s in STATIONS if "atis" in s[3]])
    write_playlist("us-hubs", [s for s in STATIONS if "us-hubs" in s[3]])
    (playlists / "atc.m3u").write_text(
        "#EXTM3U\n"
        + "".join(f"#EXTINF:-1,{a} — {t}\n{url(m)}\n" for m, t, a, _ in STATIONS)
    )
    print(f"{len(STATIONS)} stations")


if __name__ == "__main__":
    main()
