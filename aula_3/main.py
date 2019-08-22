services:



def ler_servicos_do_yml():
	return services

import docker

client = docker.DockerClient()

services = ler_servicos_do_yml()

for key, value in services.items():
	client.containers.run()