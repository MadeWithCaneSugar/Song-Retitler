import os, eyed3

def addTrackNumberToFilename (path=None):
    """
    Similar to the above function, but instead of adding the track number to the title, it adds it to the filename
    """
    if path == None:
        path = input("Enter the path to the directory: ")
    files = os.listdir(path)
    for file in files:
        if file.endswith(".mp3"):
            audiofile = eyed3.load(path + "\\" + file)
            if audiofile.tag.track_num is not None:
                track = str(audiofile.tag.track_num[0])
                newFileName = track + " - " + file
                newFileName = newFileName.replace("None - ", "")
                try:
                    os.rename(path + "\\" + file, path + "\\" + newFileName)
                    print("Track number added to filename for " + file)
                except FileExistsError:
                    print("File already exists: " + newFileName)
                    os.rename(path + "\\" + file, path + "\\" + newFileName + " 1")
                except:
                    print("Error renaming file: " + file)
            else:
                print("No track number for " + file)
        elif os.path.isdir(path + "\\" + file):
            addTrackNumberToFilename(path + "\\" + file)
        else:
            print(file + " is not an mp3 file")

def removeArtistNameFromFilename (path=None):
    """
    This function removes the artist name from the filename. This is useful if you have a bunch of songs that are named like this: 
    'Artist - Song.mp3' (turned into 'Song.mp3' by this function)
    Basically I take whatever is in the `contributing artists` part of the metadata and remove that from the filename if it's found there. Also searches for '- ' following
    the artist name and removes that to since it's just a seperator.
    """
    if path == None:
        path = input("Enter the path to the directory: ")
    files = os.listdir(path)
    for file in files:
        if file.endswith(".mp3"):
            audiofile = eyed3.load(path + "\\" + file)
            if audiofile.tag.artist is not None:
                artist = audiofile.tag.artist
                #replace semicolons with commas. This is because files with multiple artists are seperated by semicolons in the metadata, but commas in the filename
                if ";" in artist:
                    artist = artist.replace(";", ",")
                newFileName = file.replace(artist, "")
                newFileName = newFileName.replace(" - ", "")
                try:
                    os.rename(path + "\\" + file, path + "\\" + newFileName)
                    print("Artist name removed from filename for " + file)
                except FileExistsError:
                    print("File already exists: " + newFileName)
                    os.rename(path + "\\" + file, path + "\\" + newFileName + " 1")
                except:
                    print("Error renaming file: " + file)
            else:
                print("No artist name for " + file)
        elif os.path.isdir(path + "\\" + file):
            removeArtistNameFromFilename(path + "\\" + file)
        else:
            print(file + " is not an mp3 file")

def runner():
    """
    This is the runner function that prompts the user for a directory path, and then runs the relevant functions
    """
    path = input("Enter the path to the directory: ")
    print("Would you like to:")
    print("(1) Add track number to filename")
    print("(2) Remove artist name from filename")
    print("(3) Add track number to filename and remove artist name from filename")
    
    choice = input("Enter your choice(1/2/3): ")

    if choice == "1":
        print("Adding track number to filename...")
        addTrackNumberToFilename(path)

    elif choice == "2":
        print("Removing artist name from filename...")
        removeArtistNameFromFilename(path)

    elif choice == "3":
        print("Removing artist name from filename...")
        removeArtistNameFromFilename(path)
        print("Adding track number to filename...")
        addTrackNumberToFilename(path)

    else:
        print("Invalid choice. Please try again.")
        runner()

    print("Done! Thank you for your patience :)")

if __name__ == "__main__":
    runner()