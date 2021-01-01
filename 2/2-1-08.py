import csv
import matplotlib.pyplot as plt                                 # 그래프를 출력하기 위한 모듈
a = [[], [], [], [], [], [], []]
with open('./2-1/passby_data.CSV', 'r') as f:
    reader = csv.DictReader(f)
    i = j = 0                                                   # i, j 변수 선언 및 초기화
    for row in reader:                                          # csv 파일에 저장된 데이터 수만큼 반복
        a[i].append(row)                                        # i번째 리스트에 csv 파일의 row행 추가
        j = j + 1                                               # 24개 행을 추가한 후, 다음 요일의 리스트로 이동
        if(j % 24 == 0):
            i = i + 1

day_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']   # 요일 제목
hour_title = ['01', '02', '03', '04', '05', '06',
              '07', '08', '09', '10', '11', '12',
              '13', '14', '15', '16', '17', '18',
              '19', '20', '21', '22', '23', '24']
# 시간대별로 주간 평균 구하기
avgh = []
for j in range(0, 24):                                              # 0~23시간만큼 19~24행 반복
    day_sum = 0                                                     # 시간대별 합을 구하기 위해 0으로 초기화
    # j번째 시간대 주간 총합
    for i in range(0, 7):                                           # 일주일, 즉 7번 반복하기
        day_sum = day_sum + int(a[i][j]['num'])                     # i번째 요일에 j번째 시간대별 행인수 누적

    avgh.append(day_sum / 7)                                        # j번째 시간대별 주간 평균 구하기

bvgh = []
for j in range(0, 24):                                              # 0~23시간만큼 19~24행 반복
    day_sum = 0                                                     # 시간대별 합을 구하기 위해 0으로 초기화
    # j번째 시간대 주간 총합
    for i in range(0, 7):                                           # 일주일, 즉 7번 반복하기
        day_sum = day_sum + int(a[i][j]['wnum'])                     # i번째 요일에 j번째 시간대별 행인수 누적

    bvgh.append(day_sum / 7)                                        # j번째 시간대별 주간 평균 구하기

cvgh = []
for j in range(0, 24):                                              # 0~23시간만큼 19~24행 반복
    day_sum = 0                                                     # 시간대별 합을 구하기 위해 0으로 초기화
    # j번째 시간대 주간 총합
    for i in range(0, 7):                                           # 일주일, 즉 7번 반복하기
        day_sum = day_sum + int(a[i][j]['ynum'])                     # i번째 요일에 j번째 시간대별 행인수 누적

    cvgh.append(day_sum / 7)                                        # j번째 시간대별 주간 평균 구하기

# 그래프의 제목 붙이기
plt.title('hourly passerby data', fontsize=16)                      # 그래프 제목
plt.xlabel('hour', fontsize=12)                                     # x축 제목
plt.ylabel('number of passerby', fontsize=12)                       # y축 제목

plt.scatter(hour_title, avgh)                                       # 꺾은선 그래프 그리기
plt.plot(hour_title, avgh)
# plt.scatter(hour_title, bvgh)                                       # 꺾은선 그래프 그리기
plt.plot(hour_title, bvgh)
# plt.scatter(hour_title, cvgh)                                       # 꺾은선 그래프 그리기
plt.plot(hour_title, cvgh)
plt.show()
