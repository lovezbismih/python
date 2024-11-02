cd ~/music_tmp/music
 read -p "输入链接:" url
BBDown  --audio-only  -p 1 $url



https://www.bilibili.com/video/BV1iG4y1x7Ur/?spm_id_from=333.337.search-card.all.click





url="https://www.bilibili.com/list/3461563583302074?sid=3809579&desc=1&oid=1603178578"
cd ~/music_tmp/music
BBDown  --audio-only $url



https://api.bilibili.com/x/polymer/space/seasons_archives_list?mid=3461563583302074&season_id=3809573&sort_reverse=false&page_num=1&page_size=30



https://space.bilibili.com/3461563583302074/channel/seriesdetail?sid=3809573


https://api.bilibili.com/x/series/archives?mid=3461563583302074&series_id=3809573&only_normal=true&sort=desc&pn=1&ps=30&current_mid=3494365181774371





cd ~/music_tmp/music
for line in `cat /root/music_tmp/music/1.txt`
do
BBDown  --audio-only  -p 1 https://www.bilibili.com/video/$line
done




https://api.bilibili.com/x/series/archives?mid=3461563583302074&series_id=3809577&only_normal=true&sort=desc&pn=1&ps=30&current_mid=3494365181774371