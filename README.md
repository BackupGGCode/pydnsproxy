#PyDNSproxy
用Python写的一个小程序，用了个非常简单的方法来忽略GFW的DNS缓存污染（暂不公布方法）。使用方法如下：

# 使用方法 #

## Windows ##
1. 下载[pydnsproxy](http://pydnsproxy.googlecode.com/files/DNSProxy-0.0.4-win32.exe)，安装在你喜欢的位置。（注：Windows Vista/7 的用户请使用管理员模式安装）

2. 将宽带连接（或者其他你喜爱的名字的连接）的dns服务器设置为127.0.0.1

3. Enjoy it!

### 备注 ###

1. 本软件默认使用OpenDNS的DNS服务器，如果你喜爱其他的**境外DNS服务器**，请修改主目录下的dnsserver.conf文件。（不知道的话请用Google搜索，注意别设成境内的了，不然就又回到祖国妈妈的怀抱了）

2. 修改dnsserver.conf后，请在控制面板->管理工具->服务中重启DNSProxy服务。

3. exe只是简单的7zip打包，如杀毒软件报告病毒应属误报。提供两个在线扫描结果：[VirusTotal](http://www.virustotal.com/zh-cn/analisis/1d6f6bd409fbe2f044787961c7a4015e289f22d4122c3a2bb77e9241f224bdd7-1261121253)、[VirScan](http://www.virscan.org/report/89d842cdfb9e0983837e51c1b0cf4a68.html)。

## Linux、Mac ##
目前没有针对Linux和Mac的包，但可以到[SVN](http://pydnsproxy.googlecode.com/svn/trunk/)里把py的源码checkout下来，除需要手动设置外，使用方法类似于Windows。

# 说明 #

什么是DNS缓存污染？参见维基百科的[这篇条目](http://zh.wikipedia.org/wiki/域名服務器緩存污染)。

DNSProxy只提供绕过DNS缓存污染的功能，而不能为你解决连接被重置的问题，更不能为你提供代理服务器翻墙。其他业务，请查询[GAppProxy](http://code.google.com/p/gappproxy/)。

既然不能翻墙，为什么开发这个工具？要知道能解决DNS缓存污染也能对付掉一部分GFW的封锁。比如说你可以使用IPv6，如果能解决掉DNS缓存污染，那么GFW在IPv6唯一的封锁手段（现今）也失效了。

# 更新日志 #
2009/12/18，更新到0.0.4版：

1. 将单线程的DNS本地服务器修改为多线程的，以解决设成服务后无法应对刚开机时的剧烈DNS解析请求的问题；

2. 默认设置成系统服务DNSProxy；

3. 自动安装包。

# 未来可能做的事 #
1. 域名查询的缓存功能；

2. 改善DNS污染的判断方法；

3. 支持模式匹配的Hosts。
