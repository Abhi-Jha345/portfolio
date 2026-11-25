"""Generate index.html for the portfolio (EN/DE). Run: python3 tools/build_site.py"""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
E = html.escape


def t(tag, en, de, cls="", attrs=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c}{attrs} data-en="{E(en)}" data-de="{E(de)}">{E(en)}</{tag}>'


def spec(items):
    return '<ul class="spec">' + "".join(f"<li>{E(i)}</li>" for i in items) + "</ul>"


def facts(rows):
    out = '<dl class="facts">'
    for k_en, k_de, v_en, v_de in rows:
        out += f'<div><dt data-en="{E(k_en)}" data-de="{E(k_de)}">{E(k_en)}</dt><dd data-en="{E(v_en)}" data-de="{E(v_de)}">{E(v_en)}</dd></div>'
    return out + "</dl>"


def video(src, poster, label):
    return (f'<figure class="media"><video muted loop playsinline preload="none" poster="{poster}" aria-label="{E(label)}">'
            f'<source src="{src}" type="video/mp4"></video>'
            f'<button class="vtoggle" type="button" aria-label="Play video" data-state="paused"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-play" d="M8 5v14l11-7z"/><path class="i-pause" d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg></button></figure>')


def image(src, alt, cls="media media--img"):
    return f'<figure class="{cls}"><a href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{E(alt)}" loading="lazy"></a></figure>'


def panel(lines):
    """Typographic stand-in for projects without footage: a datasheet block."""
    rows = "".join(f'<div><span>{E(k)}</span><span>{E(v)}</span></div>' for k, v in lines)
    return f'<figure class="media media--sheet"><div class="sheet">{rows}</div></figure>'


def row(id_, title_en, title_de, specs, lead_en, lead_de, media, detail_en, detail_de, fact_rows, links=""):
    return f'''
      <article class="work" id="{id_}">
        <div class="work__text">
          {t("h3", title_en, title_de, "work__title")}
          {spec(specs)}
          {t("p", lead_en, lead_de, "work__lead")}
          <details class="work__more">
            <summary><span data-en="Case details" data-de="Details zum Projekt">Case details</span></summary>
            {t("p", detail_en, detail_de)}
            {facts(fact_rows)}
            {links}
          </details>
        </div>
        {media}
      </article>'''


def mini(title_en, title_de, specs, body_en, body_de, link=""):
    return f'''
        <li class="mini">
          {t("h3", title_en, title_de)}
          {spec(specs)}
          {t("p", body_en, body_de)}
          {link}
        </li>'''


def job(date, role_en, role_de, org, body_en, body_de, tags):
    tg = "".join(f"<li>{E(x)}</li>" for x in tags)
    return f'''
          <li class="job">
            <p class="job__date">{E(date)}</p>
            <div>
              {t("h3", role_en, role_de)}
              <p class="job__org">{E(org)}</p>
              {t("p", body_en, body_de)}
              <ul class="tags">{tg}</ul>
            </div>
          </li>'''


GH = lambda url: f'<a class="textlink" href="{url}" target="_blank" rel="noopener">GitHub ↗</a>'

work = "".join([
    row("thesis",
        "Real-time line detection with transformers", "Echtzeit-Linienerkennung mit Transformern",
        ["Master thesis · grade 1.0", "Jetson AGX Orin", "NanoSAM · GPU-RANSAC · Kalman", "real time"],
        "Line detection for an automated guided vehicle: I compared classical methods, CNNs and transformers, changed the model architecture for the task and made the whole pipeline fast enough to run in real time on the vehicle's embedded computer.",
        "Linienerkennung für ein fahrerloses Transportfahrzeug: Ich habe klassische Verfahren, CNNs und Transformer verglichen, die Modellarchitektur für die Aufgabe angepasst und die gesamte Pipeline schnell genug für Echtzeit auf dem Embedded-Rechner des Fahrzeugs gemacht.",
        video("assets/videos/thesis_line_detection.mp4", "assets/videos/thesis_line_detection.jpg", "Line detection model running on real AGV recordings"),
        "The training data combined CARLA simulation across many maps, weather and lighting scenarios with public lane data and real vehicle images, which I labelled automatically with a segmentation model. Models were trained on an HPC cluster. The video shows the model on real recordings with the live IoU score.",
        "Die Trainingsdaten kombinierten CARLA-Simulation über viele Karten, Wetter- und Lichtszenarien mit öffentlichen Spurdaten und realen Fahrzeugbildern, die ich automatisch mit einem Segmentierungsmodell gelabelt habe. Trainiert wurde auf einem HPC-Cluster. Das Video zeigt das Modell auf realen Aufnahmen mit dem laufenden IoU-Wert.",
        [("Hardware", "Hardware", "NVIDIA Jetson AGX Orin", "NVIDIA Jetson AGX Orin"),
         ("Stack", "Stack", "PyTorch, TensorRT (INT8 encoder, FP16 decoder), CUDA, CARLA", "PyTorch, TensorRT (INT8-Encoder, FP16-Decoder), CUDA, CARLA"),
         ("Result", "Ergebnis", "Inference sped up by roughly an order of magnitude, full pipeline within the camera's frame budget", "Inferenz rund um eine Größenordnung beschleunigt, gesamte Pipeline im Frame-Budget der Kamera"),
         ("Where", "Wo", "PEM, RWTH Aachen, 10/2025 – 05/2026", "PEM, RWTH Aachen, 10/2025 – 05/2026")]),

    row("uav",
        "Fixed-wing UAV autopilot", "Starrflügler-UAV-Autopilot",
        ["Personal project", "C++17", "Simulink 6-DOF", "H∞ + TECS", "JSBSim SIL", "STM32 Cortex-M4F"],
        "A safety-critical autopilot built in a lightweight DO-178C style: requirements, hazard assessment and a code-to-test trace matrix are checked in CI, and the C++ core is verified back-to-back against a Simulink reference.",
        "Ein sicherheitskritischer Autopilot im Stil eines schlanken DO-178C-Prozesses: Anforderungen, Gefährdungsanalyse und eine Trace-Matrix von Code zu Tests werden in der CI geprüft, und der C++-Kern wird Back-to-Back gegen eine Simulink-Referenz verifiziert.",
        image("assets/uav/architecture.svg", "Software architecture of the UAV autopilot: rate groups, HAL, platforms and CI verification", "media media--img media--light"),
        "I designed gain-scheduled structured H-infinity attitude and rate control with anti-windup and a TECS energy controller, and tested them in standard flight-test cycles and a sim-to-real Monte Carlo campaign with airframe uncertainty, servo limits, sensor noise, wind and turbulence. The core runs software-in-the-loop against JSBSim and cross-compiles for an STM32. A ROS 2 companion with Gazebo and OpenVINS for GNSS-denied navigation is in progress. Built with Claude Code sub-agents in parallel worktrees and an MCP server for MATLAB.",
        "Ich habe eine gain-geplante strukturierte H-unendlich-Lage- und Ratenregelung mit Anti-Windup sowie einen TECS-Energieregler entworfen und in Standard-Flugtestzyklen und einer Sim-to-Real-Monte-Carlo-Kampagne mit Zellenunsicherheit, Servogrenzen, Sensorrauschen, Wind und Turbulenz getestet. Der Kern läuft Software-in-the-Loop gegen JSBSim und lässt sich für einen STM32 cross-kompilieren. Ein ROS-2-Companion mit Gazebo und OpenVINS für GNSS-freie Navigation ist in Arbeit. Entwickelt mit Claude-Code-Sub-Agents in parallelen Worktrees und einem MCP-Server für MATLAB.",
        [("Loops", "Regelkreise", "10 / 50 / 200 Hz rate groups on a 5 ms base frame", "Ratengruppen mit 10 / 50 / 200 Hz auf 5-ms-Grundtakt"),
         ("Modes", "Modi", "MANUAL, STABILIZE, ALT_HOLD, WAYPOINT, LOITER, RTL with failsafes", "MANUAL, STABILIZE, ALT_HOLD, WAYPOINT, LOITER, RTL mit Failsafes"),
         ("Verification", "Verifikation", "GoogleTest, back-to-back vs Simulink, trace matrix, clang-tidy, sanitizers", "GoogleTest, Back-to-Back gegen Simulink, Trace-Matrix, clang-tidy, Sanitizer"),
         ("Status", "Status", "Requirement limits still draft; HIL and GNSS-denied fusion in progress", "Anforderungsgrenzen noch Entwurf; HIL und GNSS-freie Fusion in Arbeit")],
        '<p class="more-media"><a class="textlink" href="assets/uav/sim2real_campaign.png" target="_blank" rel="noopener" data-en="Monte Carlo campaign plot ↗" data-de="Plot der Monte-Carlo-Kampagne ↗">Monte Carlo campaign plot ↗</a></p>'),

    row("tracking",
        "Tank detection and tracking on Jetson", "Panzererkennung und Tracking auf Jetson",
        ["Personal project", "YOLO26n · YOLOv8n", "TensorRT FP16", "C++ / CUDA", "~93 FPS tracking"],
        "From raw video to real-time multi-object tracking: training labels generated by a vision-language model from text prompts, YOLO detectors, and a C++ tracker I wrote from scratch for the Jetson AGX Orin.",
        "Vom Rohvideo zum Multi-Object-Tracking in Echtzeit: Trainingslabels von einem Vision-Language-Modell aus Textprompts, YOLO-Detektoren und ein C++-Tracker, den ich für den Jetson AGX Orin neu geschrieben habe.",
        video("assets/mot/tank_tracking_jetson.mp4", "assets/mot/tank_tracking_jetson.jpg", "Two tanks tracked with stable IDs by the Jetson C++ pipeline"),
        "LocateAnything-3B labels each frame from prompts such as \"military tank\", so no box is drawn by hand. The detectors reach about 0.93 mAP@50. The Jetson pipeline uses a CUDA preprocessing kernel, a TensorRT FP16 engine and a Kalman + KLT tracker with Hungarian matching. A modified FastMOT with a PyTorch re-identification model covers the workstation side.",
        "LocateAnything-3B labelt jedes Bild aus Prompts wie \"military tank\", ohne von Hand gezeichnete Boxen. Die Detektoren erreichen rund 0,93 mAP@50. Die Jetson-Pipeline nutzt einen CUDA-Vorverarbeitungskernel, eine TensorRT-FP16-Engine und einen Kalman-+-KLT-Tracker mit Hungarian Matching. Ein angepasstes FastMOT mit PyTorch-Re-Identifikation deckt die Workstation ab.",
        [("Detection", "Detektion", "133 FPS FP16 TensorRT vs 37 FPS PyTorch on Jetson AGX Orin", "133 FPS FP16-TensorRT vs. 37 FPS PyTorch auf Jetson AGX Orin"),
         ("Tracking", "Tracking", "~93 FPS in C++, 2.8× the Python pipeline", "~93 FPS in C++, 2,8× die Python-Pipeline"),
         ("Labels", "Labels", "Open-vocabulary VLM, 8-bit quantized", "Open-Vocabulary-VLM, 8-Bit-quantisiert")],
        f'<p class="more-media">{GH("https://github.com/Abhi-Jha345/MOTwithyolo")} <a class="textlink" href="assets/mot/jetson_benchmark.png" target="_blank" rel="noopener" data-en="Benchmark chart ↗" data-de="Benchmark-Diagramm ↗">Benchmark chart ↗</a></p>'),

    row("vla",
        "Language-conditioned picking with a small VLA", "Sprachgesteuertes Greifen mit einem kleinen VLA",
        ["Learning project", "MuJoCo", "Franka Panda · RB-Y1", "ResNet-18 + CLIP", "flow matching"],
        "A simulated robot picks the item named in an instruction such as \"put the red box in the tote\". The policy reads two cameras, the instruction and the joint state and outputs chunks of actions through a flow-matching head, trained by behaviour cloning.",
        "Ein simulierter Roboter greift das Objekt, das eine Anweisung wie \"put the red box in the tote\" nennt. Die Policy liest zwei Kameras, die Anweisung und den Gelenkzustand und gibt über einen Flow-Matching-Kopf Aktionsabschnitte aus, trainiert per Behaviour Cloning.",
        video("assets/vla/vla_sim_demo.mp4", "assets/vla/vla_sim_demo.jpg", "Scripted expert demonstrations in the warehouse and supermarket scenes"),
        "I built the scenes, a scripted expert and the data pipeline, then trained the model. The video shows the scripted expert that generates the training data, not the learned policy. The policy is not solved yet: diagnostics showed it ignored the product name and missed grasps, and a weight-space edit made the instruction matter measurably without improving outcomes. Working out why is the part I learned most from.",
        "Ich habe die Szenen, einen skriptbasierten Experten und die Datenpipeline gebaut und dann das Modell trainiert. Das Video zeigt den skriptbasierten Experten, der die Trainingsdaten erzeugt, nicht die gelernte Policy. Die Policy ist noch nicht gelöst: Diagnosen zeigten, dass sie den Produktnamen ignorierte und Griffe verfehlte, und eine Gewichtsraum-Änderung machte die Anweisung messbar wirksam, ohne die Ergebnisse zu verbessern. Den Gründen nachzugehen, war für mich der lehrreichste Teil.",
        [("Expert", "Experte", "95/100 episodes (warehouse), 100/100 (supermarket v2)", "95/100 Episoden (Lager), 100/100 (Supermarkt v2)"),
         ("Data", "Daten", "497 successful demonstrations, held-out evaluation seeds", "497 erfolgreiche Demonstrationen, getrennte Evaluations-Seeds"),
         ("Model", "Modell", "Fine-tuned ResNet-18 tokens, frozen CLIP text, 4-layer fusion, flow-matching decoder", "Feinjustierte ResNet-18-Tokens, eingefrorener CLIP-Text, 4-Layer-Fusion, Flow-Matching-Decoder"),
         ("Status", "Status", "Policy success still low; under active work", "Erfolgsrate der Policy noch niedrig; in Arbeit")]),

    row("bus",
        "Autonomous electric bus", "Autonomer Elektrobus",
        ["PEM, RWTH Aachen", "ROS 2", "NVIDIA Jetson", "stereo + LiDAR fusion", "SIL 2 concept"],
        "I brought a prototype bus with years of history back on the road from its wiring diagrams in two months, then integrated localisation, perception and heading control in ROS 2 and tested them on the moving vehicle.",
        "Ich habe einen Prototyp-Bus mit jahrelanger Historie anhand seiner Schaltpläne in zwei Monaten wieder fahrbereit gemacht und danach Lokalisierung, Wahrnehmung und Kursregelung in ROS 2 integriert und auf dem fahrenden Fahrzeug getestet.",
        panel([("vehicle", "autonomous electric bus"), ("compute", "NVIDIA Jetson"), ("middleware", "ROS 2 · Fast DDS"), ("perception", "stereo · LiDAR · odometry"), ("detector", "YOLOv8 · TensorRT"), ("safety", "SICK scanner → safety PLC"), ("tests", "~200 per deployment")]),
        "Stereo camera, LiDAR and odometry are fused for obstacle detection in bad weather, and YOLOv8 runs on the Jetson with TensorRT, trained on data labelled automatically by a vision-language model. I wrote a safety concept targeting SIL 2 in which a safety laser scanner reports via CIP Safety to a safety PLC. A Docker CI/CD pipeline runs about 200 automated tests including ISO 26262 unit tests before each deployment, and Ethernet HIL tests cut latency by more than an order of magnitude after Fast DDS tuning.",
        "Stereokamera, LiDAR und Odometrie werden zur Hinderniserkennung bei schlechtem Wetter fusioniert, und YOLOv8 läuft mit TensorRT auf dem Jetson, trainiert mit von einem Vision-Language-Modell automatisch gelabelten Daten. Ich habe ein Sicherheitskonzept mit Ziel SIL 2 geschrieben, in dem ein Sicherheitslaserscanner über CIP Safety an eine Sicherheits-SPS meldet. Eine Docker-CI/CD-Pipeline führt vor jedem Deployment rund 200 automatisierte Tests inklusive ISO-26262-Unit-Tests aus, und Ethernet-HIL-Tests senkten die Latenz nach dem Fast-DDS-Tuning um mehr als eine Größenordnung.",
        [("Role", "Rolle", "Student research assistant, 01/2024 – 09/2026", "Wissenschaftliche Hilfskraft, 01/2024 – 09/2026"),
         ("Result", "Ergebnis", "On-vehicle debugging from days to hours", "Fehlersuche am Fahrzeug von Tagen auf Stunden"),
         ("Tooling", "Werkzeuge", "Docker, CI/CD, static analysis, agentic workflows with Claude Code and MCP servers", "Docker, CI/CD, statische Analyse, agentische Workflows mit Claude Code und MCP-Servern")]),

    row("hyperloop",
        "Hyperloop powertrain", "Hyperloop-Antriebsstrang",
        ["Tachyon Hyperloop", "team lead · 8 students", "TI C2000", "90 kW axial-flux", "350 V pack"],
        "As team lead for powertrain and control I took the drive from scratch to its first demonstration in 1.5 years. We passed all rulebook tests at the European Hyperloop Week and received an award for a promising electrical subsystem.",
        "Als Teamleiter für Antrieb und Regelung habe ich den Antrieb in 1,5 Jahren von null bis zur ersten Demonstration gebracht. Wir haben alle Regelwerkstests der European Hyperloop Week bestanden und eine Auszeichnung für ein vielversprechendes elektrisches Subsystem erhalten.",
        panel([("team", "8 students"), ("brake ECU", "Simulink · Embedded Coder · TI C2000"), ("motor", "90 kW axial flux · resolver"), ("battery", "350 V · cell monitoring"), ("tools", "XCP · CANape · CAPL"), ("event", "European Hyperloop Week")]),
        "I wrote the brake ECU software in Simulink with Embedded Coder including unit and module tests, commissioned the axial-flux motor on the HV inverter and tuned its speed control via XCP, and integrated a 350 V prototype battery pack with temperature and cell monitoring, emergency shutdown and balancing.",
        "Ich habe die Bremssteuergeräte-Software in Simulink mit Embedded Coder inklusive Unit- und Modultests entwickelt, den Axialflussmotor am HV-Umrichter in Betrieb genommen und seine Drehzahlregelung per XCP abgestimmt sowie ein 350-V-Prototyp-Batteriepaket mit Temperatur- und Zellüberwachung, Notabschaltung und Balancing integriert.",
        [("Period", "Zeitraum", "01/2023 – 09/2024", "01/2023 – 09/2024"),
         ("Qualification", "Qualifikation", "HV qualification, level 3E", "HV-Qualifikation, Stufe 3E")]),
])

minis = "".join([
    mini("Fuel-cell hybrid truck", "Brennstoffzellen-Hybrid-Lkw", ["PEM", "ECU", "CAN J1939", "XCP"],
         "Commissioned a new ECU and cut CAN integration effort by 70% with MATLAB scripts that process about 800 signals. Built a one-pedal drive with recuperation within motor, battery and fuel-cell limits.",
         "Neues Steuergerät in Betrieb genommen und den CAN-Integrationsaufwand mit MATLAB-Skripten für rund 800 Signale um 70 % gesenkt. One-Pedal-Drive mit Rekuperation innerhalb der Grenzen von Motoren, Batterie und Brennstoffzelle entwickelt."),
    mini("Lateral control under delay", "Querregelung unter Totzeit", ["PEM", "Stanley", "LTV-MPC"],
         "Closed-loop analysis with realistic noise, dropouts and actuator delay. Found and fixed two delay-compensation bugs and brought tracking error from metres to centimetres.",
         "Closed-Loop-Analyse mit realistischem Rauschen, Aussetzern und Aktortotzeit. Zwei Fehler in der Totzeitkompensation behoben und den Spurfehler von Metern auf Zentimeter gesenkt."),
    mini("Agentic engineering", "Agentische Entwicklung", ["Claude Code", "sub-agents", "MCP"],
         "I use custom skills, sub-agents, hooks and MCP servers to write scripts and tests around vehicle software, including an MCP server for MATLAB that generates models and runs their unit tests.",
         "Ich nutze eigene Skills, Sub-Agents, Hooks und MCP-Server, um Skripte und Tests rund um Fahrzeugsoftware zu erstellen, darunter einen MCP-Server für MATLAB, der Modelle erzeugt und ihre Unit-Tests ausführt."),
    mini("Battery cell test station", "Batteriezellen-Prüfstation", ["Personal project", "TIA Portal V20", "S7-1500", "SCL"],
         "Step chain, PackML-style modes, fault reactions, E-stop and guard-door logic, WinCC Unified HMI and unit tests in CI.",
         "Schrittkette, PackML-Betriebsarten, Fehlerreaktionen, Not-Halt- und Schutztürlogik, WinCC-Unified-HMI und Unit-Tests in CI.",
         GH("https://github.com/Abhi-Jha345/TIA_portal")),
    mini("Drive and bearing test benches", "Antriebs- und Lagerprüfstände", ["ENGIRO", "Elgeti", "CODESYS", "LabVIEW"],
         "PLC control for 48 V and 96 V drive test benches to IEC 61131-3, and a DBC import script that saved up to 90% of manual signal work. Bearing test benches automated in LabVIEW.",
         "PLC-Steuerung für 48-V- und 96-V-Antriebsprüfstände nach IEC 61131-3 und ein DBC-Importskript, das bis zu 90 % der manuellen Signalarbeit einsparte. Lagerprüfstände in LabVIEW automatisiert."),
])

jobs = "".join([
    job("01/2024 – 09/2026", "Student Research Assistant, Autonomous Systems Software", "Wissenschaftliche Hilfskraft, Software für autonome Systeme", "PEM, RWTH Aachen University",
        "Autonomous electric bus and fuel-cell hybrid truck: vehicle bring-up, ROS 2 integration, perception on Jetson, CI/CD and HIL testing, ECU commissioning.",
        "Autonomer Elektrobus und Brennstoffzellen-Hybrid-Lkw: Fahrzeug-Inbetriebnahme, ROS-2-Integration, Wahrnehmung auf Jetson, CI/CD- und HIL-Tests, Steuergeräte-Inbetriebnahme.",
        ["ROS 2", "Jetson", "TensorRT", "Docker", "CAN J1939", "XCP"]),
    job("10/2025 – 05/2026", "Master Thesis, grade 1.0", "Masterarbeit, Note 1,0", "PEM, RWTH Aachen University",
        "Evaluation and optimisation of line detection algorithms, with a transformer-based pipeline running in real time on a Jetson AGX Orin.",
        "Bewertung und Optimierung von Linienerkennungsalgorithmen mit einer transformerbasierten Pipeline in Echtzeit auf einem Jetson AGX Orin.",
        ["PyTorch", "NanoSAM", "TensorRT", "CARLA"]),
    job("01/2023 – 09/2024", "Embedded Software Developer, Team Lead Powertrain & Control", "Embedded-Softwareentwickler, Teamleiter Antrieb & Regelung", "Tachyon Hyperloop e.V.",
        "Led eight students; brake ECU software for TI C2000; HV inverter, motor and battery integration.",
        "Acht Studierende geleitet; Bremssteuergeräte-Software für TI C2000; Integration von HV-Umrichter, Motor und Batterie.",
        ["Simulink", "Embedded Coder", "CAPL", "CANape"]),
    job("08/2023 – 08/2024", "Working Student, Test Bench Software", "Werkstudent, Prüfstandssoftware", "ENGIRO GmbH",
        "PLC control for 48 V and 96 V drive test benches in CODESYS, DBC import automation in Python.",
        "PLC-Steuerung für 48-V- und 96-V-Antriebsprüfstände in CODESYS, DBC-Import-Automatisierung in Python.",
        ["CODESYS", "IEC 61131-3", "Python"]),
    job("07/2022 – 07/2023", "Working Student, Test Bench Automation", "Werkstudent, Prüfstandsautomatisierung", "Elgeti Engineering GmbH",
        "Designed and automated bearing test benches, supervised two interns and supported customers after delivery.",
        "Lagerprüfstände konstruiert und automatisiert, zwei Praktikanten betreut und Kunden nach der Auslieferung unterstützt.",
        ["CODESYS", "LabVIEW"]),
])

toolchain = [
    ("Autonomy", "Autonomie", "ROS 2, Fast DDS, sensor fusion, YOLOv8/YOLO26, transformers, TensorRT, CUDA, CARLA, MuJoCo, MPC"),
    ("Vehicle E/E", "Fahrzeug-E/E", "CAN / J1939, DBC, XCP, CANape, CANoe, CAPL, oscilloscope, HV systems (level 3E)"),
    ("Embedded", "Embedded", "C++, MATLAB/Simulink, Embedded Coder, TI C2000, STM32, ISO 26262 unit tests"),
    ("Automation and test", "Automatisierung und Test", "Docker CI/CD, GitHub Actions, HIL, CODESYS, TIA Portal (personal), LabVIEW, Linux, Python"),
    ("AI-assisted", "KI-gestützt", "Claude Code, sub-agents, hooks, MCP servers"),
]
tools_html = "".join(f'<div><dt data-en="{E(a)}" data-de="{E(b)}">{E(a)}</dt><dd>{E(c)}</dd></div>' for a, b, c in toolchain)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Abhishek Jha · Autonomous Systems Engineer</title>
<meta name="description" content="Abhishek Jha, autonomous systems engineer in Aachen: perception and edge AI on NVIDIA Jetson, vehicle bring-up, UAV autonomy, HIL and CI testing.">
<meta name="theme-color" content="#101214">
<link rel="preload" href="assets/fonts/big-shoulders-display-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/archivo-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="skip" href="#work" data-en="Skip to work" data-de="Zu den Projekten">Skip to work</a>
<header class="bar">
  <a class="bar__name" href="#top">Abhishek Jha</a>
  <nav aria-label="Main">
    <a href="#work" data-en="Work" data-de="Projekte">Work</a>
    <a href="#career" data-en="Career" data-de="Werdegang">Career</a>
    <a href="#contact" data-en="Contact" data-de="Kontakt">Contact</a>
  </nav>
  <div class="lang" role="group" aria-label="Language">
    <button type="button" data-lang="en" aria-pressed="true">EN</button>
    <button type="button" data-lang="de" aria-pressed="false">DE</button>
  </div>
</header>

<main id="top">
  <section class="hero" aria-labelledby="hero-title">
    <video class="hero__video" autoplay muted loop playsinline preload="metadata" poster="assets/videos/thesis_line_detection.jpg" aria-hidden="true">
      <source src="assets/videos/thesis_line_detection.mp4" type="video/mp4">
    </video>
    <div class="hero__shade" aria-hidden="true"></div>
    <div class="hero__body">
      <h1 id="hero-title"><span data-en="Autonomy," data-de="Autonomie,">Autonomy,</span> <span data-en="from model to vehicle." data-de="vom Modell bis ins Fahrzeug.">from model to vehicle.</span></h1>
      {t("p", "I'm Abhishek Jha, an autonomous systems engineer in Aachen. I make perception run in real time on embedded computers, bring prototype vehicles up, and build the tests that keep them working.", "Ich bin Abhishek Jha, Ingenieur für autonome Systeme in Aachen. Ich bringe Wahrnehmung in Echtzeit auf Embedded-Rechner, nehme Prototyp-Fahrzeuge in Betrieb und baue die Tests, die sie funktionsfähig halten.", "hero__lead")}
      <div class="hero__actions">
        <a class="btn btn--primary" href="#work" data-en="See the work" data-de="Zu den Projekten">See the work</a>
        <a class="btn btn--ghost" href="mailto:abjha1998@gmail.com">abjha1998@gmail.com</a>
      </div>
    </div>
    <dl class="datum">
      <div><dt data-en="Degree" data-de="Abschluss">Degree</dt><dd data-en="M.Sc. Automation Eng., RWTH" data-de="M.Sc. Automatisierungstechnik, RWTH">M.Sc. Automation Eng., RWTH</dd></div>
      <div><dt data-en="Thesis" data-de="Masterarbeit">Thesis</dt><dd>1.0</dd></div>
      <div><dt data-en="Start" data-de="Start">Start</dt><dd data-en="immediately" data-de="sofort">immediately</dd></div>
      <div><dt data-en="Base" data-de="Ort">Base</dt><dd data-en="Aachen · will relocate" data-de="Aachen · umzugsbereit">Aachen · will relocate</dd></div>
      <div><dt data-en="Languages" data-de="Sprachen">Languages</dt><dd data-en="English · German C1" data-de="Englisch · Deutsch C1">English · German C1</dd></div>
    </dl>
  </section>

  <section class="works" id="work" aria-labelledby="work-title">
    {t("h2", "Selected work", "Ausgewählte Projekte", "section-title", ' id="work-title"')}
    {work}
    <div class="more">
      {t("h2", "More engineering", "Weitere Projekte", "section-title section-title--small")}
      <ul class="minis">{minis}
      </ul>
    </div>
  </section>

  <section class="career" id="career" aria-labelledby="career-title">
    <div class="career__intro">
      {t("h2", "Career", "Werdegang", "section-title", ' id="career-title"')}
      {t("p", "Automation engineer (M.Sc., RWTH Aachen) with work across autonomous vehicles, embedded control and test automation. Most of my work sits where software meets the machine: commissioning, measuring and finding the real cause.", "Automatisierungsingenieur (M.Sc., RWTH Aachen) mit Erfahrung in autonomen Fahrzeugen, Embedded-Regelung und Testautomatisierung. Der Großteil meiner Arbeit liegt dort, wo Software auf die Maschine trifft: Inbetriebnahme, Messen und die wahre Ursache finden.")}
      <p class="career__cv"><a class="textlink" href="https://www.linkedin.com/in/abhishek-j-3497a8121" target="_blank" rel="noopener">LinkedIn ↗</a> <a class="textlink" href="https://github.com/Abhi-Jha345" target="_blank" rel="noopener">GitHub ↗</a></p>
    </div>
    <div class="career__list">
      <ol class="jobs">{jobs}
      </ol>
      <div class="edu">
        {t("h3", "Education", "Ausbildung", "career__sub")}
        <ul>
          <li><span>04/2022 – 05/2026</span> <span data-en="M.Sc. Automation Engineering, RWTH Aachen University, thesis 1.0" data-de="M.Sc. Automatisierungstechnik, RWTH Aachen University, Masterarbeit 1,0">M.Sc. Automation Engineering, RWTH Aachen University, thesis 1.0</span></li>
          <li><span>2018 – 04/2022</span> <span data-en="B.Eng. Mechanical Engineering, FH Aachen, Department of Energy Engineering" data-de="B.Eng. Maschinenbau, FH Aachen, Fachbereich Energietechnik">B.Eng. Mechanical Engineering, FH Aachen, Department of Energy Engineering</span></li>
        </ul>
      </div>
      <div class="tools">
        {t("h3", "Toolchain", "Werkzeuge", "career__sub")}
        <dl>{tools_html}</dl>
      </div>
    </div>
  </section>

  <section class="contact" id="contact" aria-labelledby="contact-title">
    {t("h2", "Let's talk.", "Lassen Sie uns sprechen.", "contact__title", ' id="contact-title"')}
    <p class="contact__mail"><a href="mailto:abjha1998@gmail.com">abjha1998@gmail.com</a></p>
    <ul class="contact__links">
      <li><a href="tel:+4915255867075">+49 1525 5867075</a></li>
      <li><a href="https://www.linkedin.com/in/abhishek-j-3497a8121" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="https://github.com/Abhi-Jha345" target="_blank" rel="noopener">GitHub</a></li>
      <li data-en="Aachen, Germany" data-de="Aachen, Deutschland">Aachen, Germany</li>
    </ul>
  </section>
</main>
<footer class="foot"><p>© 2026 Abhishek Jha</p></footer>
<script src="js/site.js" defer></script>
</body>
</html>
'''
(ROOT / "index.html").write_text(page, encoding="utf-8")
print("index.html written", len(page))
