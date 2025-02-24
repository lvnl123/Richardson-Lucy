<h1 id="基于-richardson-lucy-算法的图像去模糊">基于 Richardson-Lucy 算法的图像去模糊</h1>
<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green" alt="License"></a>
</p>
<p>
  本项目通过模拟图像模糊并使用 <strong>Richardson-Lucy 去卷积算法</strong> 恢复模糊图像，展示了图像退化与恢复的完整流程。它是一个简单易懂但功能强大的工具，适合用于学习和研究图像处理技术。
</p>

<h2 id="目录">目录</h2>
<ul>
  <li><a href="#功能概述">功能概述</a></li>
  <li><a href="#核心特点">核心特点</a></li>
  <li><a href="#代码结构">代码结构</a></li>
  <li><a href="#依赖库">依赖库</a></li>
  <li><a href="#运行方法">运行方法</a></li>
  <li><a href="#参数说明">参数说明</a></li>
  <li><a href="#示例输出">示例输出</a></li>
  <li><a href="#应用场景">应用场景</a></li>
  <li><a href="#未来改进方向">未来改进方向</a></li>
  <li><a href="#许可证">许可证</a></li>
</ul>

<h2 id="功能概述">功能概述</h2>
<p>
  本项目的主要功能包括以下几个步骤：
</p>
<ol>
  <li><strong>加载原始图像：</strong>
    <ul>
      <li>使用 OpenCV 加载一张灰度图像作为输入。</li>
      <li>图像被读取为灰度模式（<code>cv2.IMREAD_GRAYSCALE</code>），以便后续处理。</li>
    </ul>
  </li>
  <li><strong>模拟图像模糊：</strong>
    <ul>
      <li>构造一个高斯点扩散函数（PSF，Point Spread Function），用于模拟图像模糊效果。</li>
      <li>使用 <code>scipy.ndimage.gaussian_filter</code> 生成平滑的高斯 PSF。</li>
      <li>将 PSF 归一化后，通过卷积操作（<code>scipy.signal.convolve2d</code>）对原始图像进行模糊处理。</li>
      <li>在模糊图像上叠加随机高斯噪声，模拟真实场景中的噪声干扰。</li>
    </ul>
  </li>
  <li><strong>应用 Richardson-Lucy 去卷积算法：</strong>
    <ul>
      <li>使用 <code>skimage.restoration.richardson_lucy</code> 函数对模糊图像进行去卷积。</li>
      <li>可以调整迭代次数（<code>num_iter</code> 参数）以优化恢复效果。</li>
    </ul>
  </li>
  <li><strong>结果可视化：</strong>
    <ul>
      <li>使用 <code>matplotlib</code> 绘制四个子图：</li>
      <ul>
        <li>原始图像。</li>
        <li>高斯模糊核（PSF）的等高线图。</li>
        <li>模拟生成的模糊图像。</li>
        <li>去卷积恢复后的清晰图像。</li>
      </ul>
    </ul>
  </li>
</ol>

<h2 id="核心特点">核心特点</h2>
<ul>
  <li><strong>高度可定制性：</strong>
    <ul>
      <li>支持调整 PSF 的大小和形状，灵活适配不同的模糊场景。</li>
      <li>噪声强度可以根据实际需求调整，模拟不同程度的退化。</li>
      <li>去卷积迭代次数可以自由设置，平衡恢复效果和计算效率。</li>
    </ul>
  </li>
  <li><strong>高效实现：</strong>
    <ul>
      <li>基于 <code>scikit-image</code> 和 <code>scipy</code> 提供的优化算法，快速完成图像模糊与恢复。</li>
      <li>使用 <code>numpy</code> 和 <code>scipy</code> 进行高效的数值计算，确保性能。</li>
    </ul>
  </li>
  <li><strong>直观展示：</strong>
    <ul>
      <li>使用 <code>matplotlib</code> 提供清晰的可视化结果，便于理解每一步的处理过程。</li>
      <li>包括 PSF 的等高线图，帮助用户更好地理解模糊核的作用。</li>
    </ul>
  </li>
  <li><strong>易于扩展：</strong>
    <ul>
      <li>代码结构清晰，模块化设计，方便添加新功能或替换算法。</li>
      <li>支持进一步扩展到彩色图像处理或其他去卷积算法。</li>
    </ul>
  </li>
</ul>

<h2 id="代码结构">代码结构</h2>
<p>
  项目的代码分为以下几个主要部分：
</p>
<ol>
  <li><strong>加载图像：</strong>
    <ul>
      <li>使用 OpenCV 的 <code>cv2.imread</code> 函数加载灰度图像。</li>
      <li>示例代码中需要将 <code>'填图片'</code> 替换为实际的图像路径。</li>
    </ul>
  </li>
  <li><strong>生成模糊图像：</strong>
    <ul>
      <li>定义函数 <code>create_blurred_image</code>，用于生成模糊图像。</li>
      <li>构造高斯 PSF 并归一化。</li>
      <li>使用 <code>convolve2d</code> 对图像进行卷积操作，生成模糊效果。</li>
      <li>添加随机高斯噪声，模拟真实场景中的退化。</li>
    </ul>
  </li>
  <li><strong>去卷积恢复：</strong>
    <ul>
      <li>使用 <code>skimage.restoration.richardson_lucy</code> 函数对模糊图像进行去卷积。</li>
      <li>可以调整迭代次数（<code>num_iter</code> 参数）以优化恢复效果。</li>
    </ul>
  </li>
  <li><strong>结果展示：</strong>
    <ul>
      <li>使用 <code>matplotlib</code> 绘制四个子图：</li>
      <ul>
        <li>原始图像。</li>
        <li>高斯模糊核（PSF）的等高线图。</li>
        <li>模拟生成的模糊图像。</li>
        <li>去卷积恢复后的清晰图像。</li>
      </ul>
    </ul>
  </li>
</ol>

<h2 id="依赖库">依赖库</h2>
<p>
  本项目依赖以下 Python 库：
</p>
<ul>
  <li><code>opencv-python</code>: 用于加载和处理图像。</li>
  <li><code>numpy</code>: 用于数值计算。</li>
  <li><code>matplotlib</code>: 用于数据可视化。</li>
  <li><code>scipy</code>: 用于卷积操作和高斯滤波。</li>
  <li><code>skimage</code>: 提供 Richardson-Lucy 去卷积算法。</li>
</ul>
<p>
  安装依赖：
</p>
<pre><code class="bash">
pip install opencv-python numpy matplotlib scipy scikit-image
</code></pre>

<h2 id="运行方法">运行方法</h2>
<ol>
  <li><strong>准备输入图像：</strong>
    <ul>
      <li>将代码中的 <code>'填图片'</code> 替换为你的图像路径。例如：<code>'input_image.jpg'</code>。</li>
    </ul>
  </li>
  <li><strong>运行脚本：</strong>
    <ul>
      <li>在终端中运行以下命令：
        <pre><code class="bash">
python your_script_name.py
        </code></pre>
      </li>
    </ul>
  </li>
  <li><strong>调整参数：</strong>
    <ul>
      <li>修改 PSF 大小（<code>psf_size</code> 参数）以控制模糊程度。</li>
      <li>调整噪声强度（<code>0.1 * blurred_image.std()</code>）以模拟不同程度的退化。</li>
      <li>修改去卷积迭代次数（<code>num_iter</code> 参数）以优化恢复效果。</li>
    </ul>
  </li>
</ol>

<h2 id="参数说明">参数说明</h2>
<table border="1" cellpadding="5">
  <thead>
    <tr>
      <th>参数名</th>
      <th>描述</th>
      <th>默认值</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>psf_size</code></td>
      <td>高斯模糊核的大小，决定了模糊的程度。</td>
      <td>15</td>
    </tr>
    <tr>
      <td><code>sigma</code></td>
      <td>高斯模糊核的标准差，控制 PSF 的平滑程度。</td>
      <td><code>psf_size / 6</code></td>
    </tr>
    <tr>
      <td><code>noise_level</code></td>
      <td>噪声强度，模拟真实场景中的退化。</td>
      <td><code>0.1 * blurred_image.std()</code></td>
    </tr>
    <tr>
      <td><code>num_iter</code></td>
      <td>Richardson-Lucy 去卷积算法的迭代次数。</td>
      <td>30</td>
    </tr>
  </tbody>
</table>

<h2 id="示例输出">示例输出</h2>
<p>
  运行脚本后，会生成一个包含四个子图的网格，展示以下内容：
</p>
<ol>
  <li><strong>原始图像：</strong> 输入的未处理清晰图像。</li>
  <li><strong>PSF 分布：</strong> 高斯模糊核的等高线图，展示了模糊核的强度分布。</li>
  <li><strong>模糊图像：</strong> 模拟生成的退化图像，经过卷积和噪声添加处理。</li>
  <li><strong>恢复图像：</strong> 经过 Richardson-Lucy 算法处理后的清晰图像。</li>
</ol>
<h2 id="应用场景">应用场景</h2>
<p>
  本项目适用于以下领域：
</p>
<ul>
  <li><strong>图像处理研究：</strong> 分析模糊和噪声对图像的影响，研究图像退化的机制。</li>
  <li><strong>天文学：</strong> 恢复因大气湍流或光学系统缺陷导致的模糊图像。</li>
  <li><strong>医学影像：</strong> 增强显微镜或 MRI 扫描中的低质量图像，提高诊断准确性。</li>
  <li><strong>摄影：</strong> 修复运动模糊或失焦问题，提升照片质量。</li>
</ul>

<h2 id="未来改进方向">未来改进方向</h2>
<ul>
  <li>支持彩色图像处理：当前仅支持灰度图像，未来可以扩展到 RGB 彩色图像。</li>
  <li>实现更多去卷积算法：例如维纳滤波（Wiener Filter）或其他高级去卷积方法。</li>
  <li>提供交互式界面：开发 GUI 或 Web 界面，方便用户调整参数并实时查看结果。</li>
  <li>优化性能：针对大尺寸图像优化算法性能，减少计算时间。</li>
</ul>

<h2 id="许可证">许可证</h2>
<p>
  本项目采用 <a href="LICENSE">MIT 许可证</a>。您可以自由使用、修改和分发本项目代码。
</p>
