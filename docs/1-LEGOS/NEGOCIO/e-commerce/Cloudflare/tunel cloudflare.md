cloudflared tunnel --config ~/.cloudflared/ssh-config.yml run ssh-tunnel


cloudflared tunnel route dns ssh-tunnel ssh-tunnel.mundomejor.uk


mousepad ~/.cloudflared/ssh-config.yml

cloudflared tunnel create ssh-tunnel
