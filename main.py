import mutagen
from mutagen.mp4 import MP4
import click
import os
import re

@click.command()
@click.option('--dir', default='.', prompt="Source directory: ", help='Location for mp4 files to apply tags too')
@click.option('--genre', default='unknown', prompt='Genre: ', help='The movie genre of the movie files')
@click.option('--album', default='unknown', prompt='Album: ', help='The album/series the movies are from')
@click.option('--disk_total', default='1', prompt='Total Disks: ', help='Total number of disks in season/series')
@click.option('--disk_number', default='1', prompt='Disk Number: ', help='Current number for disks in season/series')
@click.option('--season', default='1', prompt='Season: ', help='Season number in series')
def main(dir, genre, album, disk_total, disk_number, season):
    files = sorted([f for f in os.listdir(dir) if re.match(r'.*\.mp4', f)])
    count = len(files)
    i=0
    for file in files:        
        print(f"Working {file} in {dir}")
        name = file[0:-4]
        i=i+1
        f = MP4(f"{dir}/{file}")
        f.delete()
        f.save()
        f['\xa9gen']=[genre]
        f['\xa9alb']=[album]
        f['\xa9nam']=[name]
        f['trkn']=[(i,count)]
        f['disk']=[(int(disk_number),int(disk_total))]
        f['tvsn']=[int(season)]
        f.save()        
        print(f)
        print("done")

if __name__ == "__main__":
    main()