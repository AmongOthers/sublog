<!--sublog
{
    "title":"Sublog: 支持Markdown和语法高亮的跨平台博客客户端",
    "category":"Thinking",
    "tags":"",
    "publish":"true",
    "blog_id":"3151861"
}
sublog-->

灵感来自[米米饭](http://www.cnblogs.com/meetrice/archive/2013/02/14/2911238.html)

## 项目主页：
[sublog](https://github.com/AmongOthers/sublog)


## 使用方法：

0. 本项目是一个插件，首先要安装[Sublime Text 2](http://www.sublimetext.com/2)

0. 重命名sublog.sublime-settings.example为sublog.sublime-settings，配置你的登录信息，除了用户名，密码外，url也要修改为在管理->设置页面底部的metaweblog访问地址

0. 拷贝整个文件夹到Sublime Text 2插件库下(Preferences->Browse Packages)，注意命名为"sublog"

0. 安装[node.js](http://nodejs.org/)，用于语法高亮，效果：

		//javascipt代码
		var test = function() {
			console.log("语法高亮");


0. 重启Sublime Text 2, Done

0. 在博客园的管理->设置页面上传css样式(markdown.css)

0. 博客文章必须以md为后缀, "shift + F8"插入header信息，其中tags使用","分割，publish为"false"的时候表示为草稿; "shift + F9"发布新博客，修改后同样使用"shift + F9"发布更新（留意Sublime Text 2底下状态栏通知）

0. 要使用博客分类自动补全功能，需要开启Sublime Text 2 在文本模式下的补全功能，具体来说，就是在user settings中增加以下语句:

		"auto_complete_selector": "source, text"

	启动时会去同步一次博客分类，如果你修改了博客分类，需要执行"shift + F7"手动同步。

0. 代码块显示行号，在sublog.sublime-settings中添加:

	    "show_ln":true

0. 支持本地图片地址作为img的url标记，例如:

		![test](file:///c:/image.png)
		![test](file:///../image.png)

	在UNIX like上：

		![test](file:////home/AmongOthers/mario.gif)
		![test](file:///~/mario.gif)

	当sublog检测到这是一个本地图片url的时候，会自动上传图片，并替换源文件的url为上传成功后得到的url

	![mario](http://images.cnitblog.com/blog/274442/201307/05151459-924c04129ec64e7fafac6a8ff040eb8f.gif)


0. enjoy!

## Makrdown兼容性
[使用quick-markdown-example测试效果](http://www.cnblogs.com/zhengwenwei/archive/2013/06/05/3118185.html) 不支持表格和脚注


## 支持的平台
目前测试平台有windows7, ubuntu13.04，Mac平台应该也可以。如果使用中遇到问题，欢迎反馈。

> Hack everything!

## UPDATE

0. 添加博客分类自动补全功能

0. 添加文章基本结构的创建

0. 修复在ubuntu下获取博客分类的编码问题(13-06-19)

0. 语法高亮(13-06-22)

0. 显示行号

0. 修改settings的加载方式，每次执行命令时都加载，使得改变可以即时生效

0. 增加img支持