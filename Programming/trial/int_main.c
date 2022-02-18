#include <stdio.h>

/*
// ';' 잊지말기
// 할당은 주소로 접근, &{var}
// ':', '-' 기호가 어디서 사용되냐에 따라 의미가 달라지기도 함
// main()은 파일 내 한 번만 사용 가능함
*/

int main() {
    int y;
    int x = 1;
    //y값은 변수 할당만 하고 x값도 입력
    y = (x >= 5) ? 5 : x;
    //':' <- '?'로 받은 조건문이 true일 때, x값을 재정의
    printf("%d", y);
    //return 0;
    
    //  conditions
    int num = 5;

    switch (num) {
        case 2:
            printf("\nTwo\n");
            break;
        case 3:
            printf("\nThree\n");
            break;
        case 5:
            printf("\nFive\n");
            break;
        default:
            printf("\nNot prime number!\n");
            //break;//sololearn.app C course에 따르면 break;없었음
            //{prettier}로 자동 생성된 switch~case~default문법엔 default:\n\tbreak;의 형식을 가지고 있음
        }
    return 0;
    // return 0을 하지 않으면, 0.419초, 하면 1.468초의 소요 시간으로 코드가 길어지면 격차가 예상보다 클 수 있는데
    // return 0을 하는 이유는 다음 함수 작동 전, init을 위함인가??
    // return 0의 위치에 따라 함수 내 강제 종료가 가능(이건 파이썬이랑 유사함)
    // 근데 왜 조건문과 위의 코드를 같이 돌리리까 출력까지의 소요 시간이 줄어든 것인가?
    // 그게 아니라 이미 run을 하고 받은 값이 있는데, 그 값에 덮어씌우다보니 연산 속도가 빨라진 것으로 보여지는 듯
 }