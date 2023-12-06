import pickle
from tqdm import tqdm

save_dir = './result'
data_pickle = pickle.load(open('./result/data_affwild2.pkl', 'rb'))
for data_type in ['train', 'val']:
    data = data_pickle[data_type]
    for sample in tqdm(data):
        with open(save_dir + '\\' + data_type + '_label' + '.txt', 'a') as f:
            f.write(sample.frame_path + ' ' + str(sample.expression) + ' ' + str(sample.valence) + ' ' + str(
                sample.arousal) + ' \n')
