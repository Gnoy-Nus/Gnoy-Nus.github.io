---
layout:     post
title:      "Essential C++ 附录1"
date:       2022-09-25 15:00:00
author:     "Gnoy-Nus"
catalog: true
header-img: "img/post-bg-default.jpg"
tags:
    - C++
---
# 附录：泛型算法（一）

## accumulate 元素累加

将容器内所有参数相加，并加上第三个参数，第四个参数为二元运算操作，可以替代加法运算

```c++
#include <numeric>

iresult = accumulate(ia，ia+8,0);
iresult = accumulate(iList.begin()，iList.end(),0,plus<int>());
```

## adjacent_difference 相邻元素的差值

将数列中每个元素减去前一个元素得到差值(第一个元素的差值为0)，此差值构成新的数列，第三个参数为新数列的首地址，第四个参数为二元运算操作，可以替代减法运算

```c++
#include <numeric>
adjacent_difference(ilist.begin(),ilist.end(),iresult.begin());
adjacent_difference(ilist.begin(),ilist.end(),iresult.begin()，multiplies<int>);
```

## adjacent_find 搜索相邻重复元素

搜寻第一组相邻且重复的元素，返回第一个重复元素的的iterator，第三个参数可以设置传入重载了 `()`的类

```c++
#include <algorithm>
class TwiceOver{
	bool operator()(int val1,int val2){
		return val1==val2/2? true:false;
	}
}
piter = adjacent_find(ilist.begin(),ilist.end());
piter = adjacent_find(ilist.begin(),ilist.end(),TwiceOver());
```

## binary_search() 二元搜寻

对默认为从小到大排序的序列进行二叉查找，可以传入第四个参数以指示排序顺序，该算法返回bool值

```c++
#include <algorithm>
found=binary_search(ilist.begin(),ilist.end(),value);
found=binary_search(ilist.begin(),ilist.end(),value,greater<int>);
```

## copy 复制

将第一个容器的元素一一复制到第二个

```c++
#include <algorithm>
copy(vec.begin(),vec.end(),result.begin());
```

## copy_backward 逆向复制

与copy相同，只是逆向操作，vec.end()-1复制到result.end()-1,vec.end()-2复制到result.end()-2，依次类推

```c++
#include <algorithm>
copy(vec.begin(),vec.end(),result.end());
```

## count 计数

返回与value值相等的元素个数

```c++
int cnt = count(vec.begin(),vec.end(),value);
```

## count_if  在特定条件下计数

返回容器中 `被某种特定运算符评估为true`的元素个数

```c++
#include <algorithm>
class Even{
	bool operator()(int val){
		return !(val%2);
	}
}
count_if(vec.begin(),vec.end(),bind2nd(less<int>(),10));
count_if(vec.begin(),vec.end(),Even());
```

## equal 判断相等与否

如果第二个数列的元素较多，多出来的部分不考虑。可以自定义运算替代默认的equality的运算符

```c++
#include <algorithm>
class TwiceOver{
	bool operator()(int val1,int val2){
		return val1==val2/2? true:false;
	}
}
int ia1[]={1,1,2,3};
int ia2[]={1,1,2,3,5,8};
res = equal(ia1,ia1+4.ia2); //true
res = equal(ia1,ia1+4.ia2,TwiceOver());
```

## fill 改填元素值

将容器中的元素值都改为value

```c++
#include <algorithm>
fill(vec.begin(),vec.end(),value);
```

## fill_n 改填元素值，n次

将容器中的元素值都改为value，但只设定n个元素

```c++
#include <algorithm>
fill(vec.begin(),count,value);
```

## find 搜寻

搜索特定值，返回第一个找到的iterator

```c++
#include <algorithm>
pointer=find(ilist.begin(),ilist.end(),value);
```

## find_end 搜索某个子序列最后一次出现的位置

成功则返回第二个序列中第一个元素的iterator。如果失败返回第二个序列的末尾，也就是第四个参数。可以指定二元运算替代equality运算符

```c++
#include <algorithm>
int ia[17]={7,3,3,7,6,5,8,7,2,1,3,7,6,3,8,4,3};
int seq[3]={3,7,6};
found_it = find_end(ia,ia+17,seq,seq+3); //found_it指向ia[10]
```

## find_first_of 搜寻某些元素的首次出现地点

返回首次出现的第二个序列中任意一个元素的首次出现位置（iterator）。如果失败返回第一个序列的末尾。可以指定二元运算替代equality运算符

```c++
#include <algorithm>
string s_array[]={"Ee","eE","ee","Oo","oo","ee"};
string to_find[]={"oo","gg","ee"};
found_it = find_first_of(s_array,s_array+6,to_find,to_find+3); //返回&s_array[2]
```

## find_if 在特定条件下搜索

指定二元运算符，寻找第一个满足条件的元素返回iterator，找不到则返回容器的end()

```c++
#include <algorithm>
class Even{
	bool operator()(int val){
		return !(val%2);
	}
}
find_if(vec.begin(),vec.end(),bind2nd(less<int>(),10));
find_if(vec.begin(),vec.end(),Even());
```

## for_each 对范围内的每一个元素实行某操作

第三个参数为需要进行的操作，返回值会被忽略，操作不能修改元素内容，除非使用 `transform`

```c++
#include <algorithm>
template <typename type>
void print_element(type elem){
    cout<<elem<<endl;
}
for_each(vec.begin(),vec.end(),print_element);
```

## generate 以指定操作的运算结果充填范围内元素

```c++
#include <algorithm>
template <typename type>
class gen_by_two{
  int operator(){
        static int seed=1;
        return seed+=2;
    }
}
vector<int> vec(10);
generate(vec.begin(),vec.end(),gen_by_two());
```

## generate_n 以指定操作的运算结果充填n个元素

```c++
#include <algorithm>
generate_n(vec.begin(),vec.size(),gen_by_two()); //第二个参数指定n
```

## includes 涵盖于

如果第二序列的每个元素都在第一序列中，则返回true；传入的两个序列都必须先进行排序

```c++
#include <algorithm>

sort(ia1,ia1+12);
sort(ia2,ia2+6);
res=include(ia1,ia1+12,ia2,ia2+6);//true
```

## inner_product 内积

两个序列进行按元素相乘，然后累加，再加上一个初值，得到结果；

相乘|累加操作可替换

第五个参数取代累加操作

第六个参数取代相乘操作

```c++
#include <numeric>
int ia1[]={7,3,3};
int ia2[]={3,7,6};
int res = inner_product(ia1,ia1+3,ia2,0)； //4个参数
  
vector<int> vec1(ia1,ia1+3);
vector<int> vec2(ia2,ia2+3);
int res2 = inner_product(vec1.begin(),vec1.end(),vec2.begin(),0,minus<int>(),plus<int>()); //6个参数
```
