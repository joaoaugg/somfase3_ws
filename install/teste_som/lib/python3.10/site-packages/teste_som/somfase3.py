#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import os
import subprocess

class SoundNode(Node):
    def __init__(self):
        super().__init__("sound_subscriber")
        
        # Inscrever no tópico
        self.subscriber_ = self.create_subscription(
            Bool, "topic_boolean", self.listener_callback, 10
        )
        self.get_logger().info("Subscriber de som inicializado. Aguardando mensagens...")

        # Caminho dos sons na Jetson
        self.path_valor_acima = "/home/somfase3_ws/src/fase3_pkg/fase3_pkg/som_dentro_do_padrao.mp3"
        self.path_valor_abaixo = "/home/somfase3_ws/src/fase3_pkg/fase3_pkg/som_fora_do_padrao.mp3"
        self.current_process = None
    
    def listener_callback(self, msg):
        self.get_logger().info(f"Recebi: {msg.data}")
        
        # Finaliza som anterior se estiver tocando
        if self.current_process is not None:
            self.current_process.terminate()
            self.current_process = None
        
        # Decide qual som tocar
        if msg.data:
            if os.path.exists(self.path_valor_acima):
                self.get_logger().info("Tocando som_dentro_do_padrao.mp3")
                self.current_process = subprocess.Popen(
                    ["mpg123", self.path_valor_acima],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            else:
                self.get_logger().error(f"Arquivo não encontrado: {self.path_valor_acima}")
        else:
            if os.path.exists(self.path_valor_abaixo):
                self.get_logger().info("Tocando som_fora_do_padrao.mp3")
                self.current_process = subprocess.Popen(
                    ["mpg123", self.path_valor_abaixo],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            else:
                self.get_logger().error(f"Arquivo não encontrado: {self.path_valor_abaixo}")

def main(args=None):
    rclpy.init(args=args)
    node = SoundNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
