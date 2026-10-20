# download_data.py —— 下载 ChnSentiCorp 并保存到本地
import urllib.request
import os

# 要下载的网址（hf-mirror 上的 ChnSentiCorp）
url = "https://hf-mirror.com/datasets/dirtycomputer/ChnSentiCorp_htl_all/resolve/main/ChnSentiCorp_htl_all.csv"

# 伪装成浏览器，防止被服务器拒绝
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

# 真正发起请求，拿到响应
resp = urllib.request.urlopen(req)

# 把响应内容（字节）读出来
data = resp.read()
print("拿到了字节数:", len(data))

# 定义保存路径（按数据契约）
save_dir = "data/raw/chnsenticorp"
save_path = os.path.join(save_dir, "ChnSentiCorp_htl_all.csv")

# 创建文件夹（已存在也不会报错）
os.makedirs(save_dir, exist_ok=True)

# 把数据写入文件
with open(save_path, "wb") as f:
    f.write(data)

# 校验：文件真的写好了吗？
size = os.path.getsize(save_path)
print("文件大小:", size)
print("是否等于 2904858:", size == 2904858)
