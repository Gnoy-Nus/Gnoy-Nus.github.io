---
layout:     post
title:      "AutoHotKey"
date:       2024-01-19 11:00:00
author:     "Gnoy-Nus"
catalog: true
header-img: "img/post-bg-default.jpg"
tags:
    - AutoHotKey
---

## AutoHotKey 简介

- Autohotkey 定义了一种脚本语言（.ahk 文件），通过脚本可以快速自定义实用的简单操作，例如
  - 设置全局快捷键（打开某个应用然后进行某种固定操作等）
  - 游戏脚本
- 下载链接
  - [AutoHotkey/AutoHotkey: AutoHotkey - macro-creation and automation-oriented scripting utility for Windows. (github.com)](https://github.com/AutoHotkey/AutoHotkey)


## AutoHotKey  脚本使用方法

- 安装完Autohotkey后，只要编写完 `.ahk` 脚本文件后，`双击脚本文件运行`

## AutoHotKey 脚本基础知识

### 快速入门

- `;`为 ahk 脚本的注释符，等同于 C/C++中的 `//`，python 中的 `#`

`^1:: WinMaximize "A" ; 表示通过按键Ctrl+1最大化当前活跃窗口`
- 上方的语句就可以构成一个ahk脚本
  - `^1`表示按下键盘 `Ctrl+1` 
  - `::` 为分隔符
  - 分隔符后面的 `WinMaximize "A"`表示按下按键后的操作，最大化当前活跃的窗口
  - `"A"` 代表当前活跃窗口


### 以一个脚本为例

- 以下的脚本可以实现用 `Win+鼠标滚轮` 替换windows默认的切换桌面快捷键 `Ctrl+Win+Left/Right`

``` ahk
#WheelUp::{
	; #表示键盘的Win键，#WheelUp 等同于 Win+鼠标滚轮向上滑动 (这一行是注释)
	; 可以用一对大括号{} 包裹分隔符后面的操作语句
	send "#^{Right}" ; 表示按下按键 Win+Ctrl+Right, 即 Windows 本身的切换下一个桌面的快捷键 (分号后面是注释)
}

#WheelDown::{
	send "#^{Left}"
}
```

### 常见的 按键/操作 对应的符号

| 常见的按键/操作 | 对应的AHK脚本中的符号 |
| --------------- | --------------------- |
| Win             | #                     |
| Ctrl            | ^                     |
|                 |                       |
