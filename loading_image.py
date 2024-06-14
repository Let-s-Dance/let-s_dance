import streamlit as st
import time

#todo
#로딩화면 실행 시, 하단에 이상한 것 뜸

def main():
    st.title("로딩 애니메이션 예제")

    if st.button("로딩 시작"):
        loading_placeholder = st.empty()

        loading_html = """
        <div style="display: flex; justify-content: center; align-items: center; height: 300px;">
            <div class="loader"></div>
        </div>
        <style>
        .loader {
            border: 16px solid #f3f3f3;
            border-radius: 50%;
            border-top: 16px solid #3498db;
            border-right: 16px solid #f39c12;
            border-bottom: 16px solid #e74c3c;
            border-left: 16px solid #8e44ad;
            width: 120px;
            height: 120px;
            animation: spin 2s linear infinite, color-change 4s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes color-change {
            0% { border-top-color: #3498db; border-right-color: #f39c12; border-bottom-color: #e74c3c; border-left-color: #8e44ad; }
            25% { border-top-color: #8e44ad; border-right-color: #3498db; border-bottom-color: #f39c12; border-left-color: #e74c3c; }
            50% { border-top-color: #e74c3c; border-right-color: #8e44ad; border-bottom-color: #3498db; border-left-color: #f39c12; }
            75% { border-top-color: #f39c12; border-right-color: #e74c3c; border-bottom-color: #8e44ad; border-left-color: #3498db; }
            100% { border-top-color: #3498db; border-right-color: #f39c12; border-bottom-color: #e74c3c; border-left-color: #8e44ad; }
        }
        </style>
        """
        
        loading_placeholder.markdown(loading_html, unsafe_allow_html=True)

        # 실제 작업 수행 (여기서는 5초 동안 대기)
        time.sleep(5)

        # 작업 완료 후 로딩 애니메이션 제거
        loading_placeholder.empty()

        st.success('로딩 끝')
        st.balloons()

if __name__ == "__main__":
    main()
