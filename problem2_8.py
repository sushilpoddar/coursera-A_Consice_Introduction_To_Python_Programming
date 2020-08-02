# %%
hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]


# %%
def problem2_8(temp_list):
    sum = 0
    for temp in temp_list:
        sum += temp
    avg = sum / len(temp_list)
    maxi_temp = max(temp_list)
    mini_temp = min(temp_list)
    print("Average:", avg)
    print("High:", maxi_temp)
    print("Low:", mini_temp)

# %%