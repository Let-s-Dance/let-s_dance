import streamlit as st
import time

#todo
#원 안에 점수 넣어야 함.. 왜 안들어가노

def main():
    st.title("애니메이션 원 안에 점수와 색상 변화 표시하기")

    if st.button("작업 시작"):
        # 큰 원을 그리기 위한 div 요소 추가
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center; height: 300px;">
                <div class="circle-container">
                    <div class="circle" id="circle">
                        <div class="percent" id="percent">0%</div>
                    </div>
                </div>
            </div>
            <style>
                .circle-container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100%;
                }

                .circle {
                    position: relative;
                    width: 200px;
                    height: 200px;
                    border-radius: 50%;
                    background-color: #f3f3f3;
                    overflow: hidden;
                }

                .circle::after {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    border-radius: 50%;
                    background-color: #f3f3f3;
                    clip-path: circle();
                    animation: circle-animation 5s linear forwards;
                }

                .percent {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-size: 24px;
                    font-weight: bold;
                    color: #ffffff;
                    text-align: center; /* 텍스트 중앙 정렬 */
                    width: 100%; /* 부모 요소에 대해 100% 너비를 설정 */
                }

                @keyframes circle-animation {
                    0% {
                        background-color: #f3f3f3;
                    }
                    25% {
                        background-color: #3498db;
                    }
                    50% {
                        background-color: #f39c12;
                    }
                    75% {
                        background-color: #e74c3c;
                    }
                    100% {
                        background-color: #8e44ad;
                    }
                }
            </style>
            """
            , unsafe_allow_html=True
        )

        # 점수 업데이트 및 애니메이션 효과
        score_placeholder = st.empty()
        for score in range(0, 101, 5):
            time.sleep(0.1)  # 작업 시뮬레이션을 위한 시간 지연
            score_placeholder.text(f"{score}%")
            st.markdown(
                f"""
                <script>
                    document.getElementById('percent').textContent = '{score}%';
                </script>
                """,
                unsafe_allow_html=True
            )

        st.success('작업이 완료되었습니다!')
        st.balloons()

if __name__ == "__main__":
    main()
