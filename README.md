# YANDEX MUSIC PRESENCE

A small script, which will display the current playing track in yandex music in your discord status.

## Installation

### Сlone this repository (git is required)

```shell
git clone https://github.com/Sekupas/YMPresence
```

### Dependencies info

For this program to work correctly, you need these dependencies

* [python3.8](https://www.python.org/downloads/) and higher
* [pypresence](https://github.com/qwertyquerty/pypresence)
* [yandex-music](https://github.com/MarshalX/yandex-music-api)

### Dependencies installation

If you have Poetry - you can use it to download dependencies:

```shell
cd yandex_music_presence
poetry install
```

or using pip:

```shell
pip install -r requirements.txt
```

### Venv

You can also create a Venv to install in a virtual space

```shell
python3 -m venv Venv
```

### Configuration file info

* `cp config.json.example config.json`
* you need to put your discord client id and yandex music api key to the config.json
  * yandex-music token from [here](https://yandex-music.readthedocs.io/en/latest/token.html)
  * discord client id from [here](https://discord.com/developers/docs/getting-started)

Run `main.py` and start to listen some track.
