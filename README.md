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

## 功能一览
[为什么你应该试试用Sublog写博客](http://www.cnblogs.com/zhengwenwei/p/3175646.html)

## 项目主页：
[sublog](https://github.com/AmongOthers/sublog)


## 使用方法：

1. 本项目是一个插件，首先要安装[Sublime Text 2](http://www.sublimetext.com/2)

1. 重命名sublog.sublime-settings.example为sublog.sublime-settings，配置你的登录信息，除了用户名，密码外，url也要修改为在管理->设置页面底部的metaweblog访问地址

1. 拷贝整个文件夹到Sublime Text 2插件库下(Preferences->Browse Packages)，注意命名为"sublog"

1. 安装[node.js](http://nodejs.org/)，用于语法高亮，效果：

		//javascipt代码
		var test = function() {
			console.log("语法高亮");


1. 重启Sublime Text 2, Done

1. 在博客园的管理->设置页面上传css样式(markdown.css)

1. 博客文章必须以md为后缀, "shift + F8"插入header信息，其中tags使用","分割，publish为"false"的时候表示为草稿; "shift + F9"发布新博客，修改后同样使用"shift + F9"发布更新（留意Sublime Text 2底下状态栏通知）

1. 要使用博客分类自动补全功能，需要开启Sublime Text 2 在文本模式下的补全功能，具体来说，就是在user settings中增加以下语句:

		"auto_complete_selector": "source, text"

	启动时会去同步一次博客分类，如果你修改了博客分类，需要执行"shift + F7"手动同步。

1. 代码块显示行号，在sublog.sublime-settings中添加:

	    "show_ln":true

1. 为了得到代码块中缩进在不同浏览器下的一致输出，请设置sublime text 2的tab为空格，例如我的设置如下：

		"tab_size": 4,
		"translate_tabs_to_spaces": true,
		"detect_indentation": true,

1. 支持github的代码块定义方式，例如下面的代码

	<pre><code class="no-highlight">
	```python ln_on
	import random

	class CardGame(object):
	    """ a sample python class """
	    NB_CARDS = 32
	    def __init__(self, cards=5):
	        self.cards = random.sample(range(self.NB_CARDS), 5)
	        print 'ready to play'
	```
	</code></pre>

	建议最好使用这种方式，由程序自动判断语言可能耗时较长。另外 `ln_on` 和 `ln_off` 作为辅助标记，表示本代码块是否启用行号。

	支持的语言： 1c, apache, avrasm, axapta, bash, cmake, cpp, cs, css, delphi, diff, django, dos, erlang-repl, erlang, go, haskell, ini, java, javascript, lisp, ls lua, mel, nginx, objectivec, parser3, perl, php, profile, python, renderman, ruby, scala, smalltalk, sql, temp tex, vala, vbscript, vhdl, xml

	特别的，使用no-highlight作为语言值表示本代码块不需要高亮。

1. 支持本地图片地址作为img的url标记，例如:

		![test](file://c:/image.png)
		![test](file://../image.png)

	在UNIX like上：

		![test](file:///home/AmongOthers/mario.gif)
		![test](file://~/mario.gif)

	当sublog检测到这是一个本地图片url的时候，会自动上传图片，并替换源文件的url为上传成功后得到的url

	![mario](http://images.cnitblog.com/blog/274442/201307/05151459-924c04129ec64e7fafac6a8ff040eb8f.gif)

	你还可以使用"shift + f10"发布当前选择的一行或多行里的"file://"url所指向的图片。

1. 为了吸引得到关注，所以在默认在每篇博客后面添加了Powered by Sublog的链接，你可以
在sublog.sublime-settings中添加:

		"advertisement": false

	来禁用。希望大家帮忙推广一下。:)

1. enjoy!

## Makrdown兼容性
[使用quick-markdown-example测试效果](http://www.cnblogs.com/zhengwenwei/archive/2013/06/05/3118185.html) 不支持表格和脚注


## 支持的平台
目前测试平台有windows7, ubuntu13.04，Mac平台应该也可以。如果使用中遇到问题，欢迎反馈。

> Hack everything!

## UPDATE

1. 添加博客分类自动补全功能

1. 添加文章基本结构的创建

1. 修复在ubuntu下获取博客分类的编码问题(13-06-19)

1. 语法高亮(13-06-22)

1. 显示行号

1. 修改settings的加载方式，每次执行命令时都加载，使得改变可以即时生效

1. 增加img支持