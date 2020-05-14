# 用Python连接MySQL并进行CRUD #

Create Date: 2020-04-04 16:13:54

Update Date: 2020-04-04 16:15:33

Tag: MySQL, PyMySQL, Python

## 准备条件 ##

1. Python 2.7
2. MySQL 5.5
3. 安装 PyMySQL `pip install PyMySQL`

## 放码过来 ##

创建一数据表

```sql
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
```

连接数据库并进行CRUD操作
```python
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('abc@163.org', '123456'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('abc@163.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```

## 参考资料 ##

1. [PyMySQL · PyPI](https://pypi.org/project/PyMySQL/)
2. [Welcome to PyMySQL’s documentation](https://pymysql.readthedocs.io/en/latest/)

