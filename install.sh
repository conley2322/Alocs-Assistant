#!/bin/bash

# Alocs-Assistant 一键安装脚本

echo "===================================="
echo "Alocs-Assistant 安装脚本"
echo "===================================="

# 检查是否安装了 git
if ! command -v git &> /dev/null; then
    echo "错误: 未安装 git，请先安装 git"
    exit 1
fi

# 检查是否安装了 python3
if ! command -v python3 &> /dev/null; then
    echo "错误: 未安装 python3，请先安装 python3"
    exit 1
fi

# 定义技能目录
SKILL_DIR="$HOME/.agents/skills/Alocs-Assistant"

# 创建技能目录
if [ -d "$SKILL_DIR" ]; then
    echo "检测到已存在 Alocs-Assistant 技能目录，正在更新..."
    rm -rf "$SKILL_DIR"
fi

# 确保技能目录存在
mkdir -p "$HOME/.agents/skills"

# 克隆仓库
echo "正在克隆仓库..."
git clone https://github.com/conley2322/Alocs-Assistant.git "$SKILL_DIR"

if [ $? -ne 0 ]; then
    echo "错误: 克隆仓库失败"
    exit 1
fi

echo "仓库克隆成功！"

# 安装必要的 Python 依赖
echo "正在安装必要的依赖..."
python3 -m pip install --upgrade pip

# 安装 markdown 库（用于 PDF 转换）
python3 -m pip install markdown

# 安装 PyPDF2 库（用于 PDF 读取）
python3 -m pip install PyPDF2

echo "依赖安装完成！"

# 修复脚本权限
echo "正在修复脚本权限..."
chmod +x "$SKILL_DIR/scripts/locker.py"
chmod +x "$SKILL_DIR/scripts/pdf_to_encrypted_md.py"

# 清理临时文件
if [ -f "install.sh" ]; then
    rm install.sh
fi

echo "===================================="
echo "Alocs-Assistant 安装完成！"
echo ""
echo "使用方法："
echo "1. 技能已安装到：$SKILL_DIR"
echo "2. 在 Trae IDE 或 OpenCode 中使用 Alocs-Assistant 技能"
echo "3. 直接询问公司政策相关问题，如："
echo "   - 如何申请报销？"
echo "   - 请假流程是什么？"
echo "   - GP积分如何计算？"
echo ""
echo "如需添加新文档，请将 PDF 文件放入项目根目录并运行："
echo "python $SKILL_DIR/scripts/pdf_to_encrypted_md.py [PDF文件路径]"
echo ""
echo "提示：如需在其他环境中使用，请确保将 $SKILL_DIR 添加到相应的技能路径中"
echo "===================================="
