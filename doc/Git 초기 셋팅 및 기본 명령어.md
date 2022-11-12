# Git | 초기 셋팅 & 기본 명령어
1. [Git Repository 생성 및 초기 셋팅](#1-git-repository-생성-및-초기-셋팅)
2. [Git 기본 명령어 (add, commit, push, pull)](#2-git-기본-명령어-add-commit-push-pull)
3. [기타 명령어 (diff, log, reset, revert)](#3-기타-명령어-diff-log-reset-revert)
4. [Git bash 기본 명령어](#4-git-bash-기본-명령어)

## 1. Git Repository 생성 및 초기 셋팅 [Top](#)
### Git 초기 셋팅
- git 설치 [download](https://git-scm.com/downloads)
- 버전 확인
```bash
git --version
```
- 기본 설정
```bash
git config --global user.name "your_name"
git config --global user.email "your_email@gmail.com"
```
- 브랜치명 변경방법 (master -> main)
기본 브랜치명을 설정에서 변경
```bash
git config --global init.defaultBranch main
```

### Github에 Repository 생성
- 홈페이지에서 +버튼 > New repository를 통해 새로운 저장소 생성
- Repository name을 입력 > 공개/비공개 설정 > Create repository

### Github Repository와 내 컴퓨터 연결
- 내 컴퓨터에 연결할 폴더를 생성
#### git init
- 해당 폴더 위치에서 git을 사용 가능하도록 초기화
```bash
cd 로컬폴더위치
git init
```
#### git remote
- 저장소 연결
```bash
git remote add origin your_repository_url
```
- 저장소 연결 확인
```bash
git remote -v
```
#### git checkout
- 브랜치 변경: 이후 기록이 branch_name 으로 저장됨
```bash
git checkout branch_name
```
- 브랜치 새로 만들고 변경
```bash
git checkout -b new_branch_name
```
    
## 2. Git 기본 명령어 (add, commit, push, pull) [Top](#)
#### git add
- 파일 추가
```bash
git add file.py   # 하나씩
git add .         # 폴더 내에 있는 모든 파일 한꺼번에
```
#### git commit
- 파일 업로드 확정 (꼭 메시지와 함께)
```bash
git commit -m "add_messages"
```
#### git status
- 상태 확인
```bash
git status
```
#### git push
- 저장소에 업로드 (commit된 것만 저장소에 저장됨)
> -u 옵션은 앞으로 git push만 입력해도 origin main으로 연결하는 것
> --force 강제로 다 업로드 시킬때
```bash
git push repository_name branch_name # 기본 템플릿
git push -u origin main 
git push
git push --force origin main 
```
#### git pull
- 저장소에 있는 내용 가져오기 내 로컬 폴더와 병합(merge) 됨
commit을 해준뒤에 pull해주자! 아니면 충돌할 수 있음
```bash
git pull repository_name branch_name # 기본 템플릿
git pull -u origin main
git pull
```
    
## 3. 기타 명령어 (diff, log, reset, revert) [Top](#)
#### git diff
- 워킹 디렉토리와 git 저장소 사이 다른 commit 비교
```bash
git diff
git diff commit_id # 특정 commit과 비교
```
#### git log
- commit 변경사항을 추적
```bash
git log
```
#### git reset
- git add 취소하기
```bash
git reset HEAD file_name # file_name 파일만 취소
git reset HEAD           # add 한 전체 파일 취소
```
- git commit 취소하기 (파일 보존)
```bash
git reset --soft HEAD^    # add한 상태 (staged)
git reset --mixed HEAD^   # add하기전 상태 (unstaged)
```
#### git revert
- 협업시에는 작업을 취소할 때 revert를 주로 사용함
- commit을 삭제하는 것이 아니라
- 이전 commit의 반대 역할을 하는 데이터를 추가하는 방식으로
- 새로운 commit을 추가한다고 보면 됨
```bash
git revert --soft HEAD^    # add한 상태 (staged)
git revert --mixed HEAD^   # add하기전 상태 (unstaged)
```
    
## 4. Git bash 기본 명령어 [Top](#)
-    화면 초기화 : Ctrl + L
-    한 행의 처음과 끝 : Ctrl + A, Ctrl + E
-    목록 보기 : ls 또는 dir
-    파일의 내용 보기 : cat
-    특정 문자를 검색 : grep
-    디렉터리로 이동 : cd
-    디렉터리 생성 : mkdir
-    파일 삭제 : rm
-    파일 생성 : touch   

[git bash 기본 명령어 출처](https://gbsb.tistory.com/10)