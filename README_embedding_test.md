# Embedding API Test Tool / Embedding API 测试工具

Simple tool to test embedding model APIs on Ubuntu / 在Ubuntu上测试embedding模型API的简单工具

## Quick Start / 快速开始

### 1. Setup / 设置
```bash
# Run setup script / 运行设置脚本
./setup_test.sh

# Or install manually / 或手动安装
sudo apt update
sudo apt install python3 python3-pip
pip3 install requests
```

### 2. Basic Test / 基础测试
```bash
# Simple test with default settings / 使用默认设置的简单测试
python3 test_embedding_api.py

# Test with Chinese text / 使用中文文本测试
python3 test_embedding_api.py --text "这是一个测试文本"
```

## Supported Providers / 支持的提供商

### 1. Hugging Face (Default / 默认)

#### API Mode (需要API密钥)
```bash
python3 test_embedding_api.py --provider huggingface --text "Hello world"
# Will prompt for API key / 会提示输入API密钥
```

#### Local Mode (本地模式)
```bash
# Install sentence-transformers first / 首先安装sentence-transformers
pip3 install sentence-transformers

# Test with local model / 使用本地模型测试
python3 test_embedding_api.py --provider huggingface --local --text "Hello world"

# Use specific model / 使用特定模型
python3 test_embedding_api.py --provider huggingface --local --model "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" --text "你好世界"
```

### 2. OpenAI

```bash
# Install OpenAI library / 安装OpenAI库
pip3 install openai

# Test with API key / 使用API密钥测试
python3 test_embedding_api.py --provider openai --api-key "your-api-key" --text "Test text"

# Use different model / 使用不同模型
python3 test_embedding_api.py --provider openai --model "text-embedding-3-small" --text "Test text"
```

### 3. Local API Endpoint / 本地API端点

```bash
# Test local API / 测试本地API
python3 test_embedding_api.py --provider local --url "http://localhost:8080/embeddings" --text "Test text"

# Test with custom endpoint / 使用自定义端点测试
python3 test_embedding_api.py --provider local --url "http://192.168.1.100:5000/v1/embeddings" --text "Test text"
```

## Command Line Options / 命令行选项

```bash
python3 test_embedding_api.py [OPTIONS]

Options:
  --provider {openai,huggingface,hf,local}  API provider (default: huggingface)
  --text TEXT                               Text to embed (default: "Hello, world! This is a test.")
  --model MODEL                            Model name
  --url URL                                API endpoint URL (for local provider)
  --api-key API_KEY                        API key
  --local                                  Use local model (for huggingface provider)
  --help                                   Show help message
```

## Example Output / 输出示例

```
🧪 开始测试 / Starting test...
📡 提供商 / Provider: huggingface
📝 文本 / Text: Hello, world! This is a test.

============================================================
EMBEDDING API 测试结果 / TEST RESULTS
============================================================
✅ 测试成功 / Test Successful
📡 提供商 / Provider: Hugging Face (Local)
🤖 模型 / Model: sentence-transformers/all-MiniLM-L6-v2
📝 输入文本 / Input Text: Hello, world! This is a test.
📊 向量维度 / Embedding Dimensions: 384
⏱️  响应时间 / Response Time: 0.234s
🔢 向量样本 / Sample Values: [0.1234, -0.5678, 0.9012, -0.3456, 0.7890]
```

## Troubleshooting / 故障排除

### Common Issues / 常见问题

1. **Python not found / Python未找到**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **pip not found / pip未找到**
   ```bash
   sudo apt install python3-pip
   ```

3. **Connection errors / 连接错误**
   - Check your internet connection / 检查网络连接
   - Verify API endpoint URL / 验证API端点URL
   - Check firewall settings / 检查防火墙设置

4. **API key issues / API密钥问题**
   - Ensure API key is valid / 确保API密钥有效
   - Check API key permissions / 检查API密钥权限

5. **Model download fails / 模型下载失败**
   ```bash
   # Clear cache and retry / 清除缓存并重试
   rm -rf ~/.cache/huggingface/
   pip3 install --upgrade sentence-transformers
   ```

### Detailed Installation / 详细安装

```bash
# Install all dependencies / 安装所有依赖
pip3 install -r requirements.txt

# Or install individually / 或单独安装
pip3 install requests
pip3 install sentence-transformers  # For local HF models
pip3 install openai                 # For OpenAI API
pip3 install torch                  # For deep learning models
pip3 install transformers           # For transformer models
```

## Testing Different Scenarios / 测试不同场景

### Batch Testing / 批量测试
```bash
# Test multiple providers / 测试多个提供商
for provider in huggingface local; do
    echo "Testing $provider..."
    python3 test_embedding_api.py --provider $provider --text "Test $provider"
done
```

### Performance Testing / 性能测试
```bash
# Test with longer text / 使用较长文本测试
python3 test_embedding_api.py --text "This is a much longer text to test the performance and capabilities of the embedding model when processing larger inputs that might be more representative of real-world usage scenarios."
```

### Multi-language Testing / 多语言测试
```bash
# Test with different languages / 测试不同语言
python3 test_embedding_api.py --text "Hello world"           # English
python3 test_embedding_api.py --text "你好世界"               # Chinese
python3 test_embedding_api.py --text "Hola mundo"            # Spanish
python3 test_embedding_api.py --text "Bonjour le monde"      # French
```

## Files Created / 创建的文件

- `test_embedding_api.py` - Main test script / 主要测试脚本
- `requirements.txt` - Python dependencies / Python依赖
- `setup_test.sh` - Setup script / 设置脚本
- `README_embedding_test.md` - This documentation / 此文档