# Reorientation-of-smartphone

---

The utilization of accelerometer data plays a crucial role in Intelligent Transportation Systems (ITS) applications as it facilitates the detection of traffic-related incidents. By analyzing accelerometer readings, it becomes possible to ascertain various aspects such as the vehicle's direction, orientation, harsh brake, crashes, or encounters with road irregularities. However, the processing of acceleration data can be challenging, particularly in uncontrolled application scenarios, such as when collecting data in the background using a mobile phone while the user engages in everyday activities. In controlled scenarios, the smartphone's axes align with the vehicle's movement. Nevertheless, this alignment is not always applicable during regular smartphone usage, causing a mismatch between the axes and the frames of reference that accurately represent the user's experiences. In such cases, it becomes necessary to perform a series of rotations on the accelerometer's Cartesian axes to align them with a specific frame of reference. For example, if the smartphone is placed horizontally within a vehicle, and the goal is to capture events related to road irregularities from the shock absorbers, a reorientation of the accelerometer samples can be applied. This reorientation ensures that the readings are correctly displayed along the Z-axis instead of the X-axis. Overall, the processing and reorientation of accelerometer data are essential for ITS applications, enabling the identification and analysis of various traffic events while considering the specific frame of reference in a given scenario.

Detecting the orientation of smartphones poses a challenge in various domains, particularly when employing crowd-sensing or unsupervised experiments. The methods and strategies presented in existing literature exhibit variations based on the specific requirements and objectives of the experiment. Certain scenarios demand precise and absolute orientation information, while in other cases, identifying an orientation category is deemed satisfactory. Moreover, some approaches focus on orienting the smartphone in a specific situation and subsequently deducing different situations based on changes in orientation.

# Algorithm 

1. **Azimuth**: This represents the rotation angle around the -z axis. Imagine it as the angle between the device's top (y-axis) and the magnetic north pole. When you face north, this angle is 0; when you face south, it's π (pi). Similarly, when facing east, it's π/2, and when facing west, it's -π/2. The values range from -π to π.

2. **Pitch**: This is the rotation angle around the x-axis. It signifies the angle between a plane parallel to the device's screen and a plane parallel to the ground. If you hold the device with the bottom edge facing you and the screen facing up, tilting the top edge toward the ground creates a positive pitch angle. The values range from -π/2 to π/2.

3. **Roll**: This angle relates to the rotation around the y-axis. It represents the angle between a plane perpendicular to the device's screen and a plane perpendicular to the ground. If you hold the device with the bottom edge facing you and the screen facing up, tilting the left edge toward the ground creates a positive roll angle. The values range from -π to π.

To obtain these orientation angles, the function applies the rotations in the order of azimuth, pitch, and roll to transform an identity matrix into the given rotation matrix. All these angles are expressed in radians.


When working with orientation sensors on a mobile device, it's often necessary to compute two important matrices: the inclination matrix (I) and the rotation matrix (R). These matrices are essential for transforming a vector from the device's coordinate system to the world's coordinate system, which is defined by specific rules:
To compute the inclination matrix (I) and the rotation matrix (R) for transforming a vector from the device's coordinate system to the world's coordinate system, we follow a specific set of rules:

1. **World's Coordinate System Definition:**
   - X-axis: The vector product of Y and Z (tangential to the ground and roughly East).
   - Y-axis: Tangential to the ground and pointing towards the magnetic North Pole.
   - Z-axis: Points towards the sky and is perpendicular to the ground.

2. **By Definition:**
   - [0 0 g] = R * gravity (where g is the magnitude of gravity).
   - [0 m 0] = I * R * geomagnetic (where m is the magnitude of the geomagnetic field).
   - R is an identity matrix when the device aligns with the world's coordinate system.
   - I is a rotation matrix that aligns the geomagnetic vector with gravity (world's coordinate system), involving a rotation around the X-axis.

3. **Matrix Formats:**
   - Matrices are returned in either 3x3 or 4x4 row-major format, depending on the array length.
   - If the array length is 16, the matrix format is suitable for OpenGL ES.
   - If the array length is 9, a more compact format is provided.
   - The inverse of each matrix can be obtained by taking its transpose.

4. **Usage Notes:**
   - These matrices are accurate when the device is not in free fall or near strong magnetic interference.
   - Free fall is defined as when gravity's magnitude is less than 1/10 of its nominal value.

In summary, you can use this function to calculate rotation (R) and inclination (I) matrices to transform vectors from the device's coordinate system to the world's coordinate system. These matrices are crucial for orientation-related applications, such as augmented reality or navigation, but their accuracy may be compromised if the device is in free fall or exposed to strong magnetic fields.
![image](https://github.com/Slmaking/Reorientation-of-smartphone/assets/58626257/c56fec0b-a17d-4af6-b038-91b249a8db19)


