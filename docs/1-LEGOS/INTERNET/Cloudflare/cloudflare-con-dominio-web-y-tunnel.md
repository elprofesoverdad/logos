# Cloudflare con dominio web y tunnel

descargar cloudflared

https://one.dash.cloudflare.com/43f42d06d6f8ab5ceeb1b2beb545c8f0/settings/downloads

https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/tunnel-useful-terms/#default-cloudflared-directory

Para configurar un túnel en Cloudflare y permitir que su servidor Node.js esté disponible en línea, puede utilizar Cloudflare Tunnel. Cloudflare Tunnel es un servicio gratuito que permite a los usuarios acceder a sus servidores locales de forma segura y remota sin necesidad de abrir puertos en su router. Para comenzar, siga los siguientes pasos:

1. Instale Cloudflare Tunnel en su servidor Xubuntu.  yendo a la pagina https://one.dash.cloudflare.com/ en la paguna hay instrucciones para instalar el cliente de cludflared y para iniciar el servicio, el token es diferente para cada tunel por que se debe ir a la pagina.

```shell
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && 

sudo dpkg -i cloudflared.deb &&

sudo cloudflared service install eyJhIjoiNDNmNDJkMDZkNmY4YWI1Y2VlYjFiMmJlYjU0NWM4ZjAiLCJ0IjoiNDY2MTE2N2EtYTBlYS00ZGY2LTg0YWMtNjRiMzlmYjNjMjNkIiwicyI6Ik56bGtOekpsWTJVdFpqQmtOQzAwTXpJd0xUazROalF0TVRka01ESXlaVFkyTkRGaiJ9
```

2. active el tunel cloudflare.
3. 

![](/home/daniel/tron/1-LEGOS/INTERNET/Cloudflare/tunelcloudflare.png)

se pueden hacer varios tuneles por computadora y colocar subdominios por cada computador con un recurso o app, sin path, y el recurso identificarlo por http y la direccion y puerto de la red.