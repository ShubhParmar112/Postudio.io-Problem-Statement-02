# Automated Promo Creator
A simple Python tool that automatically creates a short promo video from a longer input video by selecting the most dynamic scenes.

## ⚙️ How It Works:<br>
-Splits the video into segments.<br>
-Detects motion using frame variance.<br>
-Picks the most active clips.<br>
-Merges them into a 1-minute promo.<br>
(Here the time duration of the final promo can be altered according to the requirements).<br> 

## 🧩 Usage:<br>
Place your video in the data/ folder as input_video.mp4<br>
Run: `python main.py`

Output is saved in output/promo_output.mp4
