# -*- encoding: utf-8 -*-

DEBUG = True
DEF_PORT = 53
DEF_CONF_FILE = 'dnsserver.conf'
DEF_TIMEOUT = 0.4
DEF_MULTITHREAD = True


#缓存相关
DEF_CACHE = False
DEF_CACHE_TTL = 300 #单位为秒

#DNS服务器地址设置
DEF_LOCAL_HOST = '127.0.0.1'
DEF_REMOTE_SERVER = '8.8.4.4'		#受信服务器
DEF_DOMESTIC_DNS = '202.96.128.143'#国内非受信服务器

#DNS解释策略配置
DEF_DNS = DEF_REMOTE_SERVER #默认代理
DEF_DNS_IF_MATCH_PATTERN = DEF_DNS #匹配规则，使用国外DNS进行解释
DEF_DNS_IF_DOESNT_MATCH = DEF_DOMESTIC_DNS #规则不匹配，使用国内DNS进行解释
DEF_CONNECTION = 'tcp' #若规则匹配，使用tcp进行查询
