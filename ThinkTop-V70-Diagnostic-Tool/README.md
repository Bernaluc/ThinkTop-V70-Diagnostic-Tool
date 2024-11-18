
---

<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ThinkTop V70 Diagnostic Tool</h3>

  <p align="center">
    A Raspberry Pi-based tool for monitoring and diagnosing ThinkTop V70 valves at Lone Star Dairy Products.
    <br />
    <a href="https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool">View Demo</a>
    ·
    <a href="https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool/issues">Report Bug</a>
    ·
    <a href="https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool/issues">Request Feature</a>
  </p>
</div>

---

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#problem-statement">Problem Statement</a></li>
    <li><a href="#solution">Solution</a></li>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

[![Product Screenshot][product-screenshot]](https://example.com)

The ThinkTop V70 Diagnostic Tool is a diagnostic solution developed for Lone Star Dairy Products, leveraging a Raspberry Pi to monitor and troubleshoot ThinkTop V70 valves. The tool combines real-time signal monitoring, signal injection, error diagnostics, and visualizations to streamline valve maintenance and reduce downtime.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Problem Statement

Troubleshooting a V70 can be a time-consuming process. Issues may involve hidden faults, like broken cables, or mechanical problems within the valves that disrupt signals. Diagnosing these issues is challenging, even for technicians with electrical experience. Currently, technicians must rely on the control room to actuate valves via radio communication, adding delays and complicating the troubleshooting process. This extended downtime can result in thousands of dollars in lost productivity. A reliable tool is needed to quickly diagnose and resolve issues with these valves and tops, minimizing downtime and streamlining maintenance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Solution

The ThinkTop V70 Diagnostic Tool provides a unified interface for monitoring and interacting with valve systems. Mounted in an IP-rated enclosure with a display and accessible web interface, it offers maintenance personnel both direct and remote access to valve data. This approach enables faster diagnostics, greater control, and significant reductions in maintenance time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Key Features

- **Real-Time Signal Monitoring**: View and track real-time data from ThinkTop V70 valves via a Raspberry Pi display.
- **Signal Injection for Testing**: Simulate signals to control and test the valve functionality.
- **Error Code Interpretation**: Quickly diagnose issues with built-in error code descriptions.
- **Signal Trend Visualization**: Graph signal trends over time for advanced diagnostics.
- **Web-Based Control Interface**: Access a secure web application to control and monitor the valve remotely, with required user authentication.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

Here’s an expanded **Roadmap** with more detailed tasks, covering setup, features, testing, and possible future improvements:

---
### Hardware Setup
- [ ] Assemble and mount all hardware components in the enclosure, including Raspberry Pi, display, optocouplers, and power converters
- [ ] Install and configure buck converters for power supply from battery bank
- [ ] Add cooling solutions (e.g., fans or heatsinks) to prevent overheating
- [ ] Wire and test optocouplers for safe signal interfacing between PLC and Raspberry Pi
- [ ] Verify all electrical connections to ensure signal integrity and isolation

### Core Software Development
- [ ] Develop and test real-time signal monitoring on Raspberry Pi display using Python and Tkinter
- [ ] Implement basic GUI layout for displaying valve status, error codes, and diagnostics
- [ ] Build a secure web interface with Flask for remote monitoring and control access
- [ ] Set up user authentication for the web application to restrict control access
- [ ] Integrate signal injection features for testing valve response from both the display and web interface

### Data Visualization and Diagnostics
- [ ] Add signal trend visualization for identifying patterns and recurring issues over time
- [ ] Implement graphical representations for real-time and historical data on the display and web interface
- [ ] Integrate error code interpretation with explanations to assist technicians in diagnostics
- [ ] Include live valve status indicators for quick visual feedback on operational state

### Automation and Startup
- [ ] Configure automatic startup for display and web applications upon Raspberry Pi boot
- [ ] Set up Raspberry Pi firewall (ufw) to allow only necessary network traffic (e.g., HTTPS, SSH)
- [ ] Enable HTTPS for the web application to secure data transmission on the plant network
- [ ] Test and refine auto-restart of services in case of system reboot or unexpected shutdowns

### Testing and Validation
- [ ] Conduct integration tests to verify seamless communication between the Raspberry Pi, PLC, and ThinkTop V70 valves
- [ ] Perform load testing to ensure the Raspberry Pi can handle simultaneous display and web application processes
- [ ] Gather feedback from maintenance technicians to improve the interface and add any requested features
- [ ] Conduct environmental tests to validate the enclosure’s durability under operating conditions

### Documentation and Training
- [ ] Document hardware setup, wiring diagrams, and configurations for easy replication and troubleshooting
- [ ] Create a user manual for maintenance technicians with instructions for operating the tool and accessing the web interface
- [ ] Develop training materials or guides to familiarize technicians with the tool’s functions and diagnostics
- [ ] Maintain a change log to track software updates and hardware adjustments

### Future Enhancements
- [ ] Implement data logging for historical analysis and trend identification
- [ ] Add notification system for error alerts, with options for SMS or email notifications
- [ ] Consider adding two-factor authentication for enhanced web application security
- [ ] Explore predictive maintenance features using historical data to forecast potential issues
- [ ] Investigate options for wireless communication to reduce reliance on physical wiring

---


See the [open issues](https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Carlos Bernal Urbina - [LinkedIn Profile](https://www.linkedin.com/in/cbernal575/) - cebu312@gmail.com

Project Link: [https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool](https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Raspberry Pi Foundation](https://www.raspberrypi.org/)
* [ThinkTop V50 and V70 Instruction Manual](https://rodem.com/wp-content/uploads/2021/05/thinktop-v50-and-v70-instruction-manual.pdf?srsltid=AfmBOooy-1xZOPXNoaUYIu_YTRTpgN_nwMu86VYCJUq8wSJOtL4KkJWK)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Bernaluc/ThinkTop-V70-Diagnostic-Tool.svg?style=for-the-badge
[contributors-url]: https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Bernaluc/ThinkTop-V70-Diagnostic-Tool.svg?style=for-the-badge
[forks-url]: https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool/network/members
[stars-shield]: https://img.shields.io/github/stars/Bernaluc/ThinkTop-V70-Diagnostic-Tool.svg?style=for-the-badge
[stars-url]: https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool/stargazers
[issues-shield]: https://img.shields.io/github/issues/Bernaluc/ThinkTop-V70-Diagnostic-Tool.svg?style=for-the-badge
[issues-url]: https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool/issues
[license-shield]: https://img.shields.io/github/license/Bernaluc/ThinkTop-V70-Diagnostic-Tool.svg?style=for-the-badge
[license-url]: https://github.com/Bernaluc/ThinkTop-V70-Diagnostic-Tool/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/cbernal575/
[product-screenshot]: images/screenshot.png
