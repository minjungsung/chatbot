import os
import json
import pandas as pd

def counting(path):
    cnt = 0
    data_dir = path

    for path in os.listdir(data_dir):
        if os.path.isfile(os.path.join(data_dir, path)):
            cnt += 1

    print(f'데이터 개수 = {cnt}')
    return cnt


## 용도별 목적 데이터 csv로 변환
target_path = "../원본데이터/용도별 목적대화 데이터/"
target_path_list = os.listdir(target_path)
target_path_list

total_data = 0
for i in range(len(target_path_list)):
    cnt = counting(target_path+target_path_list[i])
    total_data += cnt
print(f'총 데이터 개수 = {total_data}')

purpose = []
for i in range(len(target_path_list)):
    files = os.listdir(target_path+target_path_list[i])
    for k in range(len(files)):
        final_path = str(target_path)+str(target_path_list[i])+"/"+str(files[k])
        try:
            target_file = open(f"{final_path}", encoding="UTF-8")
            target_file = json.loads(target_file.read())
            for j in range(len(target_file['info'][0]['annotations']['lines'])):
                purpose.append(target_file['info'][0]['annotations']['lines'][j]['norm_text'][2:])
        except:
            print(f"error! {final_path}")


len(purpose)
purpose_df = pd.DataFrame({'text':purpose})
purpose_df.head()
purpose_df.tail()
purpose_df.to_csv("../변형데이터/용도별목적대화데이터.csv", index=False)


## 주제별 일상 대화 데이터 csv로 변환
target_path = "../원본데이터/주제별 일상 대화 데이터/"
target_path_list = os.listdir(target_path)
target_path_list

total_data = 0
for i in range(len(target_path_list)):
    cnt = counting(target_path+target_path_list[i])
    total_data += cnt
print(f'총 데이터 개수 = {total_data}')

ex = open(f"../원본데이터/주제별 일상 대화 데이터/TL_01. KAKAO/KAKAO_898_15.json", encoding="UTF-8")
ex = json.loads(ex.read())

ex['info'][0]['annotations']['lines'][7]['norm_text']
len(ex['info'][0]['annotations']['lines'])
target_path_list

files = files = os.listdir(target_path+target_path_list[0])
target_path+target_path_list[0]+files[0]
target_path_list

daily_conversations = []
for i in range(len(target_path_list)):
    files = os.listdir(target_path+target_path_list[i])
    for k in range(len(files)):
        final_path = str(target_path)+str(target_path_list[i])+"/"+str(files[k])
        try:
            target_file = open(f"{final_path}", encoding="UTF-8")
            target_file = json.loads(target_file.read())
            for j in range(len(target_file['info'][0]['annotations']['lines'])):
                daily_conversations.append(target_file['info'][0]['annotations']['lines'][j]['norm_text'])
        except:
            print(f"error! {final_path}")

len(daily_conversations)

daily_conversations_df = pd.DataFrame({'text':daily_conversations})
daily_conversations_df.head()
daily_conversations_df.tail()
daily_conversations_df.to_csv("../변형데이터/주제별일상대화데이터.csv", index=False)

## 일반상식 데이터 csv로 변환
common_sense = open(f"../원본데이터/ko_wiki_v1_squad.json", encoding="UTF-8")
common_sense = json.loads(common_sense.read())

len(common_sense['data'])
common_sense['data'][0]
common_sense['data'][0]['paragraphs'][0]['qas'][0]

query = []
answer = []
for i in range(len(common_sense['data'])):
    query.append(common_sense['data'][i]['paragraphs'][0]['qas'][0]['question'])
    answer.append(common_sense['data'][i]['paragraphs'][0]['qas'][0]['answers'][0]['text'])

len(query)
len(answer)

common_sense_df = pd.DataFrame({'intent':['일반상식']*len(query), 'query':query, 'answer':answer})
common_sense_df.head()
common_sense_df.tail()
common_sense_df.to_csv("../변형데이터/일반상식.csv", index=False)

## 네이버 영화 리뷰 csv로 변환
ratings = pd.read_csv("../원본데이터/ratings.txt", delimiter='\t')
ratings
ratings.to_csv("../변형데이터/영화리뷰.csv", index=False)