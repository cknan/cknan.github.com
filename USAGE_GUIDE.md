# Ubuntu Embedding API 测试指南 / Ubuntu Embedding API Test Guide

## 已创建文件 / Created Files

✅ **基础文件已准备完成 / Basic files ready:**

1. `test_embedding_api.py` - 主要测试脚本 / Main test script
2. `quick_test.py` - 快速功能验证 / Quick functionality verification  
3. `setup_test.sh` - 设置脚本 / Setup script
4. `requirements.txt` - Python依赖 / Python dependencies

## 快速开始 / Quick Start

### 1. 验证基本功能 / Verify Basic Functionality
```bash
# 运行快速测试 / Run quick test
python3 quick_test.py
```

### 2. 系统准备 / System Preparation
```bash
# 安装系统依赖 / Install system dependencies
sudo apt update
sudo apt install -y python3-requests

# 或运行设置脚本 / Or run setup script
chmod +x setup_test.sh
./setup_test.sh
```

## 测试不同API / Testing Different APIs

### 🔧 测试本地端点 / Test Local Endpoint
```bash
# 如果你有本地embedding服务 / If you have local embedding service
python3 test_embedding_api.py --provider local --url "http://localhost:8080/embeddings" --text "测试文本"
```

### 🤗 测试Hugging Face (推荐开始) / Test Hugging Face (Recommended Start)

#### 方式1：本地模型 (无需API密钥) / Method 1: Local Model (No API Key Needed)
```bash
# 安装sentence-transformers / Install sentence-transformers
sudo apt install python3-pip python3-venv
python3 -m venv embedding_env
source embedding_env/bin/activate
pip install sentence-transformers

# 测试本地模型 / Test local model
python test_embedding_api.py --provider huggingface --local --text "Hello world"
```

#### 方式2：API模式 (需要API密钥) / Method 2: API Mode (Requires API Key)
```bash
# 将提示输入API密钥 / Will prompt for API key
python3 test_embedding_api.py --provider huggingface --text "你好世界"
```

### 🧠 测试OpenAI / Test OpenAI
```bash
# 需要先安装openai库 / Need to install openai library first
python3 -m venv embedding_env
source embedding_env/bin/activate
pip install openai

# 测试OpenAI API / Test OpenAI API
python test_embedding_api.py --provider openai --api-key "your-api-key" --text "Test embedding"
```

## 常见使用场景 / Common Use Cases

### 1. 验证API连接 / Verify API Connection
```bash
# 基本连接测试 / Basic connection test
python3 test_embedding_api.py --text "API连接测试"
```

### 2. 性能测试 / Performance Testing
```bash
# 长文本测试 / Long text test
python3 test_embedding_api.py --text "这是一个较长的测试文本，用于验证embedding模型的性能和处理能力。我们可以看到模型如何处理中文和复杂的语义内容。"
```

### 3. 多语言测试 / Multi-language Testing
```bash
# 英文 / English
python3 test_embedding_api.py --text "Hello, this is an English test."

# 中文 / Chinese
python3 test_embedding_api.py --text "你好，这是一个中文测试。"

# 混合语言 / Mixed languages
python3 test_embedding_api.py --text "Hello 你好 Bonjour مرحبا"
```

## 预期输出示例 / Expected Output Example

```
🧪 开始测试 / Starting test...
📡 提供商 / Provider: huggingface
📝 文本 / Text: 你好世界

============================================================
EMBEDDING API 测试结果 / TEST RESULTS
============================================================
✅ 测试成功 / Test Successful
📡 提供商 / Provider: Hugging Face (Local)
🤖 模型 / Model: sentence-transformers/all-MiniLM-L6-v2
📝 输入文本 / Input Text: 你好世界
📊 向量维度 / Embedding Dimensions: 384
⏱️  响应时间 / Response Time: 0.234s
🔢 向量样本 / Sample Values: [0.1234, -0.5678, 0.9012, -0.3456, 0.7890]
```

## 故障排除 / Troubleshooting

### ❌ 常见错误 / Common Errors

1. **ModuleNotFoundError: No module named 'requests'**
   ```bash
   sudo apt install python3-requests
   ```

2. **externally-managed-environment error**
   ```bash
   # 使用虚拟环境 / Use virtual environment
   python3 -m venv embedding_env
   source embedding_env/bin/activate
   pip install requests
   ```

3. **连接错误 / Connection Error**
   - 检查网络连接 / Check network connection
   - 验证API端点URL / Verify API endpoint URL
   - 检查防火墙设置 / Check firewall settings

### 📋 系统要求 / System Requirements

- Ubuntu 18.04+ (已在Ubuntu Plucky测试 / Tested on Ubuntu Plucky)
- Python 3.6+
- 网络连接 (用于下载模型或API调用) / Internet connection (for downloading models or API calls)

## 获取帮助 / Getting Help

```bash
# 查看所有选项 / View all options
python3 test_embedding_api.py --help

# 运行快速测试 / Run quick test
python3 quick_test.py
```

## 下一步 / Next Steps

1. ✅ **已完成** - 基本功能测试
2. 🔄 **可选** - 安装特定embedding库 (sentence-transformers, openai)
3. 🔑 **可选** - 获取API密钥 (OpenAI, Hugging Face)
4. 🚀 **可选** - 集成到你的应用中

现在你已经有了一个完整的embedding API测试工具集！