# 关于这个目录

因为在本地写markdown时有时会插入截图，图片都存在于本地md文件的同级文件夹imgs下面，如果转移到github page就会失效

所以写了个python脚本，把md文件放到当前目录后运行.exe或.bat，输入指定folder

图片链接就可以转换到`https://gnoy-nus.github.io/img/in-post/指定folder/imgs`

之后只要把本地存放图片的imgs文件夹移动到项目中`img/in-post/指定folder/`就可以了