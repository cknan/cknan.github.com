#!/usr/bin/env python3
"""
Quick test for embedding API functionality
快速测试embedding API功能

This script demonstrates basic embedding API testing capabilities.
这个脚本演示基本的embedding API测试功能。
"""

import sys
import time

def test_basic_functionality():
    """Test basic script functionality"""
    print("🧪 Testing basic functionality / 测试基本功能")
    print("="*50)
    
    # Test import capabilities
    try:
        import requests
        print("✅ requests module available / requests模块可用")
    except ImportError:
        print("❌ requests module not available / requests模块不可用")
        return False
    
    try:
        import json
        print("✅ json module available / json模块可用")
    except ImportError:
        print("❌ json module not available / json模块不可用")
        return False
    
    return True

def test_embedding_simulation():
    """Simulate embedding generation"""
    print("\n🔢 Simulating embedding generation / 模拟embedding生成")
    print("="*50)
    
    test_text = "这是一个测试文本 / This is a test text"
    print(f"📝 Input text / 输入文本: {test_text}")
    
    # Simulate embedding (simple hash-based approach for demo)
    import hashlib
    
    start_time = time.time()
    
    # Create a simple "embedding" based on text hash
    text_hash = hashlib.md5(test_text.encode()).hexdigest()
    
    # Convert hex to numbers and normalize to [-1, 1] range
    embedding = []
    for i in range(0, min(32, len(text_hash)), 2):
        hex_val = text_hash[i:i+2]
        num_val = int(hex_val, 16) / 128.0 - 1.0  # Normalize to [-1, 1]
        embedding.append(round(num_val, 4))
    
    end_time = time.time()
    
    print(f"📊 Simulated embedding dimensions / 模拟embedding维度: {len(embedding)}")
    print(f"⏱️  Processing time / 处理时间: {end_time - start_time:.3f}s")
    print(f"🔢 Sample values / 样本值: {embedding[:5]}")
    
    return True

def test_api_structure():
    """Test API request structure"""
    print("\n🌐 Testing API request structure / 测试API请求结构")
    print("="*50)
    
    # Mock API request data
    api_request = {
        "input": "Hello, world!",
        "model": "test-model",
        "encoding_format": "float"
    }
    
    print("📤 Sample API request / API请求样本:")
    import json
    print(json.dumps(api_request, indent=2, ensure_ascii=False))
    
    # Mock API response
    api_response = {
        "data": [
            {
                "embedding": [0.1234, -0.5678, 0.9012, -0.3456, 0.7890],
                "index": 0
            }
        ],
        "model": "test-model",
        "usage": {
            "total_tokens": 3
        }
    }
    
    print("\n📥 Sample API response / API响应样本:")
    print(json.dumps(api_response, indent=2, ensure_ascii=False))
    
    return True

def main():
    print("🚀 Embedding API Quick Test / Embedding API 快速测试")
    print("="*60)
    
    # Run tests
    tests = [
        ("Basic Functionality", test_basic_functionality),
        ("Embedding Simulation", test_embedding_simulation),
        ("API Structure", test_api_structure)
    ]
    
    all_passed = True
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            if not result:
                all_passed = False
        except Exception as e:
            print(f"❌ Test '{test_name}' failed: {e}")
            all_passed = False
    
    print("\n" + "="*60)
    if all_passed:
        print("✅ All tests passed! / 所有测试通过！")
        print("\n🎯 Next steps / 下一步:")
        print("1. Test real APIs with: python3 test_embedding_api.py")
        print("2. Install sentence-transformers for local testing")
        print("3. Get API keys for OpenAI or Hugging Face")
    else:
        print("❌ Some tests failed / 一些测试失败")
        sys.exit(1)

if __name__ == "__main__":
    main()