���̿ռ�#df -lP | grep -e 'echnweb$' | awk '{print $5}'#<85%#
���̿ռ�#df -lP | grep -e 'echncms$' | awk '{print $5}'#<85%#
���̿ռ�#df -lP | grep -e 'var$' | awk '{print $5}'#<85%#
���̿ռ�#df -lP | grep -e 'usr$' | awk '{print $5}'#<85%#
���̿ռ�#df -lP | grep -e '/$' | awk '{print $5}'#<85%#
�ڴ�#free -m | sed -n '3p' | awk '{printf("%d%\n", 1319/30793*100)}'#<70%#
swapʹ�����#free -m | awk '{if(NR==4){print $3}}'#=0#
tomcat1���̴���#ps -ef | grep tomcat1 | grep -v grep | wc -l#=1#
tomcat2���̴���#ps -ef | grep tomcat2 | grep -v grep | wc -l#=1#
tomcat3���̴���#ps -ef | grep tomcat3 | grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 8005 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 8006 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 8007 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 10009 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 10010 | grep LISTEN|grep -v grep | wc -l#=1#
�˿ڼ��#netstat -na | grep 10011 | grep LISTEN|grep -v grep | wc -l#=1#
