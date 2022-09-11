//此程序用来启动escaps，并且防止重复启动

# include <iostream>
# include <string>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

using namespace std;

int main(){
    
    int ret = system("echo $(pgrep escaps) |grep -c \" \"");
        std::cout<<"ret = "<<ret<<std::endl;
    if (ret){
        system("/opt/escaps/escaps");
    }else{
        std::cout<<"错误：不能重复运行escaps！"<<std::endl;
        system("/opt/escaps/show_is_runging_alarm");
    }
    
    return 0;
}

