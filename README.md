# RaBit
## A pure Python asynchronous BitTorrent Client
### Features

- [x] HTTP and UDP tracker announces + compact response support (BEP 3, BEP 7, BEP 15, BEP 23)
- [x] Download a multi-file torrent using all strategies (BEP 3, BEP 20)
- [x] Download multiple torrents simultaneously
- [x] Seeding + tracker updating in intervals
- [x] Smart ban 
- [x] Location-based peer filtering
- [x] Canonical peer priority for seeding (BEP 40)
- [x] UPnP port forwarding with randomization
- [x] User interface
- [x] Compatible with Windows / Linux

### Limitations
You won't be able to:

- Use protocol extensions
- Seed in ipv6
- Download / seed without an upnp-enabled router or seed from a double nat
- Download from magnet links
- Contribute to incoming connections during download (only to outgoing)

### Usage
> [!IMPORTANT]
> To mitigate unexpected behavior, use a python version above `3.10`

1. Go to `src` directory with ```cd RaBit/src```
2. Install required libraries with ```pip install -r requirements.txt```
3. Run `main.py`