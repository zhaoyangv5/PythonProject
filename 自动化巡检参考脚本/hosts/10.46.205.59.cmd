���̿ռ�#df -lP | grep -e 'dmmiso$' | awk '{print $5}'#<85%#
���̿ռ�#df -lP | grep -e 'dmcrmpd$' | awk '{print $5}'#<85%#
���̿ռ�#df -lP | grep -e 'dmftp$' | awk '{print $5}'#<85%#
���̿ռ�#df -lP | grep -e '/$' | awk '{print $5}'#<85%#
�ڴ�#free -m | sed -n '3p' | awk '{printf("%d%\n", 1319/30793*100)}'#<70%#
swapʹ�����#free -m | awk '{if(NR==4){print $3}}'#=0#
nginx���̴���#ps -ef | grep nginx | grep master | wc -l#=2#
tomcat6_dmp���̴���#ps -ef | grep tomcat6_dmp | grep -v grep | wc -l#=1#
tomcat_cms���̴���#ps -ef | grep tomcat_cms | grep -v grep | wc -l#=1#
tomcat6-01���̴���#ps -ef | grep tomcat6-01 | grep -v grep | wc -l#=1#
tomcat6_syndata���̴���#ps -ef | grep tomcat6_syndata | grep -v grep | wc -l#=1#
tomcat6_mnp���̴���#ps -ef | grep tomcat6_mnp | grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 10002 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 10003 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 10004 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 10007 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 10009 | grep LISTEN|grep -v grep | wc -l#=1#
