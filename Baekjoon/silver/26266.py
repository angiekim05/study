# 암호 해독
# 암호화하고 싶은 문장 seq, 암호키 key
# seq 와 k의 알파벳을 숫자로 바꾸고, 26이 넘는 경우 26을 뺀다
# 다시 숫자를 알파벳으로 만든 결과가 ps이며
# seq와 ps를 통해 k를 구하는 문제

# 즉 ps = (seq + keys(key의 반복))%26
# keys = (ps-seq+26)%26

seq = [ord(x)-64 for x in input()]
ps = [ord(x)-64 for x in input()]
keys = ""
n = len(seq)
for i in range(len(seq)):
    keys += chr((ps[i]-seq[i]+26)%26 + 64)
    
for i in range(1,n):
    # i는 key의 길이
    # key를 n//i번 반복한 것이 keys와 동일한지 확인
    if keys[:i]*(n//i) == keys:
        print(keys[:i])
        break