# VideoToSMI-Server
Create a smi file in Web based on the video
- Copyright (c) 2019 [InfoLab](http://infolab.kunsan.ac.kr) ([Donggun LEE](http://duration.digimoon.net))
- How to install
    ```bash
    pip install VideoToSMI-Server # This method will soon be supported.
    ```
    - other version
        ```bash
        # 0.0.1
        pip install VideoToSMI-Server==0.0.1 # This method will soon be supported.
        ```
- How to use
    ```python
    from videotosmi-server import Server
    server = Server()
    
    # Setting Config
    config = server.getConfig()
    config.IP = "127.0.0.1"
    config.PORT = 80
    config.MODEL_NAME = "mscoco"
    config.MODEL_CONFIG_PATH = "./config.json" # Goto https://github.com/Sotaneum/DeepGeo
    config.MODEL_ENGINE = "maskrcnn"
    config.FILTER = ['car','truck','bus']

    # Server RUN
    server.RUN()

    # POST VIDEO FILE -> http://127.0.0.1:80/ -> Reulst SMI FILE
    ```