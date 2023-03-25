from moviepy.editor import *
from pydub import AudioSegment

# *.mp4 -> *.wav
# 소리만 추출하는 과정
def extractAudio(video_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    #mp4 포맷 비디오 대상 -> *.wav
    audio_file = video_file.replace(".mp4", ".wav") 
    audio.write_audiofile(audio_file)

    return audio_file

# *.wav -> *.mp3
# 추출한 소리로 *.mp3로 변환
def convertToMp3(audio_file):
    audio = AudioSegment.from_wav(audio_file)
    audio_file_mp3 = audio_file.replace("*.wav", "*.mp3")   
    audio.write_audiofile(audio_file_mp3)
    
    return audio_file_mp3