from pytube import YouTube

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