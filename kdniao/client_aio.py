#!/usr/bin/env python
# coding=utf-8
"""
client, 同步、异步
"""
import logging
import asyncio
import aiohttp
from asyncio import TimeoutError
from kdniao.client import KdNiaoClient
from kdniao.conf import HEADERS, DEFAULT_HTTP_RESP


class KdNiaoAsyncIOClient(KdNiaoClient):
    """
        Non-Blocking Client by asyncio

        Warning::: A ValueError will be raised if you are calling this in python < 3.4

        """

    def __init__(self, app_id, app_key, is_prod=True):
        """
        init
        :param int app_id: app id
        :param str app_key: app key
        :param bool is_prod: env type, prod or test, default is True
        """
        super(KdNiaoAsyncIOClient, self).__init__(app_id, app_key, is_prod=is_prod)

    @asyncio.coroutine
    def _request(self, rtype, data, **kwargs):
        """
        prepare and send request
        :param str rtype:
        :param data:
        :param timeout:
        :return:
        """
        timeout = kwargs.get("timeout")
        timeout = self._parese_time_out(timeout)
        if isinstance(timeout, (list, set, tuple)):
            timeout = timeout[0]

        url = self._gen_api_url(rtype)
        rdata = self._prepare_req_params(rtype, data)

        try:
            res = yield from self._post(url, rdata, timeout)
        except TimeoutError as exc:
            logging.error("timeout while request kdniao API: %s", exc, exc_info=True)
            res = DEFAULT_HTTP_RESP()
            res.url = url
            res.body = ""

        resp = self._parse_http_resp(res.status, res.reason, res.body, res.url)
        res = self._parse_api_resp(resp)
        return res

    @classmethod
    @asyncio.coroutine
    def _post(cls, url, data, timeout=None, callback=None):
        """
        :param str url: URL
        :param dict data: request parms
        :param tuple timeout: tuple or an int object
        :param function callback: callback function
        :return:
        """
        with aiohttp.ClientSession() as session:
            res = yield from session.post(url, data=data, headers=HEADERS, timeout=timeout)
            body = yield from res.read()
            setattr(res, "body", body)
            return res


__all__ = ["KdNiaoAsyncIOClient"]
