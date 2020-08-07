from datetime import datetime

date_list = ['2018-11-03 18:21:26', '2018-11-05 10:12:15','2019-01-03 15:29:10' , '2020-03-07 10:10:20','2020-08-02 16:33:06']

# con_date_list = [datetime.strptime(i, '%Y-%m-%d %H:%M:%S') for i in date_list]



d = {'Monstera Deliciosa': date_list[0], 'banana': date_list[1], 'almond': date_list[2] , 'beetroot': date_list[3], 'peach': date_list[4]}


result = sorted(d.items(), key=lambda x: -(x[1], x[0]))

# convert tuple to dictionary
sorted_dictionary = dict(result)
