def judge_it(metric,low,high,mean,deviation):
    score = 3
    std_metric_percent=((metric-low)*100)//(high-low)
    print(std_metric_percent)
    mean_percent=((mean-low)*100)//(high-low)
    print(mean_percent)
    deviation_percent=((deviation-low)*100)//(high-low)
    print(deviation_percent)
    differential=int((std_metric_percent-mean_percent)//deviation_percent)
  
    if differential>0:
        differential=min(differential,2)
    else:
        differential=max(differential,-2)
    
    score=differential+score
    return score

print(judge_it(700,0,1000,500,100))
   
