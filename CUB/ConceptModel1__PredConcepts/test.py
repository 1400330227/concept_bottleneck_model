import pickle

if __name__ == '__main__':
    with open('./train.pkl', 'rb') as f:
        train = pickle.load(f)
        # id
        # img_path=''CUB_200_2011/images/022.Chuck_will_Widow/Chuck_Will_Widow_0059_796982.jpg''
        # class_label=21
        # attribute_label=[-5.967625, -4.7681236, -3.614014, ...]
        # attribute_certainty=[4, 4, 4, ...]
        print(train)