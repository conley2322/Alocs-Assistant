#!/usr/bin/env python3
import sys
import os
import subprocess
import shutil


def install_markitdown():
    """按需安装 markitdown 库"""
    try:
        import markitdown
        print("markitdown 已安装")
        return True
    except ImportError:
        print("正在安装 markitdown...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "markitdown[pdf]"],
                check=True,
                capture_output=True
            )
            print("markitdown 安装成功")
            return True
        except subprocess.CalledProcessError as e:
            print(f"安装失败: {e}")
            return False


def encrypt_file(input_path, output_path, key):
    """加密文件"""
    import base64
    
    def xor_encrypt(data, key_bytes):
        result = bytearray()
        for i, byte in enumerate(data):
            result.append(byte ^ key_bytes[i % len(key_bytes)])
        return bytes(result)
    
    with open(input_path, 'rb') as f:
        data = f.read()
    encrypted = xor_encrypt(data, key.encode())
    encoded = base64.b64encode(encrypted)
    with open(output_path, 'wb') as f:
        f.write(encoded)


def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_encrypted_md.py <pdf_file>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print(f"文件不存在: {pdf_path}")
        sys.exit(1)
    
    if not install_markitdown():
        sys.exit(1)
    
    from markitdown import MarkItDown
    
    base_name = os.path.basename(pdf_path)
    name_without_ext = os.path.splitext(base_name)[0]
    md_output = f"{name_without_ext}.md"
    
    print(f"正在转换 PDF: {pdf_path}")
    converter = MarkItDown()
    with open(pdf_path, 'rb') as f:
        result = converter.convert(f)
    
    markdown_content = str(result)
    
    with open(md_output, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"转换成功: {md_output}")
    
    pdf_dest = os.path.join("pdfs", base_name)
    if not os.path.exists(pdf_dest):
        shutil.copy2(pdf_path, pdf_dest)
        print(f"保存原始 PDF: {pdf_dest}")
    
    encrypted_output = os.path.join("references", f"{name_without_ext}.md.enc")
    encrypt_file(md_output, encrypted_output, "company2026")
    print(f"加密成功: {encrypted_output}")
    
    if os.path.exists(md_output):
        os.remove(md_output)
        print(f"清理临时文件: {md_output}")
    
    print("\n=== 处理完成 ===")
    print(f"原始 PDF: {pdf_dest}")
    print(f"加密 MD: {encrypted_output}")


if __name__ == "__main__":
    main()
