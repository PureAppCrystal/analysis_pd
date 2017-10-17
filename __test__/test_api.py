import collection.api as pdapi

'''
url = pdapi.pd_gen_url(
    "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList",
    YM="{0:04d}{1:02d}".format(2017, 1),
    SIDO="서울특별시",
    GUNGU="",
    RES_NM="",
    numOfRows=100,
    _type="json",
    pageNo=2
)
'''


# test from pd_fetch_tourspot
for year in range(2017, 2018):
    for month in range(1, 13):
        for item in pdapi.pd_fetch_tourspot_visitor(district1="하남시",  year=year, month=month):
            print(item)


