import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 은재가 조사한 일주일간 유동 인구 데이터(월요일~일요일)
a = [242, 256, 237, 223, 263, 81, 46]   # 리스트에 유동 인구 데이터 초기화
# 그래프를 그리기 위한 외부 모듈 선언
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)                              # 그래프 제목에 한글 표시하기

x_data = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']  # x축에 표시할 제목 리스트에 저장
# 그래프의 제목 붙이기
plt.title('일주일간 유동 인구수 데이터', fontsize=16)         # 큰 제목
plt.xlabel('요일', fontsize=12)                           # x축 제목
plt.ylabel('유동 인구수', fontsize=12)                     # y축 제목
# 꺾은선 그래프 그리기
plt.scatter(x_data, a)
plt.plot(x_data, a)
plt.show()
