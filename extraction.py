import tweets_nifty
import time

tweets_nifty.init()

for i in range(3,31) : 
    name = "Nifty 50 Data\\t"
    if(i<=8) : name = name + f"Jan-0{9-i}"
    else :
        name = name + "Dec-"
        date = 40-i
        if(date<10) : name = name + "0"
        name = name + date
    name = name + ".csv"
    print(name)
    
    tweets_nifty.scrape(i,name)
    # except :
    #     time.sleep(900)
    #     try : tweets_nifty.scrape(i,name)
    #     except :
    #         print("Excecution stopped at",i)
    #         break 
    time.sleep(300)