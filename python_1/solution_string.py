def solution(string):

    ss=string.split(" ")
    print(ss)
    str_update=""
    for str in ss :
        str_update=str_update+str+"\n"
    return str_update


print(solution("hello you !"))