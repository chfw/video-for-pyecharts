cat *.log |sort -n > all.txt
gource all.txt --user-image-dir gavata --hide filenames,dirnames --seconds-per-day 1 --title pyecharts --bloom-multiplier 1.1 --bloom-intensity 1.2 -1920x1080 --file-idle-time 0 --logo logo.png --auto-skip-seconds 2  -o gource-aug-2018.ppm
ffmpeg -y -r 20 -f image2pipe -probesize 100M -vcodec ppm -i gource-aug-2018.ppm -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -threads 0 -bf 0 gource.mp4

