# ssac_repo   
   
SSAC x AIFFEL first repository   
   
## branch 이름   

github에서 repository를 만들고 로컬에서 `git clone 깃헙레포주소`로 땡겨왔더니 
기본 브랜치 이름이 main 이다.   
   
학습 노드에서는 `master`가 기본인데 왜 다른지 찾아봤더니 2020년 10월 1일 부로 깃헙에서 만드는 레포의 기본 브랜치 이름을 `main`으로 바꿨다고 한다.   
[깃 허브 기본 브랜치 이름 변화](https://github.blog/changelog/2020-10-01-the-default-branch-for-newly-created-repositories-is-now-main/)   
[변화 내용과 앞으로의 계획](https://github.com/github/renaming/)   
정리하자면    
+이미 만들어진 레포지토리의 기본 브랜치 이름도 바뀌는 것은 아니다.   
  +기존의 기본 브랜치 이름을 지금 당장 바꿀수 있게하면서 깃헙 사용자들의 불편을 피하는 방법이 쉽지는 않다.   
  +하지만 2021년 1월에 기존 기본 브랜치 이름도 바꾸는 기능을 만들거다.   

깃 허브는 새로운 기본 브랜치 이름으로 `main`을 선택했고 다른 온라인 깃 관리 서비스도 이제는 `master`를 기본으로 사용하지 않을 것 처럼 얘기하는데 왜 그런 걸까?   
[깃 허브가 기본 브랜치 이름을 master 에서 main으로 바꾼 이유](https://www.theserverside.com/feature/Why-GitHub-renamed-its-master-branch-to-main)   
컴퓨터 산업에서 별 다른 뜻 없이 'slave-master'에 사용된 용어를 써왔던 것이 더이상 적절치 않아 변경하였다고 한다.   
별 생각 없이 편향된 것을 고치고자 하는 노력은 좋아 보인다.   
이제 막 깃을 알게 되었을 때 바뀌는 거라 나 같은 초심자에게는 오히려 좋아 보인다.   
생각 없이 써왔던 것을 생각 없이 또 쓰고 괜히 짜증내면서 변화를 타박하는 포지션을 자연스럽게 피할 수 있으니 아주 좋은 것 아닌가.   
   
   
그런데 기본 브랜치 이름 변경은 아직 git 에서는 이루어지지 않았다. 컴퓨터에 설치된 깃 버전은 `2.17.1`버전인데 `git init`으로 깃을 생성하면 아직 `master`가 기본 브랜치 이름으로 설정된다.   
그렇다면 로컬에서는 git init으로 깃을 생성하고 깃 허브에서는 레포를 만들어 로컬에서 `git remote add` 로 리모트 레포를 연결하면 기본 브랜치 관리는 어떻게 될까??   
일단 이걸 올리고 나중에 알아보기로 하자.   

