## 如果你想部署自用的vercel api

### ①注册

首先前往 [Vercel 官网](https://vercel.com/)，点击右上角的 sign up 进行注册。

![image.png](https://cdn.nlark.com/yuque/0/2021/png/8391485/1612880174758-059d6e22-d5ec-4478-9b8c-4a9d7c041f44.png)

极有可能遇到的 bug

若注册时提示 `Error:This user account is blocked.Contact support@vercel.com for more information.`

这是由于 `Vercel` 不支持大部分国内邮箱。可以将 `github` 账号主邮箱改为 `Gmail` 邮箱。

**但是**根据群友反应，将 `github` 账号主邮箱切换为 `Gmail` 以后，`Vercel` 又会提示需要使用手机号码验证。然而 `github` 并没有提供手机号码绑定的内容。

综上，建议一开始注册 `github` 账号时就使用 `Gmail` 等国外邮箱进行注册。

1. 国内访问`Gmail`的方案：

- - 直接使用 QQ 邮箱手机版，它提供 `Gmail` 的访问路线，可以直接注册并使用。
  - 使用 `Ghelper` 等浏览器插件访问。详情可以参考这篇文章：[玩转 Microsoft-Edge](https://github.com/Zfour/python_github_calendar_api/blob/master/posts/8c8df126)

1. 若是执着于当前`Github`账号，可以参考以下方案进行尝试:

- - 完成了 `Gmail` 等国外邮箱的注册，打开 [github-> 头像 ->settings->Emails](https://github.com/settings/emails)->Add email address, 并完成邮箱验证。
  - 在Add email address 下方的Primary email address 选项中将 `Gmail` 设置为主邮箱。

### ②新建项目，fork我的项目

打开[dashboard](https://vercel.com/dashboard)点击新建项目的`New Project`按钮。点击导入第三方库。

![image.png](https://cdn.nlark.com/yuque/0/2021/png/8391485/1612949541795-cfe67df4-a443-4604-86fd-a34ea9c34bed.png)



填入俺提供的自建 API 项目地址:

```
https://github.com/Zfour/friends_link_list_api
```



![image.png](https://cdn.nlark.com/yuque/0/2021/png/8391485/1612949577842-18cc23f8-5cf6-4f72-b892-d244d22a3089.png)

选择私有账户。点击`select`。



![image.png](https://cdn.nlark.com/yuque/0/2021/png/8391485/1612949622863-54b72f81-9add-479d-94ed-aeb125099afe.png)

选择github按钮然后会帮你将仓库克隆到你的github中，填入自定义仓库名称。

![image.png](https://cdn.nlark.com/yuque/0/2021/png/8391485/1612949755226-a97f3c75-8328-4630-91f2-2dd9dddf3665.png)

之后会识别出项目文件，单击 `Continue`。

![image.png](https://cdn.nlark.com/yuque/0/2021/png/8391485/1612949831064-f4b2cef1-eb64-4bac-8841-b991768ffee8.png)

`Vercel` 的 `PROJECT NAME` 可以自定义，不用太过在意，但是之后不支持修改，若要改名，只能删除 `PROJECT` 以后重建一个了。下方三个选项保持默认就好。 


![image.png](https://cdn.nlark.com/yuque/0/2021/png/8391485/1612949883724-064103a2-658f-49cb-b1e6-f3a7f0a511d1.png)



此时点击Deploy，`Vercel` 的api部署已经完成。

### ④检查API是否配置成功

访问**API链接**（图中链接+'/api'+查询参数）,如我的为

https://python-github-calendar-api-zfour.vercel.app/api/?zfour

如果显示数据则说明API配置成功。
