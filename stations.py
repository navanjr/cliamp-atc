#!/usr/bin/env python3
"""Generate cliamp TOML/M3U/radios.toml from the curated station list."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

# mount, title, artist, groups
STATIONS = [
    # Florida TWR/APP/GND
    ("kmia_app", "KMIA Approach", "Miami International", ["florida", "us-hubs"]),
    ("kmia_twr", "KMIA Tower", "Miami International", ["florida", "us-hubs"]),
    ("kmia_gnd", "KMIA Ground", "Miami International", ["florida", "us-hubs"]),
    ("kfll_app", "KFLL Approach", "Fort Lauderdale-Hollywood", ["florida"]),
    ("kfll_twr", "KFLL Tower", "Fort Lauderdale-Hollywood", ["florida"]),
    ("kpbi_app", "KPBI Approach", "Palm Beach International", ["florida"]),
    ("kpbi_twr", "KPBI Tower", "Palm Beach International", ["florida"]),
    ("kmco_twr", "KMCO Tower", "Orlando International", ["florida"]),
    # Florida ATIS
    ("kmia_atis", "KMIA ATIS", "Miami International", ["florida", "atis"]),
    ("kmia_atis_arr", "KMIA ATIS Arrival", "Miami International", ["florida", "atis"]),
    ("kmia_atis_dep", "KMIA ATIS Departure", "Miami International", ["florida", "atis"]),
    ("kfll_atis", "KFLL ATIS", "Fort Lauderdale-Hollywood", ["florida", "atis"]),
    ("kpbi_atis", "KPBI ATIS", "Palm Beach International", ["florida", "atis"]),
    ("kmco_atis", "KMCO ATIS", "Orlando International", ["florida", "atis"]),
    # Florida / nearby Center
    ("zma", "ZMA Miami Center", "Miami ARTCC", ["florida", "center"]),
    ("zma_ctr", "ZMA Miami Center (CTR)", "Miami ARTCC", ["florida", "center"]),
    ("kmia_zma", "ZMA / KMIA", "Miami ARTCC", ["florida", "center"]),
    ("zjx", "ZJX Jacksonville Center", "Jacksonville ARTCC", ["florida", "center"]),
    # US hubs TWR/APP
    ("kjfk_app", "KJFK Approach", "John F. Kennedy", ["us-hubs"]),
    ("kjfk_twr", "KJFK Tower", "John F. Kennedy", ["us-hubs"]),
    ("klga_twr", "KLGA Tower", "LaGuardia", ["us-hubs"]),
    ("kewr_twr", "KEWR Tower", "Newark Liberty", ["us-hubs"]),
    ("kbos_app", "KBOS Approach", "Boston Logan", ["us-hubs"]),
    ("kbos_twr", "KBOS Tower", "Boston Logan", ["us-hubs"]),
    ("klax_app", "KLAX Approach", "Los Angeles International", ["us-hubs"]),
    ("klax_twr", "KLAX Tower", "Los Angeles International", ["us-hubs"]),
    ("ksfo_app", "KSFO Approach", "San Francisco International", ["us-hubs"]),
    ("ksfo_twr", "KSFO Tower", "San Francisco International", ["us-hubs"]),
    ("kord_app", "KORD Approach", "Chicago O'Hare", ["us-hubs"]),
    ("kord_twr", "KORD Tower", "Chicago O'Hare", ["us-hubs"]),
    ("katl_app", "KATL Approach", "Hartsfield-Jackson Atlanta", ["us-hubs"]),
    ("katl_twr", "KATL Tower", "Hartsfield-Jackson Atlanta", ["us-hubs"]),
    ("kden_twr", "KDEN Tower", "Denver International", ["us-hubs"]),
    ("kdfw_twr", "KDFW Tower", "Dallas/Fort Worth", ["us-hubs"]),
    ("kiah_twr", "KIAH Tower", "Houston Intercontinental", ["us-hubs"]),
    ("kphx_twr", "KPHX Tower", "Phoenix Sky Harbor", ["us-hubs"]),
    ("ksea_twr", "KSEA Tower", "Seattle-Tacoma", ["us-hubs"]),
    ("klas_twr", "KLAS Tower", "Las Vegas Harry Reid", ["us-hubs"]),
    # US hubs ATIS
    ("kjfk_atis", "KJFK ATIS", "John F. Kennedy", ["atis", "us-hubs"]),
    ("klga_atis", "KLGA ATIS", "LaGuardia", ["atis"]),
    ("kewr_atis", "KEWR ATIS", "Newark Liberty", ["atis"]),
    ("kbos_atis", "KBOS ATIS", "Boston Logan", ["atis", "us-hubs"]),
    ("klax_atis", "KLAX ATIS", "Los Angeles International", ["atis", "us-hubs"]),
    ("ksfo_atis", "KSFO ATIS", "San Francisco International", ["atis", "us-hubs"]),
    ("kord_atis", "KORD ATIS", "Chicago O'Hare", ["atis", "us-hubs"]),
    ("katl_atis", "KATL ATIS", "Hartsfield-Jackson Atlanta", ["atis", "us-hubs"]),
    ("kden_atis", "KDEN ATIS", "Denver International", ["atis"]),
    ("kdfw_atis", "KDFW ATIS", "Dallas/Fort Worth", ["atis"]),
    ("kiah_atis", "KIAH ATIS", "Houston Intercontinental", ["atis"]),
    ("kphx_atis", "KPHX ATIS", "Phoenix Sky Harbor", ["atis"]),
    ("ksea_atis", "KSEA ATIS", "Seattle-Tacoma", ["atis"]),
    ("klas_atis", "KLAS ATIS", "Las Vegas Harry Reid", ["atis"]),
    # ARTCC / Center
    ("zny", "ZNY New York Center", "New York ARTCC", ["center"]),
    ("zdc", "ZDC Washington Center", "Washington ARTCC", ["center"]),
    ("zbw", "ZBW Boston Center", "Boston ARTCC", ["center"]),
    ("zau", "ZAU Chicago Center", "Chicago ARTCC", ["center"]),
    ("ztl", "ZTL Atlanta Center", "Atlanta ARTCC", ["center"]),
    ("zla", "ZLA Los Angeles Center", "Los Angeles ARTCC", ["center"]),
    ("zoa", "ZOA Oakland Center", "Oakland ARTCC", ["center"]),
    ("zse", "ZSE Seattle Center", "Seattle ARTCC", ["center"]),
    ("zdv", "ZDV Denver Center", "Denver ARTCC", ["center"]),
    ("zfw", "ZFW Fort Worth Center", "Fort Worth ARTCC", ["center"]),
    ("zhu", "ZHU Houston Center", "Houston ARTCC", ["center"]),
    ("zob", "ZOB Cleveland Center", "Cleveland ARTCC", ["center"]),
    ("zmp", "ZMP Minneapolis Center", "Minneapolis ARTCC", ["center"]),
    ("zkc", "ZKC Kansas City Center", "Kansas City ARTCC", ["center"]),
    ("zlc", "ZLC Salt Lake Center", "Salt Lake ARTCC", ["center"]),
    ("zab", "ZAB Albuquerque Center", "Albuquerque ARTCC", ["center"]),
    ("zme", "ZME Memphis Center", "Memphis ARTCC", ["center"]),
    ("zid", "ZID Indianapolis Center", "Indianapolis ARTCC", ["center"]),
    # International TWR
    ("egll_twr", "EGLL Tower", "London Heathrow", ["international"]),
    ("eham01_twr_main1", "EHAM Tower", "Amsterdam Schiphol", ["international"]),
    ("cyyz7", "CYYZ Tower", "Toronto Pearson", ["international"]),
    ("cyvr1_gnd_twr", "CYVR Ground/Tower", "Vancouver International", ["international"]),
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


def m3u_entry(mount: str, title: str, artist: str) -> str:
    return f"#EXTINF:-1,{artist} — {title}\n{url(mount)}\n"


def radios_station(mount: str, title: str, artist: str) -> str:
    return "\n".join(
        [
            "[[station]]",
            f'name = "{title} ({artist})"',
            f'url = "{url(mount)}"',
            "",
        ]
    )


def write_group(name: str, predicate) -> None:
    rows = [s for s in STATIONS if predicate(s)]
    (ROOT / "playlists" / f"{name}.toml").write_text(
        "".join(toml_track(*s) for s in rows)
    )


def main() -> None:
    playlists = ROOT / "playlists"
    playlists.mkdir(exist_ok=True)
    write_group("atc", lambda _: True)
    write_group("florida", lambda s: "florida" in s[3])
    write_group("us-hubs", lambda s: "us-hubs" in s[3])
    write_group("international", lambda s: "international" in s[3])
    write_group("atis", lambda s: "atis" in s[3])
    write_group("center", lambda s: "center" in s[3])
    (playlists / "atc.m3u").write_text(
        "#EXTM3U\n" + "".join(m3u_entry(*s[:3]) for s in STATIONS)
    )
    (ROOT / "radios.toml").write_text("".join(radios_station(*s[:3]) for s in STATIONS))
    print(f"{len(STATIONS)} stations")


if __name__ == "__main__":
    main()
