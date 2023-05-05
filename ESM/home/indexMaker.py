
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
     "content": "너는 인기있는 블로거처럼 글을써줘 주제를 입력하면 주제와 관련된 목차를 작성하고 나에게 보여줘. 주제와 함께 다른 글이 입력되는 경우엔 주제와 글 모두 연관된 목차를 작성해줘야해. 아래에있는 양식을 지키면서 목차를 출력해줬으면 좋겠어———————말투는 따듯하게 목차는 주제를 이해하기위한 지식을 완성하는 방식을 작성해줘. 목차별로 충분한 설명과 예제를 작성할수 있게끔 만들어줘. 어떤 작동원리에 관한거라면 최상의 시나리오와 최악의 시나리오가 목차에 들어가면 좋겠어. -예시- 주제: 자바작동원리 목차: 자바가 어떻게 작동하는지와 관련된 개념인 힙 메모리, 참조에 의한 호출, 모듈, 클래스,등등과 실제작동을 알 수 있는 예제, 작동원리의 장점, 작동원리의 단점, 작동 방식의 최상의 시나리오, 작동방식의 최악의 시나리오, 빈번하게 일어아는 시나리오, 등등.———— 다음 입력에 주제가 입력될꺼야. 알겠다면 '주제를 입력해주세요!'라고 출력해줘."}
    
    
    
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


