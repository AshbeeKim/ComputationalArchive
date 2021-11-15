#include <stdio.h>

void main() {
    /*
    char input_Value[50]="programming";
    scanf("%s", &input_Value);*/
    /* const char * input_Value[]="programming"; */
    /*
    char input_Value[]="programming";
    scanf("%s", &input_Value);*/
    //char input_Value="programming";
    char input_Value[];
    input_Value = "programming";
    printf("%s\n%15s\n%-15s\n%15.5s\n%-15.5s\n%.3s", input_Value, input_Value, input_Value,\
            input_Value, input_Value, input_Value);
}

/*일단 뭐가 잘못들어간 것 같은데...
C 규칙
1. 선언을 해야 함
2. 주소로 접근해야 함
3. gcc, gpp 다른가?다를 것 같기는 함
*/

/*
/*
* 
* 
* 
* 
*/