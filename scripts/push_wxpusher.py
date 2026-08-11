#!/usr/bin/env python3
"""Push Horizon daily Chinese digest to WeChat via WxPusher"""
import glob, os, json, urllib.request

files = sorted(glob.glob('docs/_posts/*-zh.md'), reverse=True)
if not files:
    print('no zh digest, skip')
    raise SystemExit(0)
lines = open(files[0], encoding='utf-8').read().splitlines()
title = next((l.lstrip('# ') for l in lines if l.startswith('# ')), 'Horizon Daily')
body = '\n'.join(lines[1:])
content = '## ' + title + '\n\n' + body[:4000]
content += '\n\n[查看完整日报](https://zuoser.github.io/Horizon/)'
payload = {
    'appToken': os.environ['WXPUSHER_APP_TOKEN'],
    'content': content,
    'contentType': 3,
    'uids': [os.environ['WXPUSHER_UID']],
}
req = urllib.request.Request(
    'https://wxpusher.zjiecode.com/api/send/message',
    data=json.dumps(payload).encode(),
    headers={'Content-Type': 'application/json'})
resp = urllib.request.urlopen(req, timeout=30)
print('WxPusher:', resp.read().decode()[:300])
