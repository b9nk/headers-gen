# Headers Generator

generates realistic http headers fast

## what it does

makes unique user agents and headers instead of using boring static lists. generates chrome/firefox/safari/edge with random versions and builds that actually make sense.

## how to use

```bash
python headers.py
```

type how many you want, it saves to headers.json

## example

```json
{
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.4829 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language": "en-US,en;q=0.9",
  "Connection": "keep-alive"
}
```

## functions

- `gu()` - user agent
- `gh()` - full headers  
- `fs(count)` - generate batch

works with windows/mac/linux/mobile. generates login headers, api headers, regular headers.

fast because multithreaded.

---

**Coded by @cleanest in Discord** 


discord: https://discord.gg/QgqKpKVG5t
