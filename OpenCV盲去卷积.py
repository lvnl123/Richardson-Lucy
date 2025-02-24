import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import restoration
from scipy.signal import convolve2d
from scipy.ndimage import gaussian_filter

# 加载原始图像
original_image = cv2.imread('填图片', cv2.IMREAD_GRAYSCALE)


# 模拟模糊：通过卷积操作生成模糊图像
def create_blurred_image(image, psf_size=15):
    # 创建一个高斯模糊核作为PSF
    psf = np.zeros((psf_size, psf_size))
    psf[psf_size // 2, psf_size // 2] = 1  # 中心点为1
    psf = gaussian_filter(psf, sigma=psf_size / 6)  # 使用高斯滤波生成平滑的PSF
    psf /= psf.sum()  # 归一化

    # 对图像进行卷积操作以模拟模糊
    blurred_image = convolve2d(image, psf, mode='same', boundary='symm')

    # 添加一些噪声
    blurred_image += 0.1 * blurred_image.std() * np.random.standard_normal(blurred_image.shape)

    return blurred_image, psf


# 创建模糊图像
blurred_image, psf = create_blurred_image(original_image)

# 使用Richardson-Lucy去卷积算法进行盲去卷积
deconvolved_image = restoration.richardson_lucy(blurred_image, psf, num_iter=30)

# 显示结果
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

# 原始图像
axes[0, 0].imshow(original_image, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

# 可视化卷积核（PSF）为等高线图
x = np.arange(psf.shape[1])
y = np.arange(psf.shape[0])
X, Y = np.meshgrid(x, y)
contour = axes[0, 1].contour(X, Y, psf, levels=10, cmap='viridis')
axes[0, 1].clabel(contour, inline=True, fontsize=8)
axes[0, 1].set_title('Convolution Kernel (PSF)')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y')

# 模糊图像
axes[1, 0].imshow(blurred_image, cmap='gray')
axes[1, 0].set_title('Blurred Image')
axes[1, 0].axis('off')

# 去卷积后的图像
axes[1, 1].imshow(deconvolved_image, cmap='gray')
axes[1, 1].set_title('Deconvolved Image')
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()