### GCC参数详解

gcc and g++分别是gnu的c & c++编译器 gcc/g++在执行编译工作的时候，总共需要4步 

1. 预处理,生成.i的文件[预处理器cpp] 
2. 将预处理后的文件不转换成汇编语言,生成文件.s[编译器egcs] 
3. 有汇编变为目标代码(机器代码)生成.o的文件[汇编器as] 
4. 连接目标代码,生成可执行程序[链接器ld] 


#### 参数详解

-x language filename
 设定文件所使用的语言,使后缀名无效,对以后的多个有效.也就是根据约定C语言的后 
缀名称是.c的，而C++的后缀名是.C或者.cpp,如果你很个性，决定你的C代码文件的后缀 
名是.pig 哈哈，那你就要用这个参数,这个参数对他后面的文件名都起作用，除非到了 
下一个参数的使用
可以使用的参数如下:
```
`c', `objective-c', `c-header', `c++', `cpp-output', `assembler', and `a 
ssembler-with-cpp'. 
```
-o 制定目标名称 缺省时位a.out

-inlcude file
包括某个代码,简单来说,就是便以某个文件,需要另一个文件的时候,就可以用它设 
定,功能就相当于在代码中使用#include<filename> 

-llibrary
制定编译的时候使用的库
thread时用-lpthread     math时用-lm


GCC 可同时用来编译 C 程序和 C++ 程序。一般来说，C 编译器通过源文件的后缀 
名来判断是 C 程序还是 C++ 程序。在 Linux 中，C 源文件的后缀名为 .c，而 C++ 源 
文件的后缀名为 .C 或 .cpp。但是，gcc 命令只能编译 C++ 源文件，而不能自动和 C 
++ 程序使用的库连接。因此，通常使用 g++ 命令来完成 C++ 程序的编译和连接，该程 
序会自动调用 gcc 实现编译。


---


