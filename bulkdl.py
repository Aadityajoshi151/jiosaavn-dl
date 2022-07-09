import subprocess

songs = []

while(True):
    song = input("Enter link for the song enter 1 if you are done:\n")
    if song == "1":
        break
    else:
        songs.append(song)

for song in songs:
    subprocess.call(f"python3 jiosaavn.py {song}", shell=True)
print("Downloads complete!")
