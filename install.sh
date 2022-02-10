env_name="linux-env"

python3 -m venv $env_name

# For M1 Mac, use miniforge3, install grpcio and opencv there
# and then copy cv2.so and the grpc folder to the site-packages folder 
# in this environment

# For other machines, uncomment "pip install grpcio" and "pip install opencv-contrib-python"

$env_name/bin/python -m pip install --upgrade pip
$env_name/bin/pip install wheel
$env_name/bin/pip install black
$env_name/bin/pip install ipykernel
# $env_name/bin/pip install grpcio
$env_name/bin/pip install grpcio-tools
$env_name/bin/pip install numpy
# $env_name/bin/pip install opencv-contrib-python