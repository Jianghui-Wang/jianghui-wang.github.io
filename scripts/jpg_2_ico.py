from PIL import Image

# 打开 JPG 文件
img = Image.open("../assets/img/avatar.jpg")

# 调整尺寸为适合图标的大小
img = img.resize((64, 64), Image.ANTIALIAS)

# 保存为 ICO 格式
img.save("../assets/img/favicon.ico", format="ICO")