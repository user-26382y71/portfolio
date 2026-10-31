# APlayer 本地演示

一个用开源播放器组件做的练习页：不联网、不装依赖，双击就能听。

## 来源

| 项 | 内容 |
|---|---|
| 原项目 | [APlayer](https://github.com/DIYgod/APlayer) |
| 作者 | DIYgod |
| 许可证 | MIT |
| 使用方式 | 直接引用官方 `dist` 里的 js/css，**未修改原库源码** |

按 MIT 协议，保留原作者版权声明即可自由使用；本页仅作学习练习。

## 我做了什么

1. 用 Python 标准库写 `make_audio.py`，生成 8.8 秒的五声音阶音频（带泛音和衰减包络）
2. 手写 `index.html`，初始化 APlayer，塞进本地音频
3. 自己画了一个 SVG 封面

## 怎么运行

双击 `index.html` 即可，纯静态、不需要服务器、不需要联网。

> 浏览器可能拦截自动播放，点一下播放按钮就行。

## 目录

```
aplayer-demo/
├─ index.html          演示页
├─ cover.svg           自己画的封面
├─ demo.wav            生成的音频
├─ make_audio.py       音频生成脚本
└─ vendor/
   ├─ APlayer.min.js   官方构建产物（MIT）
   └─ APlayer.min.css
```

## 学到什么

- 开源库不是"下载整个仓库跑起来"，而是**取它的 dist 产物**，像用工具一样接进自己的页面
- 用 MIT 协议的项目，留个出处就能放心用
- 纯静态页面用 `file://` 就能跑，调试成本最低
