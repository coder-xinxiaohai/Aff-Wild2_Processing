# Aff-Wild2_Processing

本项目完成了对Aff-Wild2数据集中，表情被标记为中性、生气、厌恶、恐惧、高兴、悲伤和惊讶，**7种表情之一**，**且效价和唤醒值均在[0,1]范围内**的图像筛选任务，并生成相关文件用于存放筛选出的图像路径及对应的标签信息。

具体地，**筛选出329789张训练图像**，其中包括132756张中性表情，13834张生气表情，5470张厌恶表情，8080张恐惧表情，75328张高兴表情，68256张悲伤表情，26065张惊讶表情；**筛选出135468张验证图像**，其中包括69498张中性表情，5874张生气表情，625张厌恶表情，7787张恐惧表情，24417张高兴表情，20070张悲伤表情，7197张惊讶表情。

注意，**该数据集包括了对图像进行面部裁剪、对齐，并缩放至112*112的处理**，因此本项目无需再进行面部对齐操作。

本项目的代码分别参考[这里](https://github.com/PanosAntoniadis/emotion-gcn)（图像筛选）和[这里](https://github.com/kaiwang960112/Self-Cure-Network)（训练标签加噪）**十分感谢前辈们的工作！** 另外，感谢我同门吴锐同学的帮助！

****
**1、数据准备工作**

由于Aff-Wild2数据集并未开源，需要自行申请，具体可点[这里](https://ibug.doc.ic.ac.uk/resources/aff-wild2/)，申请并下载成功后，须**将Aff-Wild2数据集中经面部裁剪、对齐并压缩至112*112大小的面部图像压缩包进行解压并放于Image文件夹下**，如下图所示：

![image](https://github.com/coder-xinxiaohai/Aff-Wild2_Processing/assets/73678229/0b1d01a9-6b86-4859-89f3-56a7e11832a5)

须**将Aff-Wild2数据集的标签信息压缩包进行解压并放于Label文件夹下**，如下图所示：
![image](https://github.com/coder-xinxiaohai/Aff-Wild2_Processing/assets/73678229/2c69c5f7-0569-49fe-aea7-63321caa01a2)

****
**2、数据处理部分**

(1) 首先运行pickle_annotations_affwild2.py文件，在result文件夹中生成data_affwild2.pkl文件。

(2) 接着运行save_annotatons_affwild2.py文件，在result文件夹中生成train_label.txt和val_label.txt文件。

至于dataloading.py和cal_each_category_img_nums.py文件分别用于数据加载和各表情类别的数量统计，如果大家只在意结果，暂时可不用管这两个文件，只需要记住须在Image和Label文件下中补充数据集的图像和标签信息，而项目的运行结果，即用于模型训练的训练集和验证集文件存于result文件，即可。

****
**3、为训练标签加噪**

该部分代码在generate_noise_label.py中，运行本文件，即可完成对训练标签的加噪(10%、20%、30%)，结果存于result文件夹中，分别为0.1noise_train.txt、0.2noise_train.txt和0.3noise_train.txt。

****
如果大家在运行本项目的过程中，遇到任何问题，欢迎留言~

