class Settings:
    """全局配置管理"""

    def __init__(self):
        """初始化全局配置项"""
        self.host = '0.0.0.0'
        self.port = 8000
        self.exception_msg = '不好意思，刚大脑短路了，请再说一遍。'
        self.prompt_default = '你好。'
