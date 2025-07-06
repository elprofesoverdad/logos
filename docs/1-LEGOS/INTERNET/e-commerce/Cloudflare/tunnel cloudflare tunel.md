Para exponer tu servidor LAMP con PrestaShop en Kubuntu bajo doble NAT usando Cloudflare Tunnel, sigue este proceso técnico:

## 1. Configuración de Cloudflare Tunnel
**Requisitos previos:**
- Tener instalado `cloudflared` en Kubuntu ([descarga oficial](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/local-management/create-local-tunnel/))
- Dominio gestionado en Cloudflare

**Pasos:**
```bash
# Instalar cloudflared (ejemplo para Debian/Ubuntu)
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# Autenticación
cloudflared tunnel login
```

## 2. Creación del túnel para PrestaShop
```bash
# Crear túnel con nombre
cloudflared tunnel create prestashop-tunnel

# Generar archivo de configuración en ~/.cloudflared/config.yml
tunnel:
credentials-file: /home/usuario/.cloudflared/.json

ingress:
  - hostname: tienda.tudominio.com
    service: http://localhost:80
  - service: http_status:404
```

## 3. Integración DNS sin afectar Cloudflare Pages
```bash
# Enlazar subdominio al túnel (mantén Pages en el dominio raíz)
cloudflared tunnel route dns prestashop-tunnel tienda.tudominio.com
```

## 4. Optimización de Apache para entorno tunnelizado
Editar `/etc/apache2/sites-available/prestashop.conf`:
```apache

    ServerName localhost
    DocumentRoot /var/www/html/prestashop


        AllowOverride All
        Require all granted


```
Reiniciar Apache:
```bash
sudo systemctl restart apache2
```

## 5. Iniciar túnel persistentemente
```bash
# Ejecutar como servicio
sudo cloudflared service install
sudo systemctl start cloudflared
```

## Consideraciones de red en doble NAT:
1. **Firewall local:** Asegurar que Kubuntu permite tráfico local en puerto 80
   ```bash
   sudo ufw allow 80/tcp
   ```
2. **Coexistencia con Cloudflare Pages:**
   - Usar subdominios diferentes (ej: `tudominio.com` para Pages, `tienda.tudominio.com` para el túnel)
   - No es necesario eliminar Pages, funcionan como servicios independientes

## Verificación y monitoreo:
```bash
# Estado del túnel
cloudflared tunnel list

# Logs en tiempo real
journalctl -u cloudflared -f
```

Para ambientes productivos, considera activar **Cloudflare Access** en la configuración del túnel para seguridad adicional. La conexión tunnelizada mantiene cifrado TLS end-to-end sin exponer tu IP real, ideal para doble NAT[1][5].

Esta configuración mantiene tu actual implementación de Pages intacta mientras exponés PrestaShop de forma segura a través del subdominio designado. El tráfico se enruta mediante conexiones outbound del túnel, evitando problemas de NAT y CGNAT[3][4].

Citations:
[1] https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/local-management/create-local-tunnel/
[2] https://developers.cloudflare.com/pages/how-to/preview-with-cloudflare-tunnel/
[3] https://www.reddit.com/r/selfhosted/comments/mdjte7/server_behind_double_nat/
[4] https://serverfault.com/questions/738979/how-to-get-around-double-nat-from-the-isp
[5] https://www.reddit.com/r/selfhosted/comments/16yp5bc/which_is_better_hosting_apache_server_directly_or/
[6] https://docs.cloud.prestashop.com/3-preparing-your-environment/
[7] https://www.howtoforge.com/how-to-install-prestashop-with-apache-and-lets-encrypt-ssl-on-debian-11/
[8] https://www.reddit.com/r/dns/comments/knqi64/cloudflare_solved_my_double_nat_why/
[9] https://fullmetalbrackets.com/blog/setup-cloudflare-tunnel-to-access-self-hosted-apps/
[10] https://community.cloudflare.com/t/solved-tunneling-to-apache-container-with-subdomain-sites/372765
[11] https://www.answeroverflow.com/m/1270753079972593674
[12] https://www.crosstalksolutions.com/cloudflare-tunnel-easy-setup/
[13] https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/create-remote-tunnel/
[14] https://www.youtube.com/watch?v=gpWo94XXrhU
[15] https://www.youtube.com/watch?v=ZvIdFs3M5ic
[16] https://www.reddit.com/r/HomeServer/comments/1crztio/how_to_properly_set_up_cloudflare_tunnel/
[17] https://fullmetalbrackets.com/blog/self-host-website-cloudflare-tunnel/
[18] https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/
[19] https://github.com/cloudflare/cloudflared
[20] https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/local-management/configuration-file/
[21] https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/
[22] https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/configure-tunnels/cloudflared-parameters/run-parameters/
[23] https://forum.netgate.com/topic/114754/avoiding-double-nat-when-using-a-locked-down-isp-modem-router
[24] https://forums.unraid.net/topic/130279-dealing-with-double-nat/
[25] https://askubuntu.com/questions/970742/how-to-access-ubuntu-server-behind-double-nat
[26] https://community.cloudflare.com/t/is-possible-run-webserver-behind-nat-with-some-cloudflare-service/615497
[27] https://www.snbforums.com/threads/double-nat-and-samba.24221/
[28] https://arstechnica.com/civis/threads/double-nat-solved.1490045/
[29] https://www.snbforums.com/threads/double-nat.34065/
[30] https://forums.servethehome.com/index.php?threads%2Fsimple-tunnel-for-incoming-connections-on-dual-nated-network.41945%2F
[31] https://stackoverflow.com/questions/64527748/how-to-access-webserver-running-in-double-nat-network-from-external-network
[32] https://forum.dd-wrt.com/phpBB2/viewtopic.php?t=321712&sid=781b93f2f368cedd08b83a71fb2d7206
[33] https://forums.linuxmint.com/viewtopic.php?t=265773
[34] https://superuser.com/questions/521015/how-is-double-nat-bad-practically
[35] https://devdocs.prestashop-project.org/8/basics/installation/advanced/httpd/
[36] https://community.cloudflare.com/t/apache-virtual-hosts-and-cloudflared/339164
[37] https://servebolt.com/help/cloudflare/how-to-set-up-argo-tunnels-for-remote-access-to-local-development-sites/
[38] https://tecnolitas.com/blog/como-instalar-prestashop-en-ubuntu-20-04/
[39] https://community.cloudflare.com/t/cloudflare-settings-for-prestashop/82284
[40] https://www.youtube.com/watch?v=PjQsxRCm6qs
[41] https://cloudkul.com/blog/how-to-setup-cloudflare-tunnel-in-magento-2/
[42] https://www.prestashop.com/forums/topic/208704-solvedmoving-prestashop-from-local-server-to-live-server-detailed-instructions/
[43] https://help.nextcloud.com/t/cloudflare-tunnel-not-connecting-to-apache-server/216493
[44] https://www.cloudpanel.io/docs/v1/guides/cloudflare/setup
[45] https://developers.cloudflare.com/learning-paths/zero-trust-web-access/connect-private-applications/best-practices/
[46] https://community.tp-link.com/en/business/forum/topic/628356
[47] https://www.reddit.com/r/unRAID/comments/1ak173v/cloudflare_tunnel_setup_questions/
[48] https://community.cloudflare.com/t/server-behind-nat-cant-be-access-whith-cloudflare-proxy-protected/291647
[49] https://www.reddit.com/r/selfhosted/comments/133rr6n/about_cloudflare_tunnels/
[50] https://stackoverflow.com/questions/68705189/how-to-delete-a-cloudflare-page-that-builds-from-my-github-repo
[51] https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/
[52] https://forum.yunohost.org/t/best-practices-for-cloudflare-warp-tunnel/23474
[53] https://superuser.com/questions/943361/how-can-i-get-rid-of-the-double-nat-in-this-network
[54] https://cycle.io/blog/2025/02/securing-private-network-access-with-cloudflare-tunnel/
[55] https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/create-remote-tunnel-api/
[56] https://developers.cloudflare.com/learning-paths/zero-trust-web-access/connect-private-applications/create-tunnel/
[57] https://www.sysbee.net/blog/configuring-cloudflare-tunnel/
[58] https://serverfault.com/questions/65206/fowarding-http-to-lamp-server-through-router-nat
[59] https://www.linuxquestions.org/questions/linux-networking-3/double-nat'ing-4175502727/
[60] https://forum.qnap.com/viewtopic.php?t=164014
[61] https://forum.qnap.com/viewtopic.php?t=154194
[62] https://forums.tomshardware.com/threads/how-to-fix-double-nat-without-access-to-main-router.2706010/
[63] https://community.cloudflare.com/t/best-way-to-configure-apache-server-for-access/388561
[64] https://geekrewind.com/how-to-install-prestashop-with-apache-on-ubuntu-24-04/
[65] https://help-center.prestashop.com/hc/en-us/articles/16417637123602-Configure-Cloudflare-on-PS-Hosting
[66] https://community.cloudflare.com/t/need-help-to-insert-cloudfare-dns-in-my-modem-router/19024

---
Respuesta de Perplexity: pplx.ai/share
