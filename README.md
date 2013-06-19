#blog {"category": "", "blog_id": "3120994", "tags": "", "publish": "true", "title": "Sublog: 在Sublime Text 2中用Makrdown发表博客"}

灵感来自[米米饭](http://www.cnblogs.com/meetrice/archive/2013/02/14/2911238.html)

## 项目主页：
[sublog](https://github.com/AmongOthers/sublog)


## 使用方法：

0. 重命名meetrice.sublime-settings.example为meetrice.sublime-settings，配置你的登录信息，除了用户名，密码外，url也要修改为在管理->设置页面底部的metaweblog访问地址;

0. 拷贝整个文件夹到插件库下(Preferences->Browse Packages);

0. 重启Sublime text2, "shift + F8"插入header信息，其中tags使用","分割，publish为"false"的时候表示为草稿;

0. 博客文章以md为后缀, "shift + F9"发布新博客，修改后同样使用"shift + F9"发布更新（留意Sublime Text 2底下状态栏通知）

0. 在博客园的管理->设置页面上传css样式(markdown.css)

0. 要使用博客分类自动补全功能，需要开启sublime text 2 在文本模式下的补全功能，具体来说，就是在user settings中增加以下语句:

		"auto_complete_selector": "source, text"
	加载Sublog插件后会去同步一次博客分类，如果你修改了博客分类，需要执行"shift + f7"手动同步。

0. enjoy!

## Makrdown兼容性
[使用quick-markdown-example测试效果](http://www.cnblogs.com/zhengwenwei/archive/2013/06/05/3118185.html) 不支持表格和脚注

## 前方危险
在没有Python经验的情况下，用了四天的下班时间做出来的东西，所以只是it works的程度，目前测试平台有windows7, ubuntu13.04。如果使用中遇到问题，欢迎反馈。

> Hack everything!

## UPDATE

0. 添加博客分类自动补全功能

0. 添加文章基本结构的创建

0. 修复在ubuntu下获取博客分类的编码问题(13-06-19)