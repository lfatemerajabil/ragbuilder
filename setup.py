from setuptools import setup, find_packages
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='ragbuilder',
    version='0.0.3',
    author='Ashwin Aravind, Aravind Parameswaran',
    author_email='ashwin@krux.ai, aravind@krux.ai',
    description='RagBuilder is a toolkit designed to help you create optimal Production-ready Retrieval-Augmented Generation (RAG) pipeline for your data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kruxai/ragbuilder',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    python_requires='>=3.7',
    package_data={
        'ragbuilder': ['templates/*','static/*', 'eval.db'],
    },
    entry_points={
        'console_scripts': [
            'ragbuilder=ragbuilder.ragbuilder:main',
        ],
    },
    install_requires=[
        'fastapi',
        'pytest==7.2.1',
        'pytest-xdist~=3.2.0',
        'coverage~=7.1.0',
        'black~=23.1.0',
        'pytest-timeout~=2.1.0',
        'pytest-env~= 0.8.1',
        'python-dotenv',
        'langchain',
        'langchain-community',
        'langchainhub',
        'langchain-openai',
        'langchain-chroma',
        'bs4',
        'langchain-core',
        'unstructured',
        'pdf2image',
        'pdfminer.six',
        'langchain_experimental',
        'scikit-learn',
        'ragas==0.1.7',
        'inquirer',
        'llama_index',
        'chromadb',
        'sentence-transformers',
        'llama-index',
        'llama-index-vector-stores-chroma',
        'llama-index-readers-web',
        'IPython',
        'llama-index-retrievers-bm25',
        'rake_nltk',
        'llama-index-embeddings-langchain',
        'llama-index-vector-stores-faiss',
        'faiss-cpu',
        'llama-index-llms-mistralai',
        'llama-index-embeddings-mistralai',
        'llama-index-embeddings-openai',
        'llama-index-postprocessor-longllmlingua',
        'llmlingua',
        'llama_index-postprocessor-cohere_rerank',
        'llama_index-postprocessor-jinaai_rerank',
        'llama-index-postprocessor-rankgpt-rerank',
        'llama-index-postprocessor-colbert-rerank',
        'llama-index-postprocessor-rankllm-rerank',
        'llama-index-llms-openai',
        'langchain-huggingface',
        'rank_bm25',
        'ragas',
        'pandas',
        # 'pillow_heif',
        # 'opencv-python',
        # 'onnx==1.16.0',
        # # 'pikepdf==8.0.0',
        # # 'unstructured-inference',
        # 'pytesseract',
        # 'unstructured',
        # # 'unstructured[all-docs]',
        'mixpanel',
        'langchain_mistralai',
        'langchain_community',
        'huggingface_hub',
        'datasets',
        'langchain_text_splitters',
        'llama-index-core',
        'requests',
        'markdown',
        'singlestoredb',
        'langchain_pinecone',
        'scikit-optimize'
        'pydantic',
        'uvicorn',
        'pinecone-client',
        'setuptools'
        # other dependencies
    ],
)
