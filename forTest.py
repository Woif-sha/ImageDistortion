from PIL import Image, ImageDraw


def fill_circle_with_image(image_path, circle_size=(84 * 2, 84 * 2), save=False):
    """
    将给定图片裁剪出指定大小的圆形区域，并可选择保存结果。
    参数:
    image_path (str): 原始图片的文件路径
    circle_size (tuple): 圆形的尺寸（宽，高），默认是(84, 84)
    """
    # 打开原始图片
    img = Image.open(image_path).convert("RGBA")
    width, height = circle_size
    orig_width, orig_height = img.size

    # 计算以图片中心为基准的裁剪区域坐标（确保圆形在图片中间）
    left = (orig_width - width) // 2
    upper = (orig_height - height) // 2
    right = left + width
    lower = upper + height

    # 创建一个透明的新图像，大小与目标圆形一致
    circle_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(circle_img)
    # 在新图像上绘制圆形，这里填充白色作为示例，可以根据需要调整
    draw.ellipse((0, 0, width, height), fill=(255, 255, 255, 255))

    # 从原始图片中裁剪出对应区域（以中心为准的矩形区域，后续再用圆形裁剪）
    img = img.crop((left, upper, right, lower))

    # 使用圆形遮罩来裁剪图片，通过alpha通道合成
    img.putalpha(circle_img.split()[-1])
    circle_img.paste(img, (0, 0), img)

    circle_img.show()
    print(circle_img.size)
    if save:
        rgb_im = circle_img.convert('RGB')
        rgb_im.save(image_path + '_circle.jpg')


if __name__ == '__main__':
    image_path = "result_concat_res.jpg"  # 替换为你的实际图片路径
    fill_circle_with_image(image_path, save=True)
