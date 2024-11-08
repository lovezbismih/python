import os
import sys
import subprocess

# SCP 目标路径
SCP_TARGET = "root@yourip:/www/wwwroot/blog/source/_posts/blog"

def upload_file(file_path):
    # SCP 命令
    scp_command = ["scp", file_path, SCP_TARGET]
    try:
        # 执行 SCP 命令
        subprocess.run(scp_command, check=True)
        print(f"文件 {file_path} 上传成功！")
    except subprocess.CalledProcessError as e:
        print(f"文件上传失败: {e}")

if __name__ == "__main__":
    # 拖拽文件时，会将文件路径作为参数传入
    if len(sys.argv) > 1:
        for file_path in sys.argv[1:]:
            if os.path.isfile(file_path):
                upload_file(file_path)
            else:
                print(f"{file_path} 不是有效的文件路径")
    else:
        print("请拖拽文件到此程序上")
