import subprocess
import requests
import time

# 配置
mid="3461563583302074"
series_id="3809573"

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

script_path = "/root/music_tmp/music/dl.sh"

# 清空1.txt
with open('1.txt', 'w') as file:
    pass  # 不写入任何内容，文件将被清空


# 循环发送请求
for page in range(1, 10):  # 从1到9
    url = f'https://api.bilibili.com/x/series/archives?mid={mid}&series_id={series_id}&only_normal=true&sort=desc&pn={page}&ps=30&current_mid=3494365181774371'
    response = requests.get(url,headers=headers)
    time.sleep(3)
    # 检查请求是否成功
    if response.status_code == 200:
        # 将返回的数据解析为Python对象
        data = response.json()

        # 提取所有的bvid
        bvids = [archive['bvid'] for archive in data['data']['archives']]

        # 打印bvids
        print(bvids)
        with open('1.txt', 'a') as file:
            for bvid in bvids:
                file.write(bvid + '\n')
    else:
        print(f"请求失败，状态码：{response.status_code}")



try:
    # 运行脚本
    result = subprocess.run(["bash", script_path], check=True, text=True, capture_output=True)
    # 打印输出
    print("标准输出:", result.stdout)
    print("标准错误:", result.stderr)
except subprocess.CalledProcessError as e:
    print(f"脚本运行失败，错误代码: {e.returncode}")
    print("标准输出:", e.stdout)
    print("标准错误:", e.stderr)