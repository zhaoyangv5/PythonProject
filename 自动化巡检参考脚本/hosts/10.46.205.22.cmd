���̿ռ�#df -lP | grep -e 'echnweb$' | awk '{print $5}'#<85%
���̿ռ�#df -lP | grep -e 'var$' | awk '{print $5}'#<85%
���̿ռ�#df -lP | grep -e 'usr$' | awk '{print $5}'#<85%
���̿ռ�#df -lP | grep -e '/$' | awk '{print $5}'#<85%
�ڴ�#free -m | sed -n '3p' | awk '{printf("%d%\n", 1319/30793*100)}'#<70%
swapʹ�����#free -m | awk '{if(NR==4){print $3}}'#=0
nginx1���̴���#ps -ef | grep nginx1 | grep master | wc -l#=2
nginx2���̴���#ps -ef | grep nginx2 | grep master | wc -l#=2
nginxcms���̴���#ps -ef | grep nginxcms | grep master | wc -l#=2
�˿ڼ��#netstat -na | grep 10007 | grep LISTEN|grep -v grep | wc -l#=1
�˿ڼ��#netstat -na | grep 10008 | grep LISTEN|grep -v grep | wc -l#=1
