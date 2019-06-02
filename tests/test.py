from VideoToSMI-Server import Server, ServerConfig

config = ServerConfig()
config.MODEL_NAME = "mscoco"
config.IP = "127.0.0.1"
config.PORT=802
config.MODEL_CONFIG_PATH = "D:/test/config.json"
config.MODEL_ENGINE = "maskrcnn"
config.FILTER = ['truck','car','bus']
config.VIDEO_FOLDER = "D:/test/videotosmi/"
server = Server(config)
server.Run()