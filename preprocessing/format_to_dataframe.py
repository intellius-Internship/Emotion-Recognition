import json
import pandas as pd

from os.path import join as pjoin

ROOT_DIR = '..'
DATA_DIR = pjoin(ROOT_DIR, 'data')

def construct_df(json_list):
    df_data = pd.DataFrame(columns=['situation', 'disease', 'age', 'sex', 'emotion-type', 'content'])

    for sess in json_list:
        human = sess['profile']['persona']['human']
        age = list(filter(lambda x: x.startswith('A'), human))[0]
        sex = list(filter(lambda x: x.startswith('G'), human))[0]

        situation = sess['profile']['emotion']['situation']
        disease = list(filter(lambda x: x.startswith('D'), situation))[0]
        situation = list(filter(lambda x: x.startswith('S'), situation))[0]

        row = {'situation': situation,
            'disease': disease,
            'age' : age,
            'sex' : sex,
            'emotion-type' : sess['profile']['emotion']['type'],
            'content' : sess['talk']['content']
        }
        df_data = df_data.append(row, ignore_index=True)
    return df_data

def get_emotion_class(emotion_id):
    emotion_id = emotion_id[1:]
    assert len(emotion_id.strip()) == 2

    if emotion_id.startswith('1'):
        return '분노'
    if emotion_id.startswith('2'):
        return '슬픔'
    if emotion_id.startswith('3'):
        return '불안'
    if emotion_id.startswith('4'):
        return '상처'
    if emotion_id.startswith('5'):
        return '당황'
    if emotion_id.startswith('6'):
        return '기쁨'
    
    raise ValueError('Unknown Emotion')

def get_human_utter(content : dict) -> list:
    utters = dict(filter(lambda x: x[0].startswith('H'), content.items()))
    utters = sorted(list(utters.items()), key=lambda x: x[0], reverse=False)
    return [text for id, text in utters]

if __name__ == "__main__":
    with open(pjoin(DATA_DIR, 'train.json')) as json_file:
        dev = json.load(json_file)

    with open(pjoin(DATA_DIR, 'test.json')) as json_file:
        test = json.load(json_file)

    dev_data = construct_df(dev)
    test_data = construct_df(test)

    dev_data['emotion-main-category'] = list(map(get_emotion_class, dev_data['emotion-type']))
    test_data['emotion-main-category'] = list(map(get_emotion_class, test_data['emotion-type']))

    dev_data['human-utter'] = list(map(get_human_utter, dev_data['content']))
    test_data['human-utter'] = list(map(get_human_utter, test_data['content']))

    dev_data.to_csv(pjoin(DATA_DIR, 'train.csv'), index=False, sep='\t')
    test_data.to_csv(pjoin(DATA_DIR, 'test.csv'), index=False, sep='\t')