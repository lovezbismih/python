cd ~/music_tmp/music
for line in `cat /root/music_tmp/music/1.txt`
do
BBDown  --audio-only  -p 1 https://www.bilibili.com/video/$line
done
