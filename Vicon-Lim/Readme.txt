Vicon Receiver ROS2 ( 09/10/23 )

-> Prerequisiti: Ubuntu & ROS2 ( Testato funzionante con Ubuntu 22.04 & ROS2 Humble )

1) Installare librerie DataStream SDK:
	"./install_libs.sh"

2) Buildare il progetto:
	"cd vicon_receiver"
	"colcon build --packages-select interfaces"
	"source install/setup.bash"
	"colcon build"

3) Runnare il driver (verificare parametro "hostname"):
	"ros2 launch vicon_receiver client.launch.py"


Per più info: "https://github.com/OPT4SMART/ros2-vicon-receiver"

! Rispetto al loro receiver ho separato la cartella dei messaggi custom dal resto
  altrimenti mi dava errori quando buildavo il progetto. 

