命令之间用 ; 隔开

> chmod命令 赋予文件属主执行文件的权限

引用一个变量时需要使用美元符,对变量进行赋值时则不要使用美元符.


在命令行上,命令总数在左侧,而重定向符号"指向"数据流动的方向.小于号说明数据正在从输入文件流向命令.

利用方括号[]区别算数运算的*号和通配符

shell看到列表值中的但因号并尝试私用它们来定义一个单独的数据值,有两种办法可解决:
* 使用转义字符(反斜线\)来将单引号转义
* 使用双信号来定义用到单引号的值

`for test in I don\'t know if "this'll" work`

IFS 用于修改字段分隔符
分隔符可以是:
* 空格
* 制表符
* 换行符




#### linux中shell变量$#,$@,$0,$1,$2的含义解释: 
变量说明: 
$$ 
Shell本身的PID（ProcessID） 
$! 
Shell最后运行的后台Process的PID 
$? 
最后运行的命令的结束代码（返回值） 
$- 
使用Set命令设定的Flag一览 
$* 
所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。 
$@ 
所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。 
$# 
添加到Shell的参数个数 
$0 
Shell本身的文件名 
$1～$n 
添加到Shell的各参数值。$1是第1参数、$2是第2参数…。 