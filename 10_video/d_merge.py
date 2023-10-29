from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def merge_videos(video_folder):
    video_files = [f for f in sorted(os.listdir(video_folder)) if f.endswith(".mp4")]
    if len(video_files) == 0:
        print("No video files found in the folder.")
        return

    clips = []
    for video_file in video_files:
        clips.append(VideoFileClip(os.path.join(video_folder, video_file)))

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("merged_video.mp4")

# 'res_mp4' 폴더 안의 비디오 파일을 병합합니다.
merge_videos('res_mp4')
