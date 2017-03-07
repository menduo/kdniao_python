kdniao\_python
==============

快递鸟 kdniao python sdk, with tornado async http client support.

-  github: https://github.com/menduo/kdniao_python
-  oschina: https://git.oschina.net/menduo/kdniao_python

    version: 0.1.1-beta

非官方。无利益关系。

TODO
====

-  doc, more doc
-  test, more test

Support API 支持的快递鸟 API
============================

-  [x] 即时查询 http://www.kdniao.com/api-track
-  [x] 物流跟踪 http://www.kdniao.com/api-follow
-  [x] 电子面单 http://www.kdniao.com/api-eorder
-  [x] 单号识别 http://www.kdniao.com/api-recognise
-  [x] 预约取件 http://www.kdniao.com/api-order
-  [x] 在途监控 http://www.kdniao.com/api-monitor
-  [x] 隐私快递 http://www.kdniao.com/api-safemail
-  [ ] 代收货款 http://www.kdniao.com/CollectionMoneyAPI.aspx

   -  [x] 用户信息类

      -  [x] 注册 9001
      -  [x] 更新 CMD1002
      -  [x] 查询 cmd1003
      -  [x] 提交返款银行信息 CMD1009
      -  [x] 查询返款银行信息 CMD1008
      -  [x] 查询用户额度 CMD1014

   -  [x] 服务申请类

      -  [x] 垫付业务申请 CMD1004
      -  [x] 直退业务申请 CMD1005
      -  [x] 普通代收货款申请 CMD1006
      -  [x] 查询服务申请状态 CMD1007

   -  [x] 订单类

      -  [x] 获取订单货款状态 CMD1010

所有 API 见 http://www.kdniao.com/api-all\ ，快递鸟可能会随时推出新的
API。

Install 安装
============

``pip install -u kdniao``

Usage 使用
==========

依赖
----

无论是在程序上，还是在命令行中，你都必须先获得快递鸟官方分配给你的 app
id 及 app key。可在 ``http://www.kdniao.com/reg`` 注册获取。

在命令行运行 ``kdniao`` 命令时，需要在命令行参数中指定 id
与key，或者预先在环境变量中指定 ``KDNIAO_APP_ID`` 及
``KDNIAO_APP_KEY``\ 。如：

1. ``KDNIAO_APP_ID={你的ID} KDNIAO_APP_KEY={你的Key} kdniao {运单号}``\ ，或：
2. 在 ``~/.bash_profile`` 中设置变量，并重新打开 shell 执行:
   ``kdniao {运单号}``\ ，或:
3. ``kdniao {运单号} --ik={APP_ID},{APP_KEY}``

Command Line 命令行
-------------------

.. code:: bash

    $ kdniao {运单号} --s=快递公司编码 --o=订单号 --ik={APP_ID},{APP_KEY}

    # 如：
    # $ kdniao 12345678 --s YTO
    # $ kdniao 12345678 --ik={APP_ID},{APP_KEY}

Sync 同步客户端
---------------

.. code:: python

    from kdniao.client import KdNiaoClient
    app_id = 12345678
    app_key = "YOUR_APP_KEY"
    is_prod = True

    logistic_code, shipper_code, order_code = 12345678, "SF", ""

    client = KdNiaoClient(app_id, app_key, is_prod)
    trace_res = client.api_track.track(logistic_code, shipper_code, order_code, timeout=(10, 10))

    # Your logic code here

Tornado Async Client 异步客户端
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from kdniao.client import KdNiaoAsyncClient
    app_id = 12345678
    app_key = "YOUR_APP_KEY"
    is_prod = True

    logistic_code, shipper_code, order_code = 12345678, "SF", ""

    async_client = KdNiaoAsyncClient(app_id, app_key, is_prod)
    trace_res = yield async_client.api_track.track(logistic_code, shipper_code, order_code, timeout=(10, 10))

    # Your logic code here

贡献
====

欢迎 start、fork 并贡献代码。也欢迎讨论交流、指正。

免费声明
========

1. 快递鸟官方 可能会随时推出新的 API，\ ``kdniao_python``
   未必会及时支持。
2. 快递鸟官方 可能会随时变动 API 协议，包括 API 网址、参数、签名算法等。

相关链接
========

-  快递鸟官网：\ http://www.kdniao.com/
-  快递鸟官网 API 列表：\ http://www.kdniao.com/api-all

联系
====

-  ``shimenduo AT gmail DOT com``
-  github: https://github.com/menduo/kdniao_python
-  oschina: https://git.oschina.net/menduo/kdniao_python
