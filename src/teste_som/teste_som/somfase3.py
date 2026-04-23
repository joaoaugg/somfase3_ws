#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
import os
import subprocess

class SoundNode(Node):
    def __init__(self):
        super().__init__("sound_service_node")

        # Criando serviços
        self.srv_in_boundary = self.create_service(
            Empty, "/in_boundary", self.in_boundary_callback
        )

        self.srv_out_boundary = self.create_service(
            Empty, "/out_of_boundary", self.out_of_boundary_callback
        )

        self.get_logger().info("Serviços de som prontos!")

        # Caminhos dos sons
        base_path = os.getcwd()

        self.path_valor_dentro = os.path.join(base_path, "som_dentro_do_padrao.mp3")
        self.path_valor_fora = os.path.join(base_path, "som_fora_do_padrao.mp3")        


        self.current_process = None

    def stop_current_sound(self):
        if self.current_process is not None:
            self.current_process.terminate()
            self.current_process = None

    def play_sound(self, path, descricao):
        if os.path.exists(path):
            self.get_logger().info(f"Tocando {descricao}")
            self.current_process = subprocess.Popen(
                ["mpg123", path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        else:
            self.get_logger().error(f"Arquivo não encontrado: {path}")

    def in_boundary_callback(self, request, response):
        self.get_logger().info("Som dentro do padrão! Ativando emissão de som...")

        self.stop_current_sound()
        self.play_sound(self.path_valor_dentro, "som_dentro_do_padrao.mp3")

        return response

    def out_of_boundary_callback(self, request, response):
        self.get_logger().info("Som fora do padrão! Ativando emissão de som...")

        self.stop_current_sound()
        self.play_sound(self.path_valor_fora, "som_fora_do_padrao.mp3")

        return response

def main(args=None):
    rclpy.init(args=args)
    node = SoundNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
