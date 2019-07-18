import re


def solution(d_str):
    area_score = {'S': 1, 'D': 2, 'T': 3}
    d_list = re.findall(r'\d+[SDT][*#]*', d_str)
    score_list = []
    for idx, d in enumerate(d_list):
        score = int(re.match(r'\d+', d).group())
        area = re.search(r'[SDT]', d).group()
        price = re.findall(r'[*#]', d)

        score_list.append(score**area_score[area])
        if price:
            if price[0] == '*':
                score_list[idx] = score_list[idx] * 2
                if idx > 0:
                    score_list[idx-1] = score_list[idx-1] * 2
            else:
                score_list[idx] = score_list[idx] * -1
    return sum(score_list)


if __name__ == '__main__':
    dart_result = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']
    for dart in dart_result:
        solution(dart)
