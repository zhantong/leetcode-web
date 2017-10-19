# LeetCode-Web

## 初始化

### 前端库依赖

下载[jQuery](https://jquery.com/download/)，并将`jquery-3.x.x.min.js`移动到`static`目录下。

下载[Semantic-UI](https://semantic-ui.com/introduction/getting-started.html)，并将`semantic.min.js`、`semantic.min.css`、`components`和`themes`移动到`static/semantic`目录下。

下载[pjax](https://github.com/defunkt/jquery-pjax)，并将`jquery.pjax.js`移动到`static`目录下。

### LeetCode题目列表

LeetCode题目列表用来展示题目名称，以及处理题目名称和slug之间的相互转换。

LeetCode题目列表使用SQLite数据库存储，其为根目录下的`leetcode.db`文件。

数据库中包含表`problem`，及字段`id`（题目编号）、`title`（题目名称）和`slug`（题目slug）。例如：

|  id |                      title                     |                      slug                      |
| :-: | :--------------------------------------------: | :--------------------------------------------: |
|  1  |                     Two Sum                    |                     two-sum                    |
|  2  |                 Add Two Numbers                |                 add-two-numbers                |
|  3  | Longest Substring Without Repeating Characters | longest-substring-without-repeating-characters |

可以使用[LeetCode-Spider](https://github.com/zhantong/leetcode-spider)来生成这个文件。

### LeetCode问题描述

LeetCode问题描述用来展示问题的详细描述。

每个问题的问题描述均对应一个HTML文件，其在`descriptions`目录下。目录结构为：

```
descriptions
    001. Two Sum.html
    002. Add Two Numbers.html
    003. Longest Substring Without Repeating Characters.html
    ...
```

可以使用[LeetCode-Spider](https://github.com/zhantong/leetcode-spider)来生成这个目录。

### LeetCode提交代码

LeetCode提交代码用来展示用户的题解。

每个提交代码均对用一个源代码文件（`*.py`、`*.java`、`*.cpp`等），其在`submissions`目录下。目录结构为：

```
submissions
    001. Two Sum
        C++
            Solution.cpp
        Java
            Solution.java
        Python
            Solution.py
    002. Add Two Numbers
        C++
            Solution.cpp
        Java
            Solution.java
        Python
            Solution.py
    ...
```

可以使用[LeetCode-Spider](https://github.com/zhantong/leetcode-spider)来生成这个目录。

### 整体目录结构示例

```
leetcode-web
    leetcode.db
    LeetCodeWeb.py
    static
        custom.css
        custom.js
        default.css
        jquery-3.2.1.min.js
        jquery.pjax.js
        semantic
            semantic.min.css
            semantic.min.js
            components
                ...
            themes
                ...
    templates
        base.html
        problem_description.html
        problem_list.html
        problem.html
        problems_summary.html
    descriptions
        001. Two Sum.html
        002. Add Two Numbers.html
        003. Longest Substring Without Repeating Characters.html
    submissions
        001. Two Sum
            C++
                Solution.cpp
            Java
                Solution.java
            Python
                Solution.py
        002. Add Two Numbers
            C++
                Solution.cpp
            Java
                Solution.java
            Python
                Solution.py
        003. Longest Substring Without Repeating Characters
            C++
                Solution.cpp
            Java
                Solution.java
            Python
                Solution.py
```
