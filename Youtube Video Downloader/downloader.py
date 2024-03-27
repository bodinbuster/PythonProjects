import sys
try:
    from pytube import YouTube
except ImportError:
    print('This program requires the PyTube module, which you')
    print('can install by following the instructions at')
    print('https://pytube.io/en/latest/user/install.html')
    input('Press ENTER to exit.')
    sys.exit()

try:
    # Ask user for url
    url = input("Enter the url of the YouTube video you want to download: ")

    # Create YouTube object
    yt = YouTube(url)

    print("Title: ", yt.title)
    print("Number of views: ", yt.views)

    # Get user confirmation
    confirm = input("Do you want to download this video? (Y/n): ")

    if confirm.lower() == "n":
        print("Video download aborted.")
        input("Press ENTER to exit.")
        exit()
    else:
        # Get the highest resolution available
        print("Getting highest resolution...")
        ys = yt.streams.get_highest_resolution()

        # Download the video
        print("Downloading...")
        ys.download()

        print("Download complete!")
        input("Press ENTER to exit.")
except Exception as e:
    print("An error occurred: ", str(e))
