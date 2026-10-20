# eda.py —— D2 探索性分析：读数据 + 打印统计量 + 生成 2 张图
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # 不弹窗口，直接存图（适合脚本运行）
import matplotlib.pyplot as plt

# 1) 中文字体：matplotlib 默认字体不含中文，不设会显示成方框
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False  # 让负号正常显示

# 2) 读数据（路径按数据契约；data/ 已被 .gitignore 排除，不会入库）
df = pd.read_csv("data/raw/chnsenticorp/ChnSentiCorp_htl_all.csv", encoding="utf-8")

# 3) 打印关键统计量 —— "不看图也能核对" 的依据
print("形状:", df.shape)
print("标签分布:\n", df["label"].value_counts())
print("正向占比:", df["label"].mean().round(4))

df["length"] = df["review"].fillna("").astype(str).str.len()  # 缺失评论按空串算
print("缺失评论数:", int(df["review"].isna().sum()))
print("评论长度统计:\n", df["length"].describe())

# 4) 图 1：标签分布柱状图
fig1, ax1 = plt.subplots(figsize=(6, 4))
counts = df["label"].value_counts().sort_index()
ax1.bar(counts.index.astype(str), counts.values, color=["#d9534f", "#5cb85c"])
ax1.set_title("评论情感标签分布")
ax1.set_xlabel("标签（0=负向，1=正向）")
ax1.set_ylabel("评论条数")
for i, v in enumerate(counts.values):
    ax1.text(i, v + 50, str(v), ha="center")
fig1.tight_layout()
fig1.savefig("figures/label_distribution.png", dpi=150)
print("已保存 figures/label_distribution.png")

# 5) 图 2：评论长度分布直方图
fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.hist(df["length"], bins=50, color="#5bc0de", edgecolor="white")
ax2.set_title("评论长度分布")
ax2.set_xlabel("长度（字符数）")
ax2.set_ylabel("评论条数")
ax2.axvline(
    df["length"].median(),
    color="red",
    linestyle="--",
    label=f"中位数 {df['length'].median():.0f}",
)
ax2.legend()
fig2.tight_layout()
fig2.savefig("figures/review_length.png", dpi=150)
print("已保存 figures/review_length.png")
