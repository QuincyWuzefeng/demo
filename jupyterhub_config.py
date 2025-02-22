c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.container_image = 'jupyter/base-notebook'  # 使用官方 Jupyter Notebook 镜像
c.DockerSpawner.remove_containers = True  # 使用完自动删除容器
c.DockerSpawner.use_internal_ip = True  # 使用内部 IP 进行连接
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'  # 使用 Dummy Authenticator（测试用）