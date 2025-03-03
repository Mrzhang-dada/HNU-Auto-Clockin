# HNU-Auto-Clockin

HNU疫情防控和健康监测系统每日自动打卡

**使用前须知：本项目仅用于学习交流Python语言的学习与相关库的使用，不得用于获利 (NON FOR PROFIT)！如有体温异常等请如实上报！**

参考开源仓库：[中南大学nCov健康打卡定时自动脚本](https://github.com/lxy764139720/Auto_Attendance)

Duang~~~在GayHub里面找了一圈才看到一个湖大的打卡脚本，作者还不更新了，可能是信息院的同学都不想开源吧😅😅😅。于是在极度愤怒的情况下自己生了个玩意。

## 食用方法

本品通过GitHub Actions实现自动化，~~具有美容养颜、改善睡眠、舒肝理气、应该不会再被辅导员电话轰炸或被喝茶等功效。~~ 需要你做的前期工作有：

1. **创建一个GitHub账号，将本项目fork到你自己的账号下**
   ![QQ20210316-0.png](https://i.loli.net/2021/03/16/1krc8KwVATBUWCl.png)

2. **配置学号与个人中心密码**

    进入刚刚你fork过去到自己名下的项目，再进入Settings -> Secrets页面，点击New repository Secret，在Name栏输入**USERNAME**，Value栏输入你的学号。然后再添加一个Secret，Name栏为**PASSWORD**，Value栏填写你登录个人中心的密码。
    ![QQ20210316-2.png](https://i.loli.net/2021/03/16/4vqF6bsBPfSUDZc.png)

3. **填写打卡地址**

    你还需要分别以**PROVINCE**, **CITY**, **COUNTY**为NAME添加相应的Secret，Value中请注意须在地名后面添加“省“、”市“、”县/区“，如”湖南省“、”长沙市“、”岳麓区“。另外，详细地址默认为一个句号，你可以在源代码（clock_in.py）中修改。

4. **配置验证码识别API**

    由于不在微信环境下登录打卡系统需要验证码，所以需要使用网上的API来自动识别，请参考如下文章：

    [验证码识别的免费 OCR](https://www.cnblogs.com/xiaowenshu/p/11792012.html)

    按照文章操作注册百度智能云账号，并在控制台创建一个文字识别的应用，拿到**AppID**, **API Key**, **Secret Key**三个参数，再回到GitHub的Secrets界面，分别以**APP_ID**, **API_KEY**, **SECRET_KEY**为NAME创建三个SECRETS。

5. **开始自动化运行**

    进入到**Actions**界面，点击该工作流，然后Run workflow，即可开启自动化运行，你可以在设置里绑定邮箱以接收运行失败的通知，防止未来哪天打卡系统升级了你还蒙在鼓里。
    ![Snipaste_2021-03-15_21-56-15.png](https://i.loli.net/2021/03/16/oxSp8VYlfskWq53.png)
    ![Snipaste_2021-03-15_21-56-34.png](https://i.loli.net/2021/03/16/xETNukAF8hVS1nw.png)
    ![Snipaste_2021-03-15_21-57-11.png](https://i.loli.net/2021/03/16/XtR6lphCxLQg3an.png)

    你可以在如下界面中检查自动化运行情况：
    ![Snipaste_2021-03-15_21-57-49.png](https://i.loli.net/2021/03/16/8RwnFvq1ZBTuMxe.png)
    ![Snipaste_2021-03-15_21-58-06.png](https://i.loli.net/2021/03/16/MSok2D9VYJOBRK7.png)
    ![image.png](https://i.loli.net/2021/03/16/vnaiPEmyx5ugNlW.png)

    我设定为每天早晨6：10自动运行，你可以在/.github/workflows/python-app.yml文件里修改，请注意cron语法下的时间为零时区时间，需要将北京时间减8个小时，且分钟在前小时在后。详情参见[POSIX cron 语法](https://crontab.guru/)和[官方文档](https://docs.github.com/cn/actions/reference/events-that-trigger-workflows#)。

6. **如果一切顺利的话，应该没有第六步。若不是那样，可以在Discussion里面说。**

## 觉得有用的话给👴点个Star呗~
