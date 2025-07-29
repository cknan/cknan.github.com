#!/bin/bash

# Embedding API Test Setup Script for Ubuntu
# Ubuntu上embedding API测试设置脚本

echo "🚀 Setting up Embedding API Test Environment"
echo "设置Embedding API测试环境"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Installing..."
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv python3-full
fi

# Install system packages for Python libraries
echo "📦 Installing system Python packages..."
echo "安装系统Python包..."

sudo apt update
sudo apt install -y python3-requests python3-pip python3-venv python3-full

echo "🔧 Setting up virtual environment..."
echo "设置虚拟环境..."

# Create virtual environment if it doesn't exist
if [ ! -d "embedding_test_env" ]; then
    python3 -m venv embedding_test_env
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
source embedding_test_env/bin/activate

# Install basic dependencies in virtual environment
echo "📦 Installing dependencies in virtual environment..."
pip install requests

echo ""
echo "✅ Basic setup complete! You can now run tests:"
echo "基础设置完成！现在可以运行测试："
echo ""
echo "🔴 IMPORTANT: Activate the virtual environment first!"
echo "重要：首先激活虚拟环境！"
echo "   source embedding_test_env/bin/activate"
echo ""
echo "🧪 Test Examples / 测试示例:"
echo ""
echo "1. Test with system python3-requests (no virtual env needed):"
echo "   python3 test_embedding_api.py --provider local --url http://httpbin.org/post --text 'System test'"
echo ""
echo "2. Test with virtual environment:"
echo "   source embedding_test_env/bin/activate"
echo "   python test_embedding_api.py --text '你好世界'"
echo ""
echo "3. Install and test local Hugging Face model:"
echo "   source embedding_test_env/bin/activate"
echo "   pip install sentence-transformers"
echo "   python test_embedding_api.py --provider huggingface --local --text 'Hello world'"
echo ""
echo "4. Test with OpenAI API:"
echo "   source embedding_test_env/bin/activate"
echo "   pip install openai"
echo "   python test_embedding_api.py --provider openai --text 'Test embedding'"
echo ""
echo "📋 To install optional dependencies in virtual environment:"
echo "   source embedding_test_env/bin/activate"
echo "   pip install -r requirements.txt"
echo ""
echo "🆘 Help:"
echo "   python3 test_embedding_api.py --help"