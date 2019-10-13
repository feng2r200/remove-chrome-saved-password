### 批量删除 Chrome 中指定用户名的全部密码

UCloud 云数据库页面的 URL 前缀经常变,导致记住了一堆密码,后来改了密码之后之前记录的还在,删除只能一个个删,用 Python 写个脚本帮我删

直接启动会打开一个没有用户的空的 Chrome 所以需要运行如下命令打开自己的Chrome:

> /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

切记,运行上面命令之前要关闭本机所有的 Chrome

在 Mac 上成功运行并达到目的, Windows 没试过,不太清楚