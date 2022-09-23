import cv2
import os
import datetime

video_path = 'videos/iphone_4k_30fps_30m.mov'
video_cap = cv2.VideoCapture(video_path)

#動画サイズ取得
width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#フレームレート取得
fps = video_cap.get(cv2.CAP_PROP_FPS)

#フォーマット指定
fmt = cv2.VideoWriter_fourcc(*'mp4v')

#出力
output_video = os.path.splitext(os.path.basename(video_path))[0]
dt_now = datetime.datetime.now()
fmt_dt_now = dt_now.strftime('%Y%m%d%H%M%S')
video_writer = cv2.VideoWriter(f'output_videos/{output_video}_{fmt_dt_now}.mov', fmt, fps, (width, height))

i=1
while video_cap.isOpened() :
    print("Frame: "+ str(i))
    #retには画像の取得が成功したかどうかの結果が(True/Fales)の２値で格納されている
    #ret = Return Value（戻り値）
    ret, frame = video_cap.read()

    if not ret:
        break
    if cv2.waitKey(1) == ord('q'):
        break

    cv2.imshow('Video', frame)

    #動画書き込み
    video_writer.write(frame)

    i +=1

video_cap.release()
video_writer.release() #これを忘れると出力ファイルが開きっぱなしになる
cv2.destroyAllWindows()
