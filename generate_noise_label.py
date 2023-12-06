import random

# w+表示打开一个文件用于读写，如果该文件已经存在则将其覆盖，如果该文件不存在，则创建新文件
new_file = open("./result/0.1noise_train.txt", "w+")  # 加10%的噪声
# new_file = open("./result/0.2noise_train.txt", "w+")  # 加20%的噪声
# new_file = open("./result/0.3noise_train.txt", "w+")  # 加30%的噪声
with open("./result/train_label.txt", "r") as file:
    for line in file:
        line = line.strip()
        img_path = line.split(' ')[0]
        label = line.split(' ')[1]
        # random.uniform()用于从在[0,1]的均匀分布中随机采样
        number = random.uniform(0, 1)
        if number <= 0.1:  # 加10%的噪声
            # if number <= 0.2:  # 加20%的噪声
            # if number <= 0.3:  # 加30%的噪声
            while (1):
                # random.randint()用于从[0,6]中随机选择一个整数
                new_label = random.randint(0, 6)
                if new_label != int(label):
                    new_file.write(img_path + ' ' + str(new_label) + '\n')
                    break
        else:
            new_file.write(img_path + ' ' + str(label) + '\n')
