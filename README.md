# movie-meta-editor
Python project that allows the bulk editing of metadata information for MP4/M4V files in a directory.  Currently supports setting Genre, Title, Album, Track Number, Season, Disk Number.

The title is set by taking the file extention off of the title name and the track number is set by sorting the files in the folder and then incrementing by 1 for every file against the total.

## Packages Used
Leverages:
* os
* mutagen

## Usage
* `python -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `python main.py --dir="/source/directory/of/files" --genre=Anime --album="My Series Title"`