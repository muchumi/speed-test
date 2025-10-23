import speedtest as st

# Function
def speed_test():
    test=st.Speedtest()

    # Get download speed in Mbps
    down_speed=test.download()
    download_speed=round(down_speed / 10**6, 2)
    print("Download speed in Mbps: ", download_speed)

    # Get upload speed in Mbps
    up_speed=test.upload()
    upload_speed=round(up_speed / 10**6, 2)
    print("Upload speed in Mbps: ", upload_speed)

    # Get ping results
    ping=test.results.ping
    print("Ping: ", ping)

speed_test()

"""
    Results:

    Download speed in Mbps:  707.6
    Upload speed in Mbps:  783.33
    Ping:  2.688
"""
