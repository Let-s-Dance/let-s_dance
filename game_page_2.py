import streamlit as st
import time

def main():
    st.title("로딩 화면 예제")

    # 버튼을 눌러 작업을 시작합니다.
    if st.button("작업 시작"):
        with st.spinner('로딩 중...'):
            # 여기서 실제로 수행할 작업을 시뮬레이션합니다.
            time.sleep(5)  # 예를 들어, 5초 동안 기다림

        st.success('작업이 완료되었습니다!')
        st.balloons()

if __name__ == "__main__":
    main()
