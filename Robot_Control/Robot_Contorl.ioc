#include <Dynamixel2Arduino.h>
#include <ArduinoJson.h>

#if defined(ARDUINO_OpenCR)

#define DXL_SERIAL Serial3 
#define DEBUG_SERIAL Serial
const int DXL_DIR_PIN = 84;  
#endif

#define DXL_93 93
#define DXL_94 94
#define DXL_45 45
#define DXL_46 46

#define DXL_91 91
#define DXL_13 13
#define DXL_14 14
#define DXL_90 90

#define DXL_12 12
#define DXL_3 3
#define DXL_11 11
#define DXL_2 2

const uint8_t DXL_ID_1[] = {DXL_93, DXL_94, DXL_45, DXL_46}; // 관절1
const uint8_t DXL_ID_2[] = {DXL_91, DXL_13, DXL_14, DXL_90}; // 관절2
const uint8_t DXL_ID_3[] = {DXL_12, DXL_3, DXL_11, DXL_2}; // 바퀴

const uint8_t DXL_ID[] = {DXL_93, DXL_94, DXL_45, DXL_46, DXL_91, DXL_13, DXL_14, DXL_90}; // 관절

const float DXL_PROTOCOL_VERSION = 1.0;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);
using namespace ControlTableItem;

// 바퀴 모드
void wheel_mode()
{
  delay(1000);

// 어깨
  dxl.setGoalPosition(DXL_93, 550);
  dxl.setGoalPosition(DXL_94, 2030);
  dxl.setGoalPosition(DXL_45, 2320);
  dxl.setGoalPosition(DXL_46, 2220);

  delay(2000);

// 관절
  dxl.setGoalPosition(DXL_91, 2280);
  dxl.setGoalPosition(DXL_13, 2048);
  dxl.setGoalPosition(DXL_14, 1780);
  dxl.setGoalPosition(DXL_90, 3470);

}

// 4족 보행 모드
void walking_mode()
{
  // 4족 보행 모드 초기화
  dxl.setGoalPosition(DXL_91, 1200); // 오른쪽 위
  dxl.setGoalPosition(DXL_13, 3030); // 왼쪽 위
  dxl.setGoalPosition(DXL_14, 2750); // 오른쪽 아래
  dxl.setGoalPosition(DXL_90, 2450); // 왼쪽 아래

  delay(1000);

  // 다리 X자
  dxl.setGoalPosition(DXL_91, 1500); // 살짝 들기
  dxl.setGoalPosition(DXL_90, 2750);
  delay(1000);
  dxl.setGoalPosition(DXL_93, 1060); // 이동
  dxl.setGoalPosition(DXL_46, 2730);
  delay(1000);
  dxl.setGoalPosition(DXL_91, 1200); // 내리기
  dxl.setGoalPosition(DXL_90, 2450);

  delay(1000);

  dxl.setGoalPosition(DXL_13, 2730); // 살짝 들기
  dxl.setGoalPosition(DXL_14, 2450);
  delay(1000);
  dxl.setGoalPosition(DXL_94, 1520); // 이동
  dxl.setGoalPosition(DXL_45, 1810);
  delay(1000);
  dxl.setGoalPosition(DXL_13, 3030); // 내리기
  dxl.setGoalPosition(DXL_14, 2750);

  delay(1000);

  // 움직임 준비 모드
  dxl.setGoalPosition(DXL_91, 1500); // 살짝 들기
  dxl.setGoalPosition(DXL_13, 2730); 
  delay(100);
  dxl.setGoalPosition(DXL_93, 1575); // 준비 모드
  dxl.setGoalPosition(DXL_94, 1005); 
  delay(100);
  dxl.setGoalPosition(DXL_91, 1200); // 내리기
  dxl.setGoalPosition(DXL_13, 3030); 

}

// 4족 보행 모드 이동
void walking_go()
{

  // 오른쪽 위, 왼쪽 아래 : 살짝 올리기
  dxl.setGoalPosition(DXL_91, 1500); 
  dxl.setGoalPosition(DXL_90, 2750); 
  delay(200);
  // 앞으로 이동
  dxl.setGoalPosition(DXL_46, 3260); 
  dxl.setGoalPosition(DXL_93, 1060);
  // 내리기
  delay(200);
  dxl.setGoalPosition(DXL_91, 1200);
  dxl.setGoalPosition(DXL_90, 2450);

  delay(200);

  // 오른쪽 위, 왼쪽 아래 원상태 : 전진
  dxl.setGoalPosition(DXL_93, 1575);
  dxl.setGoalPosition(DXL_46, 2730);

  delay(200);

  // 왼쪽 위, 오른쪽 아래 : 살짝 올리기
  dxl.setGoalPosition(DXL_13, 2730);
  dxl.setGoalPosition(DXL_14, 2450);
  delay(200);
  // 앞으로 이동
  dxl.setGoalPosition(DXL_94, 1520);
  dxl.setGoalPosition(DXL_45, 1352);
  delay(200);
  // 내리기
  dxl.setGoalPosition(DXL_13, 3030);
  dxl.setGoalPosition(DXL_14, 2750);

  delay(200);

  dxl.setGoalPosition(DXL_91, 1400); // 전진
  dxl.setGoalPosition(DXL_90, 2650);

  delay(200); 
  // 왼쪽 위, 오른쪽 아래 원상태
  dxl.setGoalPosition(DXL_94, 1005); // 전진
  dxl.setGoalPosition(DXL_45, 1810);

  delay(200);

}

// 4족 보행 모드 정지
void walking_stop()
{
  dxl.setGoalPosition(DXL_91, 1200); // 오른쪽 위
  dxl.setGoalPosition(DXL_13, 3030); // 왼쪽 위
  dxl.setGoalPosition(DXL_14, 2750); // 오른쪽 아래
  dxl.setGoalPosition(DXL_90, 2450); // 왼쪽 아래

  delay(1000);

  dxl.setGoalPosition(DXL_93, 15750); // 이동
  dxl.setGoalPosition(DXL_46, 2730);
  dxl.setGoalPosition(DXL_94, 1005); // 이동
  dxl.setGoalPosition(DXL_45, 1810);

}

// 바퀴 모드 이동
void wheel_go()
{

  delay(1000);
  
  // 바퀴 모드 초기화
  dxl.setGoalPosition(DXL_91, 2180);
  dxl.setGoalPosition(DXL_13, 2148);
  dxl.setGoalPosition(DXL_14, 1880);
  dxl.setGoalPosition(DXL_90, 3370);

  delay(500);  
  
  // 전진
  dxl.setGoalVelocity(DXL_12, 1500); // 오른쪽 위
  dxl.setGoalVelocity(DXL_11, 1500); // 오른쪽 아래

  dxl.setGoalVelocity(DXL_3, 500); // 왼쪽 위
  dxl.setGoalVelocity(DXL_2, 500); // 왼쪽 아래
  
}

// 정지
void wheel_stop()
{
  delay(1000);

  dxl.setGoalVelocity(DXL_12, 0); // 오른쪽 위
  dxl.setGoalVelocity(DXL_11, 0); // 오른쪽 아래

  dxl.setGoalVelocity(DXL_3, 0); // 왼쪽 위
  dxl.setGoalVelocity(DXL_2, 0); // 왼쪽 아래
}

void setup() 
{

  DEBUG_SERIAL.begin(115200);


  dxl.begin(1000000); // 통신 속도

  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION); // 프로토콜 지정

// 모터 초기화
  for(int i = 0; i < 4; i++)
  {
    dxl.torqueOff(DXL_ID_1[i]);
    dxl.setOperatingMode(DXL_ID_1[i], OP_POSITION);
    dxl.torqueOn(DXL_ID_1[i]);
  }

  for(int i = 0; i < 4; i++)
  {
    dxl.torqueOff(DXL_ID_2[i]);
    dxl.setOperatingMode(DXL_ID_2[i], OP_POSITION);
    dxl.torqueOn(DXL_ID_2[i]);
  }

  for(int i = 0; i < 4; i++)
  {
    dxl.torqueOff(DXL_ID_3[i]);
    dxl.setOperatingMode(DXL_ID_3[i], OP_VELOCITY);
    dxl.torqueOn(DXL_ID_3[i]);
  }

  // 모터 속도

  for(int i = 0; i < 8; i++)
  {
    dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID[i], 80);
  }
  dxl.writeControlTableItem(MOVING_SPEED, DXL_94, 100);
  dxl.writeControlTableItem(MOVING_SPEED, DXL_93, 100);

}

void loop() 
{
    if(Serial.available())
  {
    String data = Serial.readStringUntil(0x0a);

    StaticJsonDocument<48> doc;

    // Stream& input;
    deserializeJson(doc, data);
    
    String robot_button = doc["button"]; // 버튼
    String robot_mode = doc["mode"]; // 모드

    if(robot_button == "1"){
      if(robot_mode == "walking_mode")
      {
        walking_mode();
      }
    }

    if(robot_button == "2"){
      if(robot_mode == "wheel_mode")
      {
        wheel_mode(); 
      }
    }

    if(robot_button == "3"){
      if(robot_mode == "walking")
      {
        walking_go();
      }
    }    
    
    if(robot_button == "4"){
      if(robot_mode == "walking_stop")
      {
        walking_stop();
      }
    }

    if(robot_button == "5"){
      if(robot_mode == "wheel")
      {
        wheel_go(); 
      }
    }

    if(robot_button == "6"){
      if(robot_mode == "wheel_stop")
      {
        wheel_stop();
      }
    }
  }

}


// 장애물 극복 알고리즘 (박스 넘기)
void pass()
{ 
  // 장애물 극복 초기화 
  dxl.setGoalPosition(DXL_91, 1200);
  dxl.setGoalPosition(DXL_13, 3030);
  dxl.setGoalPosition(DXL_14, 2750);
  dxl.setGoalPosition(DXL_90, 2450);

  delay(1000);

  dxl.setGoalPosition(DXL_94, 1520);
  
  delay(2000);
  
  dxl.setGoalPosition(DXL_91, 1500);

  dxl.setGoalPosition(DXL_93, 1060);

  delay(500);

  dxl.setGoalPosition(DXL_91, 1200);

  /////////////////////

  delay(1000);

  // 오른쪽 다리 : 장애물에 걸치기
  dxl.setGoalPosition(DXL_93, 1360); // 75도
  dxl.setGoalPosition(DXL_91, 2280); // 다리 들기
  delay(1000);
  dxl.setGoalPosition(DXL_93, 550);

  delay(2000);

  // 왼쪽 다리 : 장애물에 걸치기
  dxl.setGoalPosition(DXL_94, 1220); // 75도
  dxl.setGoalPosition(DXL_13, 1948); // 다리 들기
  delay(1000);
  dxl.setGoalPosition(DXL_94, 2030);

  delay(3000);

  // 뒷다리 ㄱ자
  dxl.setGoalPosition(DXL_45, 2310); 
  dxl.setGoalPosition(DXL_46, 2230);

  delay(1000);

  // 앞 다리 바퀴 활성화
  dxl.setGoalVelocity(DXL_12, 1500);
  dxl.setGoalVelocity(DXL_3, 500);

  delay(4000);

  // 장애물 끝까지 이동 시 바퀴 종료
  dxl.setGoalVelocity(DXL_12, 0);
  dxl.setGoalVelocity(DXL_3, 0);

  delay(1000);

  // 앞다리 ㄱ자
  dxl.setGoalPosition(DXL_91, 850);
  dxl.setGoalPosition(DXL_13, 3380);

  delay(3000);
  
  // 앞다리 펼치기
  dxl.setGoalPosition(DXL_93, 1575);
  dxl.setGoalPosition(DXL_94, 1005);

  delay(4000);

  // 왼쪽 뒷발 올리기
  dxl.setGoalPosition(DXL_91, 1500);
  dxl.setGoalPosition(DXL_90, 3470);
  delay(1000);
  dxl.setGoalPosition(DXL_46, 3260);
  dxl.setGoalPosition(DXL_93, 1060);
  delay(1000);
  dxl.setGoalPosition(DXL_91, 1500);
  dxl.setGoalPosition(DXL_90, 2750);
  delay(1000);
  dxl.setGoalPosition(DXL_94, 1520);

  delay(1000);

  // 앞발, 왼쪽 뒷발 장애물에 눕기  
  dxl.setGoalPosition(DXL_91, 2280);
  dxl.setGoalPosition(DXL_13, 2048);

  delay(500);

  dxl.setGoalPosition(DXL_90, 3470);

  delay(1000);

  // 나머지 오른쪽 뒷발 장애물에 올리기
  dxl.setGoalPosition(DXL_14, 1080); 
  delay(1000);
  dxl.setGoalPosition(DXL_45, 1352);
  delay(1000);
  dxl.setGoalPosition(DXL_14, 1780);

  delay(2000);


  // 장애물 위에서 서기
  dxl.setGoalPosition(DXL_14, 2750);
  dxl.setGoalPosition(DXL_90, 2450);
  delay(300);
  dxl.setGoalPosition(DXL_91, 1200);
  dxl.setGoalPosition(DXL_13, 3030);

  delay(1000);


  // 앞발 일자
  dxl.setGoalPosition(DXL_93, 550);
  dxl.setGoalPosition(DXL_94, 2030);
  delay(1000);
  dxl.setGoalPosition(DXL_91, 2180);
  dxl.setGoalPosition(DXL_13, 2148);

  delay(1000);

  // 앞 다리 바퀴 활성화
  dxl.setGoalVelocity(DXL_12, 1500); // 바퀴
  dxl.setGoalVelocity(DXL_3, 500); // 바퀴

  delay(1000);

    // 장애물 통과 시 뒤 바퀴 일자
  dxl.setGoalPosition(DXL_45, 2320);
  dxl.setGoalPosition(DXL_46, 2220);

  delay(5000);

  dxl.setGoalPosition(DXL_14, 1880);
  dxl.setGoalPosition(DXL_90, 3370);

  delay(1000);

  dxl.setGoalVelocity(DXL_11, 1500); // 오른쪽 아래
  dxl.setGoalVelocity(DXL_2, 500); // 왼쪽 아래

  delay(3000);

  dxl.setGoalVelocity(DXL_12, 0); // 바퀴
  dxl.setGoalVelocity(DXL_3, 0); // 바퀴
  dxl.setGoalVelocity(DXL_11, 0);
  dxl.setGoalVelocity(DXL_2, 0);

}

