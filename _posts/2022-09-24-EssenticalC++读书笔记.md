---
layout:     post
title:      "Essential C++ 读书笔记"
date:       2022-09-24 15:00:00
author:     "Gnoy-Nus"
catalog: true
header-img: "img/post-bg-default.jpg"
tags:
    - C++
---
# 第二章 面向过程的编程风格

- inline函数在编译时就地展开，调用头文件中的inline函数必须在头文件中定义该函数
- 声明可以在不同文件中多次声明，但定义只能定义一次【定义在头文件的inline函数例外】
- 函数指针需要用括号例如：`const vector<int>* (*func_ptr)(int)`
- 在头文件中声明变量，为了防止看起来像定义一样需要加入 `extern`关键字，`const Object`例外

  - ```c++
    const int func_cnt = 6; //const Object例外
    extern const vector<int>* (*func_array[func_cnt])(int)  //声明函数指针的数组，func_array不是const变量，它是指向const Object的指针
    ```

# 第三章 泛型编程风格

- 序列式容器：vector、list、deque
- 关联式容器：map、set
- 泛型算法：与容器种类、容器中数据类型无关的通用函数，例如：find()、begin()、end()等
- ```c++
  //容器初始化
  vector<int> ivec(1024); //1024为容器大小,默认值为0
  vector<string> svec(1024,"default_str"); //指定默认值
  ```
- list不支持iterator的的偏移运算，即不能调用 `list容器.erase(it,it+num)`
- function object：使用泛型算法时有时需要传入函数，为了减少调用函数的开销引入function object

  - ```c++
    //不用function object，传入函数指针
    #include <algorithm>
    bool cmp(int a,int b){
    	return a>b?true:false;
    }
    sort(vec.begin(),vec.end(),&cmp);

    //调用function object
    #include <algorithm>
    #include <functional>
    sort(vec.begin(),vec.end(),greater<int>());
    ```
  - function object adapter

    ```c++
    greater<int> gt();//function object
    bind2nd(gt,val);//function object adapter，将参数绑定至function object上，类似的还有bind1st,not1,not2
    ```
- map，调用map["xxx"]会将 `xxx`作为键放入map中并赋予初值，所以要用find函数【此处find不是泛型算法】确认map中是否有某个对象，或是count函数

  ```c++
  map <string,int> words;
  //find
  map <string,int>:;iterator it;
  it=words.find("dict");
  if(it!=words.end()) cout<<it->second; //find返回iterator
  //count
  if(words.count("dict")) cout<<words["dict"];//count返回个数
  ```
- set，可以使用count函数判断是否在set中
- inserter，插入迭代器，返回的是iterator，调用容器的插入函数代替赋值(=)运算，保证插入时容器能自动扩容

  ```c++
  #include <iterator>
  inserter(ivec,ivec.end()) //参数1：容器；参数2：插入操作起始点
  front_inserter(ivec) //调用容器的push_front(),适用于list和deque
  back_inserter(ivec) //调用容器的push_back()

  //应用于copy、unique_copy函数中
  copy(ilist.begin(),ilist.end(),front_inserter(ilist_clone));
  ```
- iostream_iterator：用iterator连接输入输出

  ```c++
  #include <iostream>
  #include <vector>
  #include <iterator>
  #include <fstream>
  using namespace std;

  int main(){
      ifstream inFile("input.txt");
      ofstream outFile("output.txt");

      istream_iterator<string> is(inFile);
      istream_iterator<string> eof; //不赋初值即表示end-of-file
      ostream_iterator<string> os(outFile," | ");//第二个参数为输出的分割符
      vector<string> text;

      copy(is,eof,back_inserter(text));
      copy(text.begin(),text.end(),os);
  }
  ```

# 第四章 基于对象的编程风格

- 在类的主体内部定义的函数自动视为inline函数；在类的主体外定义inline函数需要自己加inline【且需要放在头文件中】
- 避免两个类中的两个指针成员变量指向同一个可能被删除的地址。调用拷贝构造（重载=运算符）时遇到动态数组变量，需要先调用 `delete []var；`，再调用 `var=new type[cnt]`
- 类中的一些成员函数需要指明const，为了确保调用这些函数不会对其调用者(类的实例)造成变化，指明方式如：`int elem(int pos) const`

  - 这些const函数返回的值不能是non-const reference（与类相关的非常量引用），否则外部可能通过引用间接修改
  - ```
    otherClass val; //成员变量

    //错误，外部可能通过引用间接修改val
    otherClass& _val() const{return val}; 

    //正确写法，重载_val,non-const class object会自动调用没有加const的函数,const class object会调用const的函数
    otherClass& _val() {return val}; 
    const otherClass& _val() const{return val}; 
    ```
  - 一般，const class object应该只调用加了const的成员函数，虽然调用了non-const成分编译器可能也只会警告（只要确实没有修改const class object）
- mutable：表示对声明为mutable的变量的修改并不算修改class-object
- 想确认两个类是否为同一个类，用指针查看是否指向同一个地址
- static：表示类的所有实例共享的变量，或是与类的实例无关（即不存取non-static members）的函数

  - 类主体内声明过static后，在类的外部定义static函数不需要再写static
- 重载运算符：被定义在类里的重载的运算符包含隐含的参数this指针
- 前置的++运算符的参数表为空

  - 后置的++运算符的参数表有个int参数
- 不同的iterator在不同的类里用typedef的方式可以保证有相同的名字iterator；

  ```
  //example
  #include "TriangleIterator"
  class Triangle{
  	public:
  	typedef TriangleIterator iterator;  //使用typedef将迭代器统一命名
  	TriangleIterator begin(){
  		...
  	}
  }
  //外部使用方式
  Triangle::iterator it = tri.begin();
  ```
- friend声明：可以让非成员函数调用类的私有变量；friend的声明不受public、private影响；友元类的所有成员函数都是本类的友元函数
- 自定义function object，需要实现的类的成员函数是重载()运算符【function call运算符】

  ```c++
  //function object重载()运算符
  inline bool LessThan::operator()(int val){
  	return val<_val; //_val为自定义function object LessThan中的成员变量
  }
  //使用方式
  LessThan lt(10);  //构造function object，并赋予_val值为10
  find_if(vec.begin(),vec.end();lt)；  //将function object传入给泛型算法，将调用上面重载的()运算符，依次以迭代器指向的内容为参数
  ```
- 指向类的成员函数的指针

  ```c++
  class num_sequence{
      public:
          typedef void (num_sequence::*PtrType) (int);//指向num_sequence类的成员函数的指针，将其定义为PtrType类型，成员函数的参数为int，返回类型为void
          void fibo(int);
          void pell(int);
          void xxx(int);
          ...
      private:
      	PtrType _pmf;
  }
  ```

  ```c++
  PtrType pm=&num_sequence::fibo; //利用&指定函数指针指向一个函数
  ```

  - 指向类的成员函数的指针与指向函数的指针有所不同
    - 调用指向类的成员函数的指针的方式：`(classInstance.*ptr)(param)` 【注意.*符号，专门用于调用指向类的成员函数的指针】
- maximal munch编译规则：总是以合法序列符号中最长的解释代码，因此：
- `vector<vector<int> > vec` 中需要用空格分割开两个 `>`符号

# 第五章 面向对象的编程风格

- 动态绑定：调用基类的函数时，只有在run-time才能确定它是哪个子类的函数
- virtual声明：使成员函数在run-time根据具体的调用对象动态决定函数具体内容
- 构造子类时，会先后执行基类和子类的构造函数；析构子类时，会先后执行子类和基类的析构函数
- protected：子类可以调用protected中的成员，其他不行
- `static_cast`可以用于将整数转换为枚举成员，例如：`static_cast<some_enum_type>(num)`
- 纯虚函数： `virtual void gen_elem(int) = 0;` 将虚函数赋值为0，表示该虚函数在类中并无实际意义，称为纯虚函数。

  - 声明了纯虚函数的类不能直接实例化，只能使用他们的**赋予所有虚函数定义的子类**
  - 纯虚函数意味着子类必须要实现父类的虚函数才能实例化，也意味着当前的这个类只是个接口，所以析构函数最好不要设成纯虚函数
- 虚函数在子类中定义时，virtual可以省略，但建议加上
- 构造函数(包括拷贝构造)中，可以通过冒号语法调用基类的构造函数 `DerivedClass(const DerivedClass& b):BaseClass(b){}`
- 子类虚函数的定义需要与基类一致，包括 `const`关键字

  - 例外：基类的虚函数的返回类型是 `某个基类的引用或指针`时，子类的虚函数可以将返回值指定为 `该基类的某个子类的指针或引用`
- 基类的构造函数中，派生类的虚函数不会被调用，只能调用基类自身的虚函数；在析构函数中，同样成立
- 多态：在单一对象中展现多种型别，需要一层间接性来实现。

  - 因此参数只有声明为基类的指针或引用时才可以支持面向对象编程概念
  - 如果参数声明为基类的对象，那么传入的子类会被 `阉割`为基类，执行的虚函数也会变为基类的虚函数
- 执行期型别识别机制（Run-Time Type Identitification,RTTI)：

  - 每一个多态类，都对应一个 `type_info`对象,`name()`函数会返回类的名称
  - ```c++
    #include <typeinfo>
    inline const char* num_sequence::what_am_i() const{
    	return typeid(*this).name();
    }
    //支持==操作
    num_sequence *ps = &fib;
    if(typeid(*ps)==typeid(Fibonacci)){
    	//判断ps是否指向某个Fibonacci对象
        //但是不能直接将ps视为Fibonacci指针
        //因为ps是基类的指针，需要通过类型转换后才能调用Fibonacci类的函数
        Fibonacci* pf = static_cast<Fibonacci*>(ps)；
        pf->gen_elen(64);
    }
    //补充：static_cast有潜在危险，有转换失败的可能，所以需要放在if判断语句之内
    //补充：dynamic_cast则不同，它也是RTTI运算符，它会进行执行期检验操作
    if(Fibonacci* pf = dynamic_cast<Fibonacci*>(ps)){
        //如果ps所指对象属于Fibonacci类，那么会发生转换，否则返回0
        pf->gen_elen(64);
    }
    ```

# 第六章 template

- 函数中出现了模板参数时，尽量使用引用，避免构造
- 构造函数中出现了模板参数时，尽量使用冒号语法初始化变量，这样效率高，因为只需要一次拷贝构造函数即可

```c++
template <typename valType>
inline BTNode<valType>::BTNode(const valType& val):_val(val){
    //通常不这么做，因为valType可能是某个类
    //_val=val; 
    //如果这么做，对_val的赋值分为两步：1）对_val采用valType的默认构造函数 2）用赋值运算符将val的内容赋给_val
	_cnt=1;
	_lchild=_rchild=0;
}
```

- 指针的引用，既可以改变指针所指内容，也可以改变指针自身【如果不加引用，函数内部只是复制了指针，无法改变指针的指向】
- 模板里的参数可以是常量表达式

```c++
//len和beg_pos不用再当作类的成员变量存储
template<int len,int beg_pos>
class num_sequence{
	xxx
};
num_sequence<16> ns;
```

- 类里可以设置模板函数，模板类里也可以再设置模板函数

# 第七章 异常处理

- catch(...)：捕捉所有异常
- 捕捉异常后再次抛出该异常：catch内使用 `throw`即可

```
catch(int errno){
	xxx
	throw;
}
```

- `try\catch`语句，若try语句块内有异常，则执行catch语句块
- 只要发生异常，函数就会在return语句之前被中断
- 为了防止异常而导致的局部资源未能释放，可以使用局部资源管理的相关类,，例如：auto_ptr

```c++
#include <memory>

auto_ptr<int> p(new int); //若发生异常，也能在函数结束前释放内存
```

- 申请空间失败时，会抛出 `bad_alloc`类的异常，其继承自 `exception`类，其包含 `what()`函数返回 `const char*`,可用于查看异常信息

  - 抑制 `bad_alloc`异常：`ptext=new(nothrow) vector<string>;`，申请空间失败时ptext为0
- `ostringstream`类提供“内存内的输出操作”，能自动将对象转为string对象，需要头文件 `<sstream>`

  - `ostringstream`类提供 `str函数`可提取string对象
  - `string`类的 `c_str函数`返回 `const char *`

```c++
#include <sstream>
ostringstream ex_msg;
static string msg;
ex_msg<<"error"<<index<<"exceeds"<<bounds;//内存内的输出操作
msg = ex_msg.str(); //提取string对象
return msg.c_str(); //返回const char *
```
