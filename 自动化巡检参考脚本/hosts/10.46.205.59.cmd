磁盘空间#df -lP | grep -e 'dmmiso$' | awk '{print $5}'#<85%#
磁盘空间#df -lP | grep -e 'dmcrmpd$' | awk '{print $5}'#<85%#
磁盘空间#df -lP | grep -e 'dmftp$' | awk '{print $5}'#<85%#
磁盘空间#df -lP | grep -e '/$' | awk '{print $5}'#<85%#
内存#free -m | sed -n '3p' | awk '{printf("%d%\n", 1319/30793*100)}'#<70%#
swap使用情况#free -m | awk '{if(NR==4){print $3}}'#=0#
nginx进程存在#ps -ef | grep nginx | grep master | wc -l#=2#
tomcat6_dmp进程存在#ps -ef | grep tomcat6_dmp | grep -v grep | wc -l#=1#
tomcat_cms进程存在#ps -ef | grep tomcat_cms | grep -v grep | wc -l#=1#
tomcat6-01进程存在#ps -ef | grep tomcat6-01 | grep -v grep | wc -l#=1#
tomcat6_syndata进程存在#ps -ef | grep tomcat6_syndata | grep -v grep | wc -l#=1#
tomcat6_mnp进程存在#ps -ef | grep tomcat6_mnp | grep -v grep | wc -l#=1#
端口检查#netstat -na | grep 10002 | grep LISTEN|grep -v grep | wc -l#=1#
端口检查#netstat -na | grep 10003 | grep LISTEN|grep -v grep | wc -l#=1#
端口检查#netstat -na | grep 10004 | grep LISTEN|grep -v grep | wc -l#=1#
端口检查#netstat -na | grep 10007 | grep LISTEN|grep -v grep | wc -l#=1#
端口检查#netstat -na | grep 10009 | grep LISTEN|grep -v grep | wc -l#=1#
