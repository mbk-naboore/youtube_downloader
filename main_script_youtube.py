from pytube import YouTube
import os
import ffmpeg

# some needed paths:-
user_path = str(os.environ["HOMEPATH"].replace("\\", "/"))
main_path = f"C:{user_path}"+"/Desktop/all_youtube_downloaded_video"

# this is for the 360p and 720p
def normal_download(user_res):
    """downloading the 360p and 720p """
    if res == 1:
        stream = yt.streams.get_by_itag(18)  # this is for the 360p
        stream.download(main_path)
    elif res == 2:
        stream = yt.streams.get_by_itag(22)  # this is for the 720p
        stream.download(main_path)

# this is for the 4k
def other_res(users_res):
    if users_res == 3:
        try:
            _4kvideo = yt.streams.get_by_itag(137)  # this is the video
            _4kvideo.download(output_path=main_path, filename='video_only.mp4',)
            _4kaudio = yt.streams.get_by_itag(251)  # this is the audio
            _4kaudio.download(output_path=main_path, filename='audio_only.mp4')
            pass
        except:
            global res
            res = 1
            normal_download(1)
        pass
    elif users_res == 4:
        try:
            _4kvideo = yt.streams.get_by_itag(271)  # this is the video
            _4kvideo.download(output_path=main_path, filename='video_only.mp4')
            _4kaudio = yt.streams.get_by_itag(251)  # this is the audio
            _4kaudio.download(output_path=main_path, filename='audio_only.mp4')
            pass
        except:
            other_res(users_res=users_res - 1)
    elif users_res == 5:
        try:
            _4kvideo = yt.streams.get_by_itag(313)  # this is the video
            _4kvideo.download(output_path=main_path, filename='video_only.mp4')
            _4kaudio = yt.streams.get_by_itag(251)  # this is the audio
            _4kaudio.download(output_path=main_path, filename='audio_only.mp4')
            pass
        except:
            other_res(users_res=users_res - 1)
        pass
    pass

#renaming all
def merging_and_cleaning():
    """while i download the file i rename it so when merging it it can be easier to know
    the file by the prefix and by the tittle of it....and now i am renaming them for the
    merge action"""

    # this is the merged
    try:
        # the merging time:
        video = ffmpeg.input(main_path+"/video_only.mp4")
        audio = ffmpeg.input(main_path+"/audio_only.mp4")
        if my_title.strip().lower() == 'd':
            ffmpeg.output(video, audio, main_path+"/{yt.title.replace('|','_')}.mp4", vcodec='copy', acodec='aac',strict='experimental').run()
        else:
            ffmpeg.output(video, audio, main_path+"/{my_title}.mp4", vcodec='copy', acodec='aac', strict='experimental').run()
    except:
        print("the files were not merged...")

    # now the clean up time
    os.remove(main_path+"/video_only.mp4")
    os.remove(main_path+"/audio_only.mp4")
    pass

#this will download the audion only
def the_audio_only_mp3():
    if my_title.strip().lower() == 'd':
        _4kaudio = yt.streams.get_by_itag(251)  # this is the audio
        _4kaudio.download(output_path=main_path, filename=f'{yt.title.replace("|","_")}.mp4')
    else:
        _4kaudio = yt.streams.get_by_itag(251)  # this is the audio
        _4kaudio.download(output_path=main_path, filename=f'{my_title}.mp4')
    pass

#to make sure that the directory is there else creat it.
def directory_checker():
    if not os.path.isdir(main_path):
        os.mkdir(main_path)
    pass

#all the inputs the user need to do at one place
def user_iputs():
    # making the user inputs:-
    url = str(input("Please provide the URL(link) of the video:\t "))
    res = int(input("""please choose the needed resolution for your video:
            1)360p
            2)720p
            3)1080(HD)
            4)1440(FHD) 
            5)2160p(4k)
            6)ONLY-THE-AUDIO(mp3)
            --------------------------------------------------------------
                please choose one of the choices above?!--> """))

    # this is the Youtube object:-
    yt = YouTube(url=url)
    my_title = str(input('What is the title you would like? To choose the default title [d] or [D] : '))
    return url, res, yt, my_title

flag = "y"
# deciding the res:
while flag == "y":
    url, res, yt, my_title = user_iputs()
    if res == 1 or res == 2:
        normal_download(res)
        break
    elif 3 <= res < 6:
        other_res(res)
        if res==1:
            break
        merging_and_cleaning()
        print()
        print()
        break
    elif res == 6:
        the_audio_only_mp3()
        break
    flag = str(input("Would you like to download another video [y]/[n]: ")).lower()
print("\n\nThank you for using my script...mbk-naboore")

