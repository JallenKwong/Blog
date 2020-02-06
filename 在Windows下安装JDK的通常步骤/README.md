# 在Windows下安装JDK的通常步骤 #

creation date:2020-02-05 22: 58: 26

tag:Windows, JDK

1. **获取安装包** 从官网或其他途径下载JDK的Windows版本的安装包，并点击安装。安装向导中无需选择配置项，默认操作即可，除了自定义的JDK安装目录。假设JDK的安装目录为`C:\Program Files\Java`。

2. **设置环境变量** 右击桌面上的计算机，在菜单项依次单击属性->高级系统配置->高级->环境变量。新建或修改一下系统变量：
	1. `JAVA_HOME` = `C:\Program Files\Java\jdk1.8.0_161`
	2. `CLASSPATH` = `.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar`
	3. `Path` += `%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;`

3. **测试安装结果** `Win + R`键入`cmd`进入命令行窗口，再输入`java -version`和`javac -version`。若得到反馈信息是对应的版本号，即JDK安装成功。