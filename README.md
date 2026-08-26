# Sistema de Comunicação Sonora

Sistema desenvolvido em ROS 2 para comunicação entre uma Jetson e um computador base, permitindo que a Jetson solicite a reprodução de alertas sonoros no computador por meio de serviços ROS 2.

O computador base é responsável pela reprodução dos arquivos de áudio, enquanto a Jetson realiza as chamadas dos serviços.

> **Atenção:** a Jetson e o computador base devem estar na mesma rede, e o computador base deve utilizar Ubuntu 22.04. Não é recomendado executar o sistema em contêiner devido às permissões necessárias para acesso ao áudio.

## Instalação

O workspace deve ser instalado no **computador base**, e não na Jetson.

Execute a partir da pasta `/home`:

```bash
git clone https://github.com/joaoaugg/somfase3_ws.git
sudo apt update
sudo apt install mpg123
```

Depois, compile o workspace:

```bash
cd ~/somfase3_ws
colcon build
```

Configure o ambiente ROS 2:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "source ~/somfase3_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Configuração

No arquivo `somfase3.py`, é necessário atualizar os caminhos dos arquivos `.mp3` de acordo com o diretório do computador:

```python
self.path_valor_acima = "/home/somfase3_ws/src/fase3_pkg/fase3_pkg/som_dentro_do_padrao.mp3"
self.path_valor_abaixo = "/home/somfase3_ws/src/fase3_pkg/fase3_pkg/som_fora_do_padrao.mp3"
```

## Teste

No computador base, execute:

```bash
cd ~/somfase3_ws/src/teste_som/teste_som/
./ambiente_som.sh
```

Na Jetson e no computador base, configure o mesmo `ROS_DOMAIN_ID`:

```bash
export ROS_DOMAIN_ID=0
```

Para testar os serviços:

```bash
ros2 service call /in_boundary std_srvs/srv/Empty {}
```

ou:

```bash
ros2 service call /out_of_boundary std_srvs/srv/Empty {}
```

Os comandos devem ser executados na Jetson, fazendo com que o computador base reproduza o respectivo arquivo de áudio.

