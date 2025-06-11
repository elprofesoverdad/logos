sudo apt-get install -y openvpn dialog python3-pip python3-setuptools
sudo pip3 install protonvpn-cli

se crea la cuenta en https://account.protonvpn.com/
alli se tiene usuari cintraseña etc

cd /usr/local/lib/python3.10/dist-packages/

  424  python -m protonvpn_cli init
  425  sudo python -m protonvpn_cli init
  426  sudo python -m protonvpn_cli connect US-FREE#178021
  427  sudo python -m protonvpn_cli connect US-FREE
  428  sudo python -m protonvpn_cli connect
  429  sudo python -m protonvpn_cli status
  430  sudo python -m protonvpn_cli disconnect


Inicia sesión en tu cuenta de ProtonVPN con el siguiente comando:
protonvpn-cli login
Conecta a un servidor de ProtonVPN con el siguiente comando:
protonvpn-cli connect
