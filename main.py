import cv2
import numpy as np
from moviepy import VideoFileClip, concatenate_videoclips
import os

INPUT_VIDEO="input/input_video.mp4"
OUTPUT_VIDEO="output/promo_output.mp4"
SEGMENT_DURATION=10
FINAL_PROMO_DURATION=60

os.makedirs("output",exist_ok=True)
os.makedirs("input",exist_ok=True)

clip=VideoFileClip(INPUT_VIDEO)
fps=clip.fps
total_duration=clip.duration

segments=[]
for start in np.arange(0,total_duration,SEGMENT_DURATION):
    end=min(start+SEGMENT_DURATION,total_duration)
    segment=clip.subclipped(start,end)
    frame=segment.get_frame(0)
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    motion_score=np.std(gray)
    segments.append((motion_score,segment))

# --- Pick the top motion segments ---
segments = sorted(segments, key=lambda x: x[0], reverse=True)
top_segments = [s[1] for s in segments[: int(FINAL_PROMO_DURATION / SEGMENT_DURATION)]]

# --- Merge the clips ---
final_clip = concatenate_videoclips(top_segments)
final_clip.write_videofile(OUTPUT_VIDEO, codec="libx264", audio_codec="aac")

print(f"✅ Promo video saved to {OUTPUT_VIDEO}")
