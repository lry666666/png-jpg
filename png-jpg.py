from PIL import Image
import os

def convert_png_to_jpg(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为PNG格式
        if filename.lower().endswith('.png'):
            try:
                # 构建完整的文件路径
                file_path = os.path.join(folder_path, filename)
                # 打开PNG图片
                img = Image.open(file_path)
                # 如果图片有透明通道，转换为RGB模式
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                # 构建新的JPG文件名
                new_filename = os.path.splitext(filename)[0] + '.jpg'
                new_file_path = os.path.join(folder_path, new_filename)
                # 保存为JPG格式
                img.save(new_file_path, 'JPEG', quality=90)
                # 删除原PNG文件
                os.remove(file_path)
                print(f'转换成功: {filename} -> {new_filename}')
            except Exception as e:
                print(f'转换失败: {filename}, 错误: {str(e)}')

# 使用示例
folder_path = 'C:/Users/lenovo/Desktop/空白图片'  # 替换为你的文件夹路径
convert_png_to_jpg(folder_path)
