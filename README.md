# RPLidar
Instructions for connection of RPLidar A2M12 for ROS2 Humble.

## Requirements
```bash
git clone https://github.com/SzymKwiatkowski/rplidar_ros
```
And then build project from source.


After that connect lidar and run:
```bash
sudo chmod 666 </dev/ttyUSB*> # USB of lidar
```


Frame Orientation
=====================================================================
<img src="rplidar_A2.png" alt="" height="600"/>


# Bag file
Test bag gile is saved in repository with name lidar_bag