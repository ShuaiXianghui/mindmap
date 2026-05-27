# 🧠 思维导图

一个极简、本地优先的单页思维导图应用。基于 [Mind Elixir](https://mind-elixir.com/) v5 构建，纯前端，数据存储在浏览器本地。

## 快速开始

```bash
# 打开应用
open index.html

# 或使用 CLI 一键加载导图
./mindmap <你的导图.json>
```

无需安装、无需注册、无需后端。首次加载需联网（CDN 依赖），之后浏览器缓存可加速。

## 功能

- **多导图管理** — 创建、切换、删除、重命名
- **智能导入** — 支持 7 种 JSON 格式自动识别（AI 生成的 JSON 可直接导入）
- **导出** — JSON 格式导出 / PNG 图片导出
- **主题切换** — 浅色 / 深色模式
- **节点折叠** — 点击节点旁圆形按钮展开/收起子节点
- **键盘快捷键** — Tab 加子节点、Enter 加兄弟节点、Space 编辑、Ctrl+S 保存
- **自动保存** — 每次操作后 500ms 自动保存到 localStorage
- **CLI 模式** — `./mindmap xxx.json` 一键启动并自动加载

## CLI 用法

```bash
# 加载指定导图文件
./mindmap ganggan.json

# 不加参数，打开空白导图
./mindmap
```

服务器自动启动在 `localhost:8765`，浏览器自动打开。

添加到 PATH 后可在任意目录使用：

```bash
export PATH="$PATH:/path/to/mindmap"
```

## 与 AI 配合使用

让 Claude Code 或任何 AI 生成思维导图 JSON，然后用 CLI 打开：

> "帮我把 Python 学习路线整理成思维导图，保存 json 并打开"

AI 生成的 JSON 格式很自由，以下格式都能自动识别：
- `{ nodeData: { topic, children } }` — 标准格式
- `{ name/topic/title: "主题", children: [...] }` — 裸节点树
- `{ meta, nodes: [{ name, children }] }` — AI 常见输出
- `{ root: {...} }` / `{ data: {...} }` — 嵌套包装
- `{ mindmap/map: {...} }` — 工具特定格式
- `[{...}, {...}]` — 节点数组

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| Tab | 添加子节点 |
| Enter | 添加兄弟节点 |
| Space | 编辑节点 |
| Delete / Backspace | 删除节点 |
| Ctrl+Z | 撤销 |
| Ctrl+Y | 重做 |
| Ctrl+S | 手动保存 |
| 滚轮 | 缩放 |
| 拖拽空白区 | 平移画布 |

## 技术栈

- Mind Elixir v5.11.2（CDN）
- html2canvas（PNG 导出）
- localStorage（数据持久化）
- 纯 HTML/CSS/JS，单文件，零依赖构建

## 项目结构

```
.
├── index.html          # 主应用（单文件）
├── server.py           # CLI 本地服务器
├── mindmap             # CLI 启动脚本
├── CLAUDE.md           # Claude Code 配置
└── *.json              # 导图数据文件
```

## 许可

MIT
