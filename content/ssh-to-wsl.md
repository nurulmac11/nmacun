+++
title = "Connecting to Arch WSL 2 Using OpenSSH"
date = 2023-05-03

[taxonomies]
tags = ["google app engine", "google cloud platform", "cloudflare", "ssl", "subdomain"]
+++

Allow port on windows firewall
 netsh advfirewall firewall add rule name="WSL SSH" dir=in action=allow protocol=TCP localport=8089