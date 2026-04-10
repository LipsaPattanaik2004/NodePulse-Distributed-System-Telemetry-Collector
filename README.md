# NodePulse – Distributed System Telemetry Collector

## Overview
NodePulse is a simple distributed system that simulates how multiple nodes send system-level metrics such as CPU and memory usage to a central service. The controller processes incoming data and detects abnormal conditions based on predefined thresholds.

This project demonstrates basic concepts of distributed systems, backend communication, and containerized deployment.

---

## Features
- Collects real-time CPU and memory usage from multiple nodes
- Sends telemetry data to a central controller using HTTP
- Processes data to detect high resource usage
- Stores and exposes processed data through APIs
- Containerized using Docker for easy setup and scalability

---

## Architecture

The system consists of two main components:

### Agent
Runs on each node and collects system metrics using psutil. Sends data periodically to the controller.

### Controller
Receives incoming data, processes it, and stores it. Provides API endpoints to retrieve collected data.

### Data Flow
Agent → Controller → Processing → Storage → API Response

---

## Technologies Used
- Python
- Flask
- Docker
- psutil
- REST APIs

---

## Setup Instructions

### Prerequisites
- Docker installed on your system
- Docker Compose installed

### Steps to Run

1. Clone the repository
git clone <your-repo-link>
cd nodepulse
2. Build and run services
docker-compose up --build
3. Access the API
http://localhost:5000/data

# LIPSA PATTANAIK | ITER SOA UNIVERSITY
