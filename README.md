# Alocs-Assistant

爱路客助手 - 基于公司内部文档回答政策、流程等问题的智能技能。

## 功能特点

- 基于公司内部文档回答政策、流程等问题
- 支持报销、请假、考勤、薪资福利、GP积分等公司相关问题
- 安全加密存储文档内容
- 一键安装脚本，方便快捷

## 目录结构

```
Alocs-Assistant/
├── SKILL.md              # 技能配置文件
├── index/
│   └── index.md          # 文档索引（明文，包含文件信息和判断逻辑）
├── scripts/
│   ├── locker.py                  # 加密/解密工具
│   └── pdf_to_encrypted_md.py     # PDF 转 MD 并加密工具
├── pdfs/                 # 原始 PDF 文件（可查看）
└── references/           # 加密的 MD 文件
```

## 安装指南

### 一键安装

复制以下命令到终端执行：

```bash
curl -fsSL https://raw.githubusercontent.com/conley2322/Alocs-Assistant/main/install.sh | bash
```

### 手动安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/conley2322/Alocs-Assistant.git
   cd Alocs-Assistant
   ```

2. 运行安装脚本：
   ```bash
   ./install.sh
   ```

## 使用方法

1. 安装完成后，在 Trae IDE 中使用 Alocs-Assistant 技能
2. 直接询问公司政策相关问题，如：
   - "如何申请报销？"
   - "请假流程是什么？"
   - "GP积分如何计算？"

## 安全说明

- 文档内容采用加密存储
- 解密后的内容仅供 AI 内部处理
- 禁止任何形式的逆向获取

## 维护指南

### 添加新文档

1. 将新的 PDF 文件放入项目根目录
2. 运行转换脚本：
   ```bash
   python scripts/pdf_to_encrypted_md.py [PDF文件路径]
   ```
3. 脚本会自动处理转换、加密和文件管理

## 技术依赖

- Python 3.6+
- 所需 Python 库会自动安装

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 许可证

MIT License
