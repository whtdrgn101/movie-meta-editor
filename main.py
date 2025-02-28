from mutagen.mp4 import MP4
import click
import os
import re
import string

@click.command()
@click.option('--dir', default='.', prompt="Source directory: ", help='Location for mp4 files to apply tags too')
@click.option('--genre', default='unknown', prompt='Genre: ', help='The movie genre of the movie files')
@click.option('--show', default='unknown', prompt='Show: ', help='The album/series the movies are from')
@click.option('--season', default='1', prompt='Season: ', help='Season number in series')
def main(dir, genre, show, season):
    files = sorted([f for f in os.listdir(dir) if re.match(r'.*\.m', f)])
    count = len(files)
    track_num=0
    for file in files:        
        print(f"Working {file} in {dir}")
        extension = file[-3:]
        name = file[0:-4]
        track_num=track_num+1

        if extension == "m4v" or extension == "mp4":
            handle_m4v(dir, genre, show, season, count, track_num, file, name)
        if extension == "mkv":
            handle_mkv(dir, genre, show, season, count, track_num, file, name)
        else:
            print(f"Unsupported extention of {extension} for file {file}")

        print("done")

def handle_mkv(dir, genre, show, season, count, track_num, file, name):
    file_pointer = f"{dir}/{file}"
 
    os.system(f"mkvpropedit.exe \"{file_pointer}\" -s title=\"{name}\"")


def handle_m4v(dir, genre, show, season, count, track_num, file, name):
    f = MP4(f"{dir}/{file}")
    f.delete()
    f.save()
    f['\xa9gen']=[string.capwords(genre)]
    f['\xa9alb']=[string.capwords(show)]
    f['\xa9nam']=[name]
    f['trkn']=[(track_num,count)]
    f['tvsn']=[int(season)]
    f.save()        
    print(f)
    

if __name__ == "__main__":
    main()