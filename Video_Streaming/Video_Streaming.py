import cv2
import torch
from flask import Flask, Response, render_template
from threading import Thread

app = Flask(__name__)

# YOLOv5 모델 로드 (커스텀 학습 모델 사용 : 장애물 객체 인식)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='ob.pt', force_reload=True)


# ==============================
# 멀티스레드 비디오 스트리밍 클래스
# ==============================
class VideoStream:
    def __init__(self):
        # 웹캠 연결
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # 해상도 가로 640
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 해상도 세로 480
        self.cap.set(cv2.CAP_PROP_FPS, 5)             # FPS 5로 제한
        self.grabbed, self.frame = self.cap.read()
        self.stopped = False
        # 비디오 프레임을 계속 읽어오는 스레드 실행
        Thread(target=self.update, args=()).start()

    def update(self):
        """웹캠에서 프레임을 계속 읽어옴"""
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                self.grabbed, self.frame = self.cap.read()

    def read(self):
        """현재 프레임 반환"""
        return self.grabbed, self.frame

    def stop(self):
        """비디오 스트리밍 중지"""
        self.stopped = True
        self.cap.release()


# ==============================
# YOLO 탐지 및 스트리밍 함수
# ==============================
def generate_frames(stream):
    while True:
        success, frame = stream.read()
        if not success:
            break
        else:
            # YOLOv5로 객체 탐지 실행
            results = model(frame)

            # 탐지 결과 배열 가져오기 (x1, y1, x2, y2, confidence, class)
            detections = results.xyxy[0].cpu().numpy()
            for detection in detections:
                xmin, ymin, xmax, ymax, conf, cls = detection
                # 신뢰도 70% 이상만 표시
                if conf >= 0.7:
                    # 탐지 박스 그리기
                    cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
                    # 클래스 라벨과 신뢰도 표시
                    label = f"{model.names[int(cls)]} {conf:.2f}"
                    cv2.putText(frame, label, (int(xmin), int(ymin) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # 프레임을 JPEG로 인코딩
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Flask에서 MJPEG 스트리밍으로 전송
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# ==============================
# Flask 라우트
# ==============================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """실시간 비디오 스트리밍"""
    return Response(generate_frames(stream), mimetype='multipart/x-mixed-replace; boundary=frame')


# ==============================
# 메인 실행
# ==============================
if __name__ == '__main__':
    # VideoStream 객체 생성
    stream = VideoStream()
    # Flask 서버 실행 (모든 IP에서 접속 허용)
    app.run(host='0.0.0.0', port=5000)
