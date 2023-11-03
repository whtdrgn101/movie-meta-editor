import mutagen
from mutagen.mp4 import MP4
import click
import os

@click.command()
@click.option('--dir', default='.', prompt="Source directory: ", help='Location for mp4 files to apply tags too')
@click.option('--genre', default='unknown', prompt='Genre: ', help='The movie genre of the movie files')
@click.option('--album', default='unknown', prompt='Album: ', help='The movie genre of the movie files')
def main(dir, genre, album):
    files = sorted(os.listdir(dir))
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
        f.save()        
        print(f)
        print("done")

if __name__ == "__main__":
    main()