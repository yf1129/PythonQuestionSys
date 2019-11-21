# 小游戏介绍
    # 1、根据题库内容出单选题
    # 2、提示作答，并给出结果

import os,json,sys

def to_answer(letter, c_len):
    letter = letter.upper()
    if len(letter) == 1 and 'A' <= letter <= 'Z':
        digit = ord(letter) - ord('A')
        if 0 <= digit < c_len:
            return digit, True
        else:
            return None, False  
    else:
        return None, False

def to_letter(n):
    return chr(ord('A') + n)

def ask_question(question, i):
    print('第{0}题: {1}'.format(i+1, question['question']))
    choices = question['choices']
    c_len = len(choices)
    for j in range(c_len):
        print('{0}: {1}'.format(to_letter(j), choices[j]))
    user_input = input('请输入答案：')
    user_answer, ok = to_answer(user_input, c_len)
    while not ok:
        user_input = input('输入格式错误，请输入选项前对应的字母：')
        user_answer, ok = to_answer(user_input, c_len)
    return user_answer == question['answer']


def read_question_file(filename):
    if not os.path.isfile(filename):
        return None
        
    with open(filename, 'r', encoding="utf-8") as f:
        try:
            return json.load(f)
        except ValueError as e:
            print(e)
            print('加载题库错误!!!')
            return None

def main(argv):
    if len(argv) < 2:
        print('请指定题库JSON文件')
        sys.exit(-1)
        
    print(argv[1])
        
    # 定义题库列表，每道题目为一个字典
    filename = os.getcwd() + '\question_list.json'
    question_json = read_question_file(filename)
    if not question_json:
        print('题库文件读取失败，请检查{0}'.format(filename))
        sys.exit(-1)
        
    name = question_json["name"]
    question_list = question_json['question_list']
    print('答题开始，当前题为：{0}'.format(name))
    
    # 遍历题库列表
    q_leln = len(question_list) # 题目总数
    correct_count = 0 # 答对数目
    for i,q in enumerate(question_list):
        # 展示题目、提示用户输入、判断答案
        if ask_question(q, i):
            correct_count += 1
            
    # 计算并展示正确率
    print('恭喜你！答题完成，共{0}道题目，你答对了{1}题。正确率{2:.2f}%。'.format(q_leln, correct_count, correct_count/q_leln*100))
    
    
if __name__ == '__main__':
    main(sys.argv)

