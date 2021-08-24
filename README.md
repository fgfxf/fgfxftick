# fgfxf tick
河南师范大学  移动学工  自动打卡


设置如下secrets数据，然后开启action

GETPROXIESAPI="品易代理ip获取代理的ip"  #API设置为txt文本格式，以\r\n结束,格数  IP:PORT\r\nIP:PORT  最好是单行的
USERNAME="xxxx"   #py用户名
YOURPHONE="xxxx" #打卡数据：你的手机号
PASSWORD="xxx"   #品易代理登录密码
EMERGENCYPHONE="1xxxx58"   #打卡数据：紧急联系人   手机号
CONTACTS="xxx" #打卡数据：紧急联系人
COOKIEFILE="xxx.cookie"    #htu   cookie  ，数据为yuml=xxxxx
G_COOKIES="wxid=xxxxx;  remember_student_xxxx=xxxx"#抓包获取微信的cookie中间为; 隔开，第二个最后不带;

LOCATE="地点1;地点2"  #你家附近不同的定位，多个地点用英文;隔开，可以输入很多个，不止两个，最少2个
ANS="??.??"   你所在精度的小数点前2位，为了保护你的位置。

