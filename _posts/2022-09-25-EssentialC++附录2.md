---
layout:     post
title:      "Essential C++ 附录2"
date:       2022-09-25 15:00:01
author:     "Gnoy-Nus"
catalog: true
header-img: "img/post-bg-default.jpg"
tags:
    - C++
---
# 附录：泛型算法（二）

## inplace_merge 合并并取代（覆写）

输入三个参数：first、middle、last

从first到middle的序列和从middle到last的序列进行归并

第四个参数可以改变排序顺序（默认从小到大）

```c++
#include <algorithm>
int ia1[10]={1,2,3,4,5,6,7,8,9,10};
int *middle = ia1+5;
int *last = ia1+10;
inplace_merge (ia1,middle,last);
```

## iter_swap 元素互换

将两个iterator所指的元素互换

```c++
#include <algorithm>
iterator it1=iList.begin();
iterator it2=iList.begin()+4;
iter_swap(it1,it2);
```

## lexicographical_compare 以字典排列方式做比较

如果第一个序列小于或等于第二个序列返回true

```c++
#include <algorithm>
bool res = lexicographical_compare (svec1.begin(),svec1,end(),svec2.begin(),svec2,end());
```

## max\min 最大最小值

可提供第三个参数改变比较方式

## max_element\min_element 最大最小值所在位置

```c++
#include <algorithm>
iterator it=max_element(vec.begin(),vec,end());
```

## merge 合并两个序列

第六个参数改变排序方式、可有可无

```c++
merge(vec1.begin(),vec1,end(),vec2.begin(),vec2,end(),vec_result.begin(),greater<int>())
```

## nth_element 重新安排序列中第n个元素的左右两端

重新排列，使得小于第n个元素的在之前，大于的在其后

```c++
int ia[]={1,2,3,4,5,6,27,8,9,10,11,12};
nth_element(ia,ia+6,&ia[12]);//第n个元素为ia+6【27】
```

## partial_sort 局部排序

## partial_sort_copy 局部排序并复制

```c++
partial_sort (ia,ia+6,last);//ia到ia+5进行局部排序，其余不动
```

## partial_sum 局部总和

原序列每个元素计算前缀和(加上自身)得到新的序列

```c++
#include <numeric>
partial_sum(vec.begin(),vec.end(),vres.begin(),multiplies<int>());
```

## stable_partition 切割并保持相对次序

根据序列中的元素在一元运算的结果排序，true在前，false在后

stable版本保证相对顺序不变

```c++
#include <algorithm>
stable_partition(vec.begin(),vec.end(),func());//func()返回bool值
```

## random_shuffle 随机重排

```c++
#include <algorithm>
random_shuffle(vec.begin(),vec.end());
```

## remove_copy 移除元素并复制

先移除元素，然后复制剩余元素。

```c++
remove_copy(ia,ia+10,ia2,0);//将ia中非零元素拷贝到ia2
```

## remove_copy_if  有条件移除元素并复制

判断为true的元素除去，复制剩余元素

```c++
remove_copy(ia,ia+10,ia2,EvenValue());//将ia中偶数元素拷贝到ia2
```

## replace/replace_copy 取代某种元素并将结果复制到另一个容器

```
#include <algorithm>
replace(vec.begin(),vec.end(),oldvalue,newvalue);
replace_copy(vec.begin(),vec.end(),inserter(vec2,vec2.begin()),newvalue,oldvalue);
```

## replace_if

## replace_copy_if 有条件地取代并将结果复制到另一个容器

```
#include <algorithm>
replace_if(vec.begin(),vec.end(),bind2nd(less<int>(),10),newvalue);
```

## reverse/reverse_copy 颠倒次序并将结果复制到另一个容器

```
#include <algorithm>
reverse_copy(vec.begin(),vec.end(),vec_copy.begin());
```

## rotate/rotate_copy 旋转并将结果复制到另一个容器

三个参数：first\middle\last

将first到middle-1的元素和middle到last-1的元素互换

```
#include <algorithm>
char ch[]="abcdefg";
rotate(ch,ch+3,ch+7);//结果为defgabc
```

## search 搜寻某个子序列

返回iterator指向第一次出现的位置

```
#include <algorithm>
int *piter=search(str,str+25,sub_str,sub_str+4);
```

## search_n 搜寻连续发生n次的子序列

返回的iterator指向第一次出现的子序列，如果找不到返回序列的末端

```
char *found_str = search_n(str,str+26,2,"o");//寻找连续出现两次的"o"
```

## set_difference 差集

出现于第一序列，但未出现在第二序列的元素

前4个参数为两个序列开始和结束位置

第5个参数为新的序列的开始位置

## set_intersection 交集

把两个序列中均出现的元素编入新容器，同上为5参数

## set_symmetric_difference 对称差集

出现于第一序列，但未出现在第二序列的元素 以及 出现于第二序列，但未出现在第一序列的元素

## set_union 联集

出现于两个序列的元素都复制到新的容器，不重复

## sort/stable_sort 排序并保持等值元素的相对次序

```
#include <algorithm>
stable_sort(vec.begin(),vec.end(),greater<string>())
```

## transform 以两个序列为基础，交互作用产生第三个

```
transform(ia,ia+5.vec.begin(),double_val);//一元运算，传入一个序列
transform(ia,ia+5.vec.begin(),vec2.begin(),difference);//二元运算,结果存放在第4个参数的容器中
```

## unique/unique_copy 将重复的元素折叠缩编

连续出现的重复元素会被剔除

```
iter = unique(ia,ia+10)
unique_copy(ia,ia+10,ia2)
```
