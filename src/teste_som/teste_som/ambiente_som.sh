#!/bin/bash

# Definir o ROS_DOMAIN_ID
export ROS_DOMAIN_ID=0
echo "ROS_DOMAIN_ID configurado para 0"

# Fazer source do setup do ROS2 Humble
source /home/somfase3_ws/install/setup.bash
echo "Setup ROS2 Humble carregado"

# Rodar o nó som_fase3 do pacote teste_som
ros2 run teste_som som_fase3
