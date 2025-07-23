# Añadir subtitulos a los videos

comando 
''' bash
ffmpeg -i video.mp4 -vf "subtitles=subtitulos.srt:force_style='FontName=Arial,FontSize=24,PrimaryColour=&H0000FFFF'" -c:a copy video_con_subtitulos.mp4
'''

