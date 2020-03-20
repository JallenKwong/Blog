# Projection投影 #

creation date:2020-03-14 22: 56: 42

tag:Github, DSN

## 解释一 ##

**Projection** means choosing **which columns** (or expressions) the query shall return.

Selection means which rows are to be returned.

if the query is

```sql
select a, b, c from foobar where x=3;
```
then "a, b, c" is the projection part, "where x=3" the selection part.

## 解释二 ##

In terms of query it is:

```sql
SELECT *PROJECTION* FROM Table
```

`*PROJECTION*` is expression for data transformation.

Example:

```sql
SELECT * FROM ORDER
```

In Hibernate, the Criteria equivalent would be:

```java
List orders = session.createCriteria(Order.class).list();
```

No projection here, we take data without transformation. If we want one:

```
SELECT NAME FROM PRODUCT
```

Here, the Projection class comes into play. The above query can be rewritten into a Criteria query as:

```java
List products=session.createCriteria(Product.class)
     .setProjection(Projection.property("name"))
     .list();
```

So we project all rows to single item: `name` field.

There are other projections: `Projection.rowCount()` for example (for `COUNT(*)`)

## 参考资料 ##

1. [What are projection and selection?](https://stackoverflow.com/questions/1031076/what-are-projection-and-selection)
2. [What is a Projection in NHibernate?](https://stackoverflow.com/questions/4746995/what-is-a-projection-in-nhibernate)
3. [Hibernate 4.3.11 Final - Relational Persistence for Idiomatic Java](https://docs.jboss.org/hibernate/orm/4.3/manual/en-US/html_single/)
