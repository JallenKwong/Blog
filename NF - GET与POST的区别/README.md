# GET与POST的区别 #

creation date:2020-02-11 23: 14: 44

tag:GET,POST

## The GET Method ##

GET is used to request data from a specified resource.

## The POST Method ##

POST is used to send data to a server to create/update a resource.

## Comparison ##

The following table compares the two HTTP methods: GET and POST.

-|GET|POST
---|---|---
**Purpose**|Request data from a specified resource|Send data to a server to create/update a resource
BACK button/Reload|Harmless|Data will be re-submitted (the browser should alert the user that the data are about to be re-submitted)
Bookmarked|Can be bookmarked|Cannot be bookmarked
**Cached**|Can be cached|Not cached
Encoding type|application/x-www-form-urlencoded|application/x-www-form-urlencoded or multipart/form-data. Use multipart encoding for binary data
**History**|Parameters remain in browser history|Parameters are not saved in browser history
Restrictions on data length|Yes, when sending data, the GET method adds the data to the URL; and the length of a URL is limited (maximum URL length is 2048 characters)|No restrictions
Restrictions on data type|Only ASCII characters allowed|No restrictions. Binary data is also allowed
Security|GET is less secure compared to POST because data sent is part of the URL<br> Never use GET when sending passwords or other sensitive information!|POST is a little safer than GET because the parameters are not stored in browser history or in web server logs
Visibility|Data is visible to everyone in the URL|Data is not displayed in the URL

## Reference ##

1. [https://www.w3schools.com/tags/ref_httpmethods.asp](https://www.w3schools.com/tags/ref_httpmethods.asp)

2. [http://cncc.bingj.com/cache.aspx?q=get+post&d=4979857532847597&mkt=en-US&setlang=en-US&w=JWqq_janEZvYk8IDi1Z_kEDcl8s_mNpe](http://cncc.bingj.com/cache.aspx?q=get+post&d=4979857532847597&mkt=en-US&setlang=en-US&w=JWqq_janEZvYk8IDi1Z_kEDcl8s_mNpe)

3. [get和post区别？ - 杨光的回答 - 知乎](https://www.zhihu.com/question/28586791/answer/145424285)
