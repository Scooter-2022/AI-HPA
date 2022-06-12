predicted_workload = [600, 800, 900, 700, 500]
workload_max = 120
pods_curr = 2
pods_min = 1
RRS = 0.7

# Input code needed
# while True:
    # workload_next=input()
    # if workload_next=='q': break
for workload_next in predicted_workload:
    pods_next = workload_next // workload_max
    if pods_next > pods_curr:
        pods_curr = pods_next
        print("pods_init: %f"%pods_curr)
        continue
    elif pods_next < pods_curr:
        pods_next = max(pods_next, pods_min)
        pods_surplus = int((pods_curr - pods_next) * RRS)
        pods_next = pods_curr - pods_surplus
        pods_curr = pods_next
        print("pods_init: %f"%pods_curr)
        print("pods_surplus: %f" % pods_surplus)
        continue
    else:
        continue
