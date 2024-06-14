import streamlit as st
import requests

def upload_video(file):
    #서버 URL 지정
    server_url = "http"

    #동영상 -> 파일 객체 생성
    files = {'file': file}

    #Post 요청, 서버 전송
    response = request.post(server_url, files=files)

    return response

def main():
    st.title("유저 동영상 업로드")

    col1, col2 = st.columns(2)

    with col1:
        st.header("원본 동영상")
        video_file_1 = st.file_uploader("원본 동영상을 업로드할지 서버에서 url만 받아와서 보여줄지", type=["mp4", "mov", "avi", "mkv"], key="video1")

        if video_file_1 is not None:
            st.video(video_file_1)

    with col2:
        st.header("유저 동영상")
        video_file_2 = st.file_uploader("유저 동영상을 업로드하세요", type=["mp4", "mov", "avi", "mkv"], key="video2")

        if video_file_2 is not None:
            # 업로드한 동영상 파일을 스트리밍에서 재생
            st.video(video_file_2)
            
            if st.button("서버로 전송"):
                with st.spinner("동영상을 서버로 전송 중..."):
                    response = upload_video(video_file_2)
                    if response.status_code == 200:
                        st.success("동영상이 성공적으로 서버로 전송되었습니다.")
                    else:
                        st.error("동영상 전송 중 오류가 발생했습니다.")

if __name__ == "__main__":
    main()
