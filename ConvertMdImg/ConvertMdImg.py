#-*- coding:utf-8 -*-
import re
import os
import sys
def patch_md(filename):
    if filename.endswith('.md'):
        return True
    return False

def _patch_replace(text,folder):
    pat = "]\(.*images/image"
    pattern = re.compile(pat)
    replace=r'](https://gnoy-nus.github.io/img/in-post/'+folder+r'/images/image' #换成图片所存储的位置
    text=re.sub(pattern,replace,text)
    return text

def patch_replace(filename,folder):
    print(filename)
    with open(filename,'r+',encoding='utf-8') as f:
        text=f.read()
        text_file=_patch_replace(text,folder)
    with open(filename,'w',encoding='utf-8') as f:
        f.write(text_file)

#处理当前目录下的所有md文件，将其中的图片链接更换
def run():
    folder = input("输入img的上一级目录:\n")
    fileset = filter(patch_md,os.listdir("."))
    print(fileset)
    for filename in fileset:
        absfile = os.path.join(".",filename)
        patch_replace(absfile,folder)

if __name__=='__main__':
    run()