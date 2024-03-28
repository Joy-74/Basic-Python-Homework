import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def conv2D(image, kernel):
    """
    对输入图像进行2D卷积操作,并返回卷积后的图像。(加Padding版本)
    :param image: 输入图像,必须是一个二维NumPy数组。
    :param kernel: 卷积核,必须是一个二维NumPy数组。
    :return: 卷积后的图像,与输入图像大小相同的二维NumPy数组。
    """

    # 获取图像和卷积核的大小
    image_height, image_width, channel = image.shape
    kernel_height, kernel_width = kernel.shape

    # 计算需要填充的行数和列数
    pad_height = int((kernel_height - 1) // 2)
    pad_width = int((kernel_width - 1) // 2)

    # 在图像周围填充0
    padded_image = np.zeros((image_height + 2 * pad_height, image_width + 2 * pad_width, channel))
    padded_image[pad_height:image_height + pad_height, pad_width:image_width + pad_width] = image
    print(image.shape)

    # 初始化卷积后的图像
    output = np.zeros_like(image)

    # 对每个像素进行卷积
    for row in range(image_height):
        for col in range(image_width):
            # 获取当前像素及其周围像素的子图像
            sub_image = padded_image[row:row + kernel_height, col:col + kernel_width]

            # 对子图像和卷积核进行逐元素乘法
            sub_output = sub_image * np.expand_dims(kernel, axis=2)

            # 对逐元素乘积求和，得到卷积结果
            output[row, col] = sub_output.sum()

    return output


# 测试代码
if __name__ == '__main__':
    #读取RGB图像
    img = plt.imread('cat.png')

    #定义卷积核
    kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    # kernel = np.ones((5,5)) / 9

    #对RGB图像进行卷积操作
    conv_img = conv2D(img, kernel)

    #显示卷积前后的图像
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axs[0].imshow(img)
    axs[0].set_title('Original Image')
    axs[1].imshow(conv_img)
    axs[1].set_title('Blurred Cat Image')
    plt.savefig('blurred_cat_padding.png', dpi=600, bbox_inches='tight' )
    
    plt.show()