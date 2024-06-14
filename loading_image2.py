import streamlit as st
import time

def main():
    st.title("로딩 애니메이션 및 % 표시 예제")

    if st.button("작업 시작"):
        progress_bar = st.progress(0)

        for percent_complete in range(0, 101, 10):
            time.sleep(1)
            progress_bar.progress(percent_complete)

        st.success('작업이 완료되었습니다!')
        st.balloons()

if __name__ == "__main__":
    main()
