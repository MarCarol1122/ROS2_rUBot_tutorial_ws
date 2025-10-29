import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')

        # Publisher al topic /turtle1/cmd_vel
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Subscriber al topic /turtle1/pose
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)
        self.subscription  # evitar warning

        self.get_logger().info('Nodo move_turtle iniciado ✅')

    def pose_callback(self, msg):
        # Crear mensaje de velocidad
        twist = Twist()

        # Si la tortuga está fuera de los límites (x o y > 7), detenerla
        if msg.x > 7.0 or msg.y > 7.0:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.get_logger().info('🐢 Límite alcanzado: deteniendo tortuga')
        else:
            # Si no, seguir moviéndose hacia delante
            twist.linear.x = 1.0
            twist.angular.z = 0.5

        # Publicar el mensaje
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
