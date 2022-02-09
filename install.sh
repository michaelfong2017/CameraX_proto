env_name="linux-env"

python3 -m venv $env_name

$env_name/bin/python -m pip install --upgrade pip
$env_name/bin/pip install wheel
$env_name/bin/pip install black
$env_name/bin/pip install ipykernel
$env_name/bin/pip install grpcio-tools
$env_name/bin/pip install numpy
$env_name/bin/pip install pillow