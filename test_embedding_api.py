#!/usr/bin/env python3
"""
Simple embedding model API test script for Ubuntu
支持多种embedding模型API的简单测试脚本

Usage:
    python test_embedding_api.py --provider openai --text "Hello world"
    python test_embedding_api.py --provider huggingface --model sentence-transformers/all-MiniLM-L6-v2
    python test_embedding_api.py --provider local --url http://localhost:8080/embeddings
"""

import argparse
import json
import time
import sys
import requests
from typing import List, Optional, Dict, Any

class EmbeddingTester:
    def __init__(self, provider: str, **kwargs):
        self.provider = provider.lower()
        self.config = kwargs
        
    def test_openai_api(self, text: str, model: str = "text-embedding-ada-002") -> Dict[str, Any]:
        """Test OpenAI embedding API"""
        try:
            import openai
        except ImportError:
            return {"error": "OpenAI library not installed. Run: pip install openai"}
        
        api_key = self.config.get('api_key') or input("Enter OpenAI API key: ")
        
        try:
            client = openai.OpenAI(api_key=api_key)
            start_time = time.time()
            
            response = client.embeddings.create(
                model=model,
                input=text
            )
            
            end_time = time.time()
            
            embedding = response.data[0].embedding
            
            return {
                "success": True,
                "provider": "OpenAI",
                "model": model,
                "text": text,
                "embedding_length": len(embedding),
                "response_time": f"{end_time - start_time:.3f}s",
                "embedding_sample": embedding[:5],  # First 5 dimensions
                "usage": response.usage.total_tokens if hasattr(response, 'usage') else None
            }
            
        except Exception as e:
            return {"error": f"OpenAI API error: {str(e)}"}
    
    def test_huggingface_api(self, text: str, model: str = "sentence-transformers/all-MiniLM-L6-v2") -> Dict[str, Any]:
        """Test Hugging Face embedding API"""
        api_key = self.config.get('api_key')
        use_local = self.config.get('use_local', False)
        
        if use_local:
            # Test local transformers
            try:
                from sentence_transformers import SentenceTransformer
                
                start_time = time.time()
                model_obj = SentenceTransformer(model)
                embedding = model_obj.encode([text])
                end_time = time.time()
                
                return {
                    "success": True,
                    "provider": "Hugging Face (Local)",
                    "model": model,
                    "text": text,
                    "embedding_length": len(embedding[0]),
                    "response_time": f"{end_time - start_time:.3f}s",
                    "embedding_sample": embedding[0][:5].tolist()
                }
                
            except ImportError:
                return {"error": "sentence-transformers not installed. Run: pip install sentence-transformers"}
            except Exception as e:
                return {"error": f"Local model error: {str(e)}"}
        else:
            # Test Hugging Face API
            if not api_key:
                api_key = input("Enter Hugging Face API key (or press Enter to skip): ")
                if not api_key:
                    return {"error": "API key required for Hugging Face API"}
            
            url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model}"
            headers = {"Authorization": f"Bearer {api_key}"}
            
            try:
                start_time = time.time()
                response = requests.post(url, headers=headers, json={"inputs": text})
                end_time = time.time()
                
                if response.status_code == 200:
                    embedding = response.json()
                    if isinstance(embedding[0], list):
                        embedding = embedding[0]  # Handle nested structure
                    
                    return {
                        "success": True,
                        "provider": "Hugging Face API",
                        "model": model,
                        "text": text,
                        "embedding_length": len(embedding),
                        "response_time": f"{end_time - start_time:.3f}s",
                        "embedding_sample": embedding[:5]
                    }
                else:
                    return {"error": f"API error: {response.status_code} - {response.text}"}
                    
            except Exception as e:
                return {"error": f"Request error: {str(e)}"}
    
    def test_local_api(self, text: str, url: str = "http://localhost:8080/embeddings") -> Dict[str, Any]:
        """Test local embedding API endpoint"""
        try:
            payload = {
                "input": text,
                "model": self.config.get('model', 'default')
            }
            
            start_time = time.time()
            response = requests.post(url, json=payload, timeout=30)
            end_time = time.time()
            
            if response.status_code == 200:
                data = response.json()
                
                # Try different response formats
                embedding = None
                if 'data' in data and len(data['data']) > 0:
                    embedding = data['data'][0].get('embedding')
                elif 'embedding' in data:
                    embedding = data['embedding']
                elif 'embeddings' in data:
                    embedding = data['embeddings'][0] if isinstance(data['embeddings'][0], list) else data['embeddings']
                else:
                    embedding = data
                
                if embedding and isinstance(embedding, list):
                    return {
                        "success": True,
                        "provider": "Local API",
                        "url": url,
                        "text": text,
                        "embedding_length": len(embedding),
                        "response_time": f"{end_time - start_time:.3f}s",
                        "embedding_sample": embedding[:5]
                    }
                else:
                    return {"error": f"Unexpected response format: {data}"}
            else:
                return {"error": f"API error: {response.status_code} - {response.text}"}
                
        except requests.exceptions.ConnectionError:
            return {"error": f"Connection failed. Is the service running at {url}?"}
        except Exception as e:
            return {"error": f"Request error: {str(e)}"}
    
    def test_embedding(self, text: str) -> Dict[str, Any]:
        """Main test method that delegates to specific provider"""
        if self.provider == "openai":
            return self.test_openai_api(text, self.config.get('model', 'text-embedding-ada-002'))
        elif self.provider == "huggingface" or self.provider == "hf":
            return self.test_huggingface_api(text, self.config.get('model', 'sentence-transformers/all-MiniLM-L6-v2'))
        elif self.provider == "local":
            return self.test_local_api(text, self.config.get('url', 'http://localhost:8080/embeddings'))
        else:
            return {"error": f"Unsupported provider: {self.provider}"}

def print_result(result: Dict[str, Any]):
    """Pretty print test results"""
    print("\n" + "="*60)
    print("EMBEDDING API 测试结果 / TEST RESULTS")
    print("="*60)
    
    if "error" in result:
        print(f"❌ 错误 / Error: {result['error']}")
        return
    
    print(f"✅ 测试成功 / Test Successful")
    print(f"📡 提供商 / Provider: {result['provider']}")
    
    if 'model' in result:
        print(f"🤖 模型 / Model: {result['model']}")
    if 'url' in result:
        print(f"🔗 URL: {result['url']}")
    
    print(f"📝 输入文本 / Input Text: {result['text']}")
    print(f"📊 向量维度 / Embedding Dimensions: {result['embedding_length']}")
    print(f"⏱️  响应时间 / Response Time: {result['response_time']}")
    print(f"🔢 向量样本 / Sample Values: {result['embedding_sample']}")
    
    if 'usage' in result and result['usage']:
        print(f"💰 使用量 / Usage: {result['usage']} tokens")

def main():
    parser = argparse.ArgumentParser(description='Test embedding model APIs / 测试embedding模型API')
    parser.add_argument('--provider', choices=['openai', 'huggingface', 'hf', 'local'], 
                       default='huggingface', help='API provider')
    parser.add_argument('--text', default='Hello, world! This is a test.', 
                       help='Text to embed')
    parser.add_argument('--model', help='Model name')
    parser.add_argument('--url', help='API endpoint URL (for local provider)')
    parser.add_argument('--api-key', help='API key')
    parser.add_argument('--local', action='store_true', 
                       help='Use local model (for huggingface provider)')
    
    args = parser.parse_args()
    
    # Configure tester
    config = {}
    if args.model:
        config['model'] = args.model
    if args.url:
        config['url'] = args.url
    if args.api_key:
        config['api_key'] = args.api_key
    if args.local:
        config['use_local'] = True
    
    tester = EmbeddingTester(args.provider, **config)
    
    print(f"🧪 开始测试 / Starting test...")
    print(f"📡 提供商 / Provider: {args.provider}")
    print(f"📝 文本 / Text: {args.text}")
    
    result = tester.test_embedding(args.text)
    print_result(result)
    
    # Exit with error code if test failed
    if "error" in result:
        sys.exit(1)

if __name__ == "__main__":
    main()