
import sys
import os
import openai
import json

#openai.organization = "org-RW97zLho4qp0kezjTGL3HLRb"
mykey = "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"
openai.api_key = f"{mykey}"

def response(message_list):
    answer = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message_list)
     
    return answer['choices'][0]['message']['content']


message_list = [
    {"role": "system",
     "content":"너는 입력된 목차를 바탕으로 인기있는 블로거처럼 글을써줘. ———————말투는 따듯하게해줬으면 좋겠어. 제목은 목차들의 주제를 관통하는 깔끔한 제목 목차별로 자세한 설명과 예제가 들어가면 좋겠다. 설명은 사실에 기반해야해. 결론은 본문내용을 요약하고 학습 방향성을 제시해주면 좋겠어. 글쓰기 방식:각 챕터별로 짜임새있는 글쓰기, 글작성이 마무리 된 후 퇴고작업으로 글 완성도 높히기———— 반드시 이 형태와 요청을 기억해줘."}
     
    
    
    
]



#주제 입력, 프롬프트 입력, 인덱스 받기,목차수정

while(True):
    print("입력")
    user = sys.stdin.readlines()
    if(user == "0"):
        break
    message_list.append({"role": "user", "content": f"{user}"})
    indexs =  response(message_list)
    message_list.append({"role": "assistant", "content":f"{indexs}\n\n수정할 부분이 있다면 고쳐주시거나 어떤 부분을 추가할지 알려주세요. 수정할 부분이 없다면 0을 입력해주세요."})
    print(indexs)

    

result = indexs


