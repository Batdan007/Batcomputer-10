context_compress = None

local_retriever = None

from .web import web_research
import os
print(os.environ.get('PYTHONPATH'));

hybrid_retriever = None

sql_retriever = None

__all__ = [
    "web_research",
    "sql_retriever",
]