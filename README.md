🔍 NetProbe

 NetProbe is a Python tool that connects to a target system, speaks its protocol, and identifies the running service by analyzing its response.

Instead of trusting banners, it actively interacts with services and infers their identity from behavior.

 💡 What it does

Given an IP and port, NetProbe:

* establishes a TCP connection
* sends a protocol-specific request (e.g., HTTP)
* receives the raw response
* extracts key indicators (status, server, technology hints)

  Why this approach

Many systems hide or modify banners to avoid detection.

NetProbe avoids this limitation by:

> treating the service as a black box and identifying it through interaction

This reflects how real-world reconnaissance works.


⚙️ Current Capabilities (v0.1)

* HTTP probing using raw sockets
* Manual request crafting (`GET / HTTP/1.1`)
* Basic response parsing
* Extraction of:

  * HTTP status codes
  * Server headers
  * backend hints (e.g., PHP)


🧪 Example Output

/
Port 80 → HTTP
Server → Apache/2.2.8
Backend → PHP/5.2.4
Status → 200 OK
/

 🚀 Usage


python netprobe.py


Example:

python
prob_http("192.168.56.101", 80)

🧰 Tech Stack

* Python
* TCP sockets
* Manual protocol interaction

📍 What I learned

* How raw client–server communication works
* Why protocols require strict formatting (`\r\n`)
* How services can be identified without relying on banners
* How small errors break real network communication


 ⚠️ Disclaimer

Use only in controlled environments or on systems you own.

-----------------------------------------------------------------------------------------------------------------------------------------------

🚧 Roadmap

NetProbe is being developed incrementally to focus on depth over shortcuts.

### v0.1 (current)

* HTTP probing
* Raw socket communication
* Manual response analysis

### v0.2

* FTP and SSH probing
* Multi-port scanning
* Improved parsing

### v0.3

* Service detection logic
* Structured output
* Better error handling

### v1.0 (goal)

* Asynchronous scanning
* Modular architecture
* CLI interface
* Advanced fingerprinting

---

## 🧭 Final Thought

This project started as a simple script, but it reshaped how I understand network interaction:

> Instead of asking a system what it is,
> you can observe how it behaves and figure it out yourself.
