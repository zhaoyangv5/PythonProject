���̿ռ�#df -lP | grep -e 'dmmiso$' | awk '{print $5}'#<85%
���̿ռ�#df -lP | grep -e 'dmcrmpd$' | awk '{print $5}'#<85%
���̿ռ�#df -lP | grep -e 'chenesb$' | awk '{print $5}'#<85%
���̿ռ�#df -lP | grep -e 'var$' | awk '{print $5}'#<85%
���̿ռ�#df -lP | grep -e 'usr$' | awk '{print $5}'#<85%
���̿ռ�#df -lP | grep -e '/$' | awk '{print $5}'#<85%
�ڴ�#free -m | sed -n '3p' | awk '{printf("%d%\n", 1319/30793*100)}'#<70%
swapʹ�����#free -m | awk '{if(NR==4){print $3}}'#=0
nginx���̴���#ps -ef | grep nginx | grep master | wc -l#=2
tomcat6_mnpsp���̴���#ps -ef | grep tomcat6_mnpsp | grep -v grep | wc -l#=1
tomcat���̴���#ps -ef | grep 'tomcat/' | grep -v grep | wc -l#=2
tomcat6-01���̴���#ps -ef | grep tomcat6-01 | grep -v grep | wc -l#=1
tomcat6-02���̴���#ps -ef | grep tomcat6-02 | grep -v grep | wc -l#=1
tomcat6-03���̴���#ps -ef | grep tomcat6-03 | grep -v grep | wc -l#=1
tomcat_short_1���̴���#ps -ef | grep tomcat_short_1 | grep -v grep | wc -l#=1
tomcat_short_2���̴���#ps -ef | grep tomcat_short_2 | grep -v grep | wc -l#=1
tomcat_short_3���̴���#ps -ef | grep tomcat_short_3 | grep -v grep | wc -l#=1
memcached���̴���#ps -ef | grep memcached | grep -v grep | wc -l#=1
�˿ڼ��#netstat -na | grep 10002 | grep LISTEN|grep -v grep | wc -l#=1
�˿ڼ��#netstat -na | grep 10003 | grep LISTEN|grep -v grep | wc -l#=1
�˿ڼ��#netstat -na | grep 10004 | grep LISTEN|grep -v grep | wc -l#=1
�˿ڼ��#netstat -na | grep 10020 | grep LISTEN|grep -v grep | wc -l#=1
