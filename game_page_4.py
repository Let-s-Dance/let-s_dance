import streamlit as st

def main():
    st.title('동영상 재생')
    
    # 동영상 파일 리스트
    videos = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4"]
    
    # 하단에 동영상 리스트 출력
    st.subheader('동영상 선택')
    for video in videos:
        st.video(video)
    
    # 메인 동영상 재생 영역
    st.subheader('메인 동영상')
    selected_video = st.selectbox('재생할 동영상 선택', videos)
    st.video(selected_video)

if __name__ == "__main__":
    main()
