train_file = open('./result/train_label.txt')
val_file = open('./result/val_label.txt')

train_label_info = []
for line in train_file:
    train_label_info.append(line.strip().split(' '))

train_each_category_img_num = [0, 0, 0, 0, 0, 0, 0]
for sample in train_label_info:
    train_each_category_img_num[int(sample[1])] += 1
print(train_each_category_img_num)
# [132756, 13834, 5470, 8080, 75328, 68256, 26065] 共329789张训练图像
# 0:中性  1:生气  2:厌恶  3:恐惧 4:高兴 5:悲伤 6:惊讶

val_label_info = []
for line in val_file:
    val_label_info.append(line.strip().split(' '))
val_each_category_img_num = [0, 0, 0, 0, 0, 0, 0]
for sample in val_label_info:
    val_each_category_img_num[int(sample[1])] += 1
print(val_each_category_img_num)
# [69498, 5874, 625, 7787, 24417, 20070, 7197] 共135468张验证图像
# 0:中性  1:生气  2:厌恶  3:恐惧 4:高兴 5:悲伤 6:惊讶
