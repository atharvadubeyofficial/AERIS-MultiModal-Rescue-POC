# AERIS
## Autonomous Emergency Response & Intelligence System

AERIS is an AI-assisted drone-based search and rescue system designed for disaster and emergency-response scenarios.

The system uses an incoming UAV video stream and combines AI perception with multi-modal sensor information to identify potential survivors, assess environmental risk, prioritize rescue targets, and assist rescue teams with mission-level decisions.

---

## Problem

During floods, disasters, and urban emergencies:

- Survivors may be difficult to identify from ground level.
- Flood water can reduce visibility.
- Rescue teams may not know which detected person requires immediate attention.
- Obstacles and unsafe regions can make direct rescue approaches difficult.
- Information from different sensors is often available independently rather than as one actionable decision.

AERIS addresses this problem by converting observations from a rescue UAV into a prioritized rescue situation.

---

## Proposed Solution

AERIS follows the pipeline:

UAV Video
↓
AI Perception
↓
Environmental / Flood Assessment
↓
Thermal + Sonar + SOS Evidence
↓
Sensor Fusion
↓
Rescue Priority
↓
Mission Recommendation

---

## Core Capabilities

### 1. UAV Video Processing
Processes a video stream from a UAV, camera, recorded mission footage, or compatible streaming source.

### 2. AI Person Detection
Uses an object-detection model to identify potential survivors/persons in the incoming visual stream.

### 3. Environmental Assessment
Analyzes the visual scene for flood/hazard-related information.

### 4. Multi-Modal Sensor Fusion
Combines information from:

- RGB camera
- Thermal sensing
- Sonar/range sensing
- Flood/hazard assessment
- SOS events

into a unified rescue assessment.

### 5. Rescue Prioritization
Every detected target receives a rescue score and priority such as:

- CRITICAL
- HIGH
- MEDIUM
- LOW

### 6. Mission Recommendation
AERIS recommends which target should receive priority and provides a mission-level action suggestion.

### 7. Mission Visualization
The mission-control interface displays:

- UAV video
- detected targets
- sensor information
- rescue score
- priority
- alerts
- mission map
- recommended action

---

## System Architecture

```text
                    UAV / CAMERA
                         |
                         v
                 VIDEO SOURCE LAYER
                         |
                         v
                  AI PERCEPTION
                         |
             +-----------+-----------+
             |           |           |
             v           v           v
          THERMAL      FLOOD       SONAR
          SENSOR       ANALYSIS    / RANGE
             |           |           |
             +-----------+-----------+
                         |
                         v
                  SENSOR FUSION
                         |
                         v
                 TARGET PRIORITY
                         |
                         v
                  MISSION PLANNER
                         |
                         v
                  MISSION CONTROL
