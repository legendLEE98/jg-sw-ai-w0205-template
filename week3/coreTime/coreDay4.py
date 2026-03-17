strs = ["eat","tea","tan","ate","nat","bat"]

# 출력예시
# [["bat"],["nat","tan"],["ate","eat","tea"]]

# 일단 제일 먼저 해야할건
# input을 순회돌면서 단어를 쪼개고 

# 쪼갠걸 밸류로 저장할일?
# 밸류끼리 비교하는게 맞나?

# dict 특징이 뭐가 있는데
# 한 key 안에 여러 value를 동시 저장 가능하고
# 기능이 뭐가 있지?
# 키 찾기 = O(1)
# if word in strs: 같은 dict 안에 word가 존재하는지 구분 가능


# 분해를 어떻게 하지?
# 테스트 해볼 것
# dict의 key로 찾은 멀티 value를 word로 찾을 수 있는지.
result = []
dictionary = {}
dictionary['key'] = 'value1', 'value2'

print(dictionary)

for key, value in dictionary.items():
    if value[1] == 'value1':
        print("되나?")

# 멀티 value는 인덱스 번호를 지정해줘야 찾을 수 있음.
# 그러면 뭘 할 수 있나?를 생각해봤을 때

# 쪼개는걸 어떤 기준으로 쪼갤지?
def split():
    pass

# 같은 size만큼? 안됨

# 핵심사고 -> sort로 정렬한다