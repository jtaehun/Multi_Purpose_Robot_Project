💻[원격 제어 UI 및 웹 생성]

Node-RED

- Flask에서 생성한 YOLO 스트리밍을 웹에서 생성
- Walking_Mode, Wheel_Mode, Go, Stop 등 버튼 생성
- 생성한 버튼은 시리얼로 아누이노 코드 제어[로봇 제어]
- 카메라 이미지 프레임을 실시간으로 Node-RED 대시보드에 표시

[FLOW1]

Flask 서버를 웹으로 연결

[FLOW2]

Walking_Mode, Wheel_Mode, Go, Stop 버튼 생성
생성한 버튼을 시리얼을 통해 아두이노와 연결

[FLOW3]

카메라 이미지 프레임을 실시간으로 변환해 Node-RED 대시보드에 표시
